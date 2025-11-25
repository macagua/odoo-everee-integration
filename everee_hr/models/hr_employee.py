import base64
import logging

import requests

from odoo import _, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    is_onboarding_started = fields.Boolean(
        string="Is this employee onboard on Everee?",
        help="Check this box to mark the employee as onboarding complete.",
        default=False,
        copy=False,
    )

    def post_onboarding_employee(self):
        """Post the employee data to Everee Onboarding API."""

        ICP = self.env["ir.config_parameter"].sudo()
        api_base_url = ICP.get_param(
            "everee_base.base_url", "https://api.everee.com/api/v2"
        )
        api_base_url = api_base_url[:-1] if api_base_url.endswith("/") else api_base_url
        api_token = ICP.get_param("everee_base.api_token")
        tenant_id = ICP.get_param("everee_base.tenant_id")

        # Encode API token in Base64
        encoded_token = base64.b64encode(api_token.encode()).decode()
        firstName = self.name.split()[0]
        lastName = self.name.split()[-1]
        email = self.work_email or self.private_email
        phone = self.work_phone or self.mobile_phone
        amount = 0
        currency = self.env.user.company_id.currency_id.name or "USD"
        pay_type = "HOURLY"
        typical_weekly_hours = 40
        street = self.private_street or ""
        street2 = self.private_street2 or ""
        city = self.private_city or ""
        state = self.private_state_id.name or ""
        zip_code = self.private_zip or ""
        hire_date = "2025-04-01"

        # Construct the URL
        # url = "https://api.everee.com/api/v2/onboarding/employee"
        url = api_base_url + "/onboarding/employee"

        # Request payload
        payload = {
            "payType": pay_type,
            "payRate": {"amount": amount, "currency": currency},
            "typicalWeeklyHours": typical_weekly_hours,
            "eligibleForOvertime": True,
            "legalWorkAddress": {"useHomeAddress": False},
            "homeAddress": {
                "line1": street,
                "line2": street2,
                "city": city,
                "state": state,
                "postalCode": zip_code,
            },
            "firstName": firstName,
            "lastName": lastName,
            "phoneNumber": phone,
            "email": email,
            "hireDate": hire_date,
        }

        # Headers
        headers = {
            "accept": "application/json",
            "authorization": f"Basic {encoded_token}",
            "x-everee-tenant-id": tenant_id,
            "content-type": "application/json",
        }

        try:
            # Request to Everee API
            response = requests.post(url, json=payload, headers=headers, timeout=1.50)
            # Check if the response is successful
            if response.status_code == 201:
                message_log = (
                    f"Employee {self.name} is already in the onboarding process",
                )
                # Log the request to the database
                self.env["ir.logging"].sudo().create(
                    {
                        "name": "Employee was exported to Everee",
                        "type": "server",
                        "level": "info",
                        "dbname": self._cr.dbname,
                        "message": message_log,
                        "path": "everee_hr/models/hr_employee.py",
                        "func": "action_everee_onboarding",
                        "line": 22,  # approximate line, optional
                    }
                )
                # Log the request to the console
                _logger.info(
                    f"Request to {url} returned {response.status_code}: {response.text}"
                )
                # Return a notification with the number of workers found
                return {
                    "type": "ir.actions.client",
                    "tag": "display_notification",
                    "params": {
                        "title": _("Employee data Successfully published"),
                        "message": _(
                            "Employee data has been successfully published on Everee."
                        ),
                        "type": "success",
                        "sticky": False,
                    },
                }
            else:
                # Show an error message to the user
                raise UserError(_(f"Error on Onboarding API: {response.text}"))
        except requests.exceptions.RequestException as e:
            # Log the request to the database
            self.env["ir.logging"].sudo().create(
                {
                    "name": "Everee Connection Error",
                    "type": "server",
                    "level": "error",
                    "dbname": self._cr.dbname,
                    "message": f"Connection error: {str(e)}",
                    "path": "everee_base/models/res_config_settings.py",
                    "func": "action_test_everee_connection",
                    "line": 36,  # approximate line, optional
                }
            )
            # Log the error to the console
            _logger.error(f"Connection error: {e}")
            # Show an error message to the user
            raise UserError(_(f"Connection error: {e}")) from e

    def action_everee_onboarding(self):
        """Open Everee Onboarding wizard or execute onboarding process."""
        self.ensure_one()
        # Call the onboarding API
        return self.post_onboarding_employee()
