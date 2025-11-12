import base64
import logging

import requests

from odoo import _, api, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class HrEmployee(models.Model):
    _inherit = "hr.employee"

    is_onboarding_started = fields.Boolean(
        string="Is this employee onboard on Everee?",
        help="Check this box to mark the employee as onboarding complete.",
        default=False,
        readonly=True,
        states={'default': [('readonly', False)]},
        copy=False,
        tracking=True
    )

    def post_onboarding_employee(self):
        """Post the employee data to Everee Onboarding API."""

        # Encode API token in Base64
        encoded_token = base64.b64encode(self.company_id.api_token.encode()).decode()

        # Request payload
        payload = {
            "payType": "HOURLY",
            "payRate": {
                "amount": "2000",
                "currency": "USD"
            },
            "typicalWeeklyHours": 40,
            "eligibleForOvertime": True,
            "legalWorkAddress": {
                "useHomeAddress": True,
                #"workLocationId": "Calle lope de Rueda"
            },
            "firstName": "Edu Test",
            "lastName": "Moreno Test",
            "phoneNumber": "7734498461",
            "email": "eduardo+test@gobonum.com",
            "hireDate": "2025-04-03"
        }

        # Headers
        headers = {
            "accept": "application/json",
            "authorization": f"Basic {encoded_token}",
            "x-everee-tenant-id": self.company_id.tenant_id,
            "content-type": "application/json"
        }
        # Construct the URL
        url = self.company_id.api_base_url + "onboarding/employee"

        # Request to Everee API
        response = requests.post(url, json=payload, headers=headers)
        # Check if the response is successful
        if response.status_code == 201:
            return response.json()
            message_log = (
                f"Employee {self.name} is already in the onboarding process",
            )
            # Log the request to the database
            self.env["ir.logging"].sudo().create(
                {
                    "name": "Employee selected was exported to Everee",
                    "type": "server",
                    "level": "info",
                    "dbname": self._cr.dbname,
                    "message": message_log,
                    "path": "everee_hr/models/hr_employee.py",
                    "func": "action_export_employees_everee",
                    "line": 110,  # approximate line, optional
                }
            )
            # Log the request to the console
            _logger.info(
                f"Request to {url} returned {response.status_code}: {response.text}"
            )
            # Get the number of workers found
            workers_total = response.json()
            # Return a notification with the number of workers found
            return {
                "type": "ir.actions.client",
                "tag": "display_notification",
                "params": {
                    "title": _("Everee Connection Successful"),
                    "message": _(
                        "Successfully connected. Workers found: %d")
                        % len(workers_total),
                    ),
                    "type": "success",
                    "sticky": False,
                },
            }
        else:
            # Show an error message to the user
            raise UserError(
                _("Error on Onboarding API: %s") % response.text
            )

    @api.onchange('is_onboarding_started')
    def _onchange_is_onboarding_started(self):
        for line in self:
            if not line.res_model_id or not line.res_id:
                continue
            action = _('Unarchived') if line.is_onboarding_started else _('Archived')
            line.execution_details = '%s %s #%s' % (action, line.res_model_id.name, line.res_id)
            self.env[line.res_model].sudo().browse(line.res_id).write({'active': line.is_onboarding_started})

    def action_export_employees_everee(self):
        for line in self:
            if self.is_onboarding_started:
                raise UserError(
                    _(
                        "The employee is already in the onboarding process."
                    )
                )
            line.is_onboarding_started = True
            line._onchange_is_onboarding_started()

