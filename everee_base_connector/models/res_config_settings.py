import base64
import logging

import requests

from odoo import _, fields, models
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    everee_enabled = fields.Boolean(
        string="Enable Everee Integration",
        config_parameter="everee_base_connector.enabled",
    )
    api_base_url = fields.Char(
        string="Everee API Base URL",
        config_parameter="everee_base_connector.base_url",
        default="https://api.everee.com/api/v2",
        required=True,
    )
    tenant_id = fields.Char(
        string="Company tenant ID",
        config_parameter="everee_base_connector.tenant_id",
        required=True,
    )
    api_token = fields.Char(
        string="Everee API Key",
        config_parameter="everee_base_connector.api_token",
        required=True,
    )

    def action_test_everee_connection(self):
        self.ensure_one()
        # Encode API token in Base64
        encoded_token = base64.b64encode(self.api_token.encode()).decode()
        # Headers
        headers = {
            "accept": "application/json",
            "authorization": f"Basic {encoded_token}",  # Basic Auth
            "x-everee-tenant-id": f"{self.tenant_id}",  # tenant ID
            "content-type": "application/json",
        }
        # Construct the URL
        url = f"{self.api_base_url}/workers?page=0&size=20"

        try:
            # Request to Everee API
            response = requests.get(url, headers=headers, timeout=10)
            # Check if the response is successful
            if response.status_code == 200:
                message_log = (
                    f"Request to {url} returned ",
                    f"{response.status_code}: {response.text}",
                )
                self.env["ir.logging"].sudo().create(
                    {
                        "name": "Everee Connection",
                        "type": "server",
                        "level": "info",
                        "dbname": self._cr.dbname,
                        "message": message_log,
                        "path": "everee_base_connector/models/res_config_settings.py",
                        "func": "action_test_everee_connection",
                        "line": 27,  # approximate line, optional
                    }
                )
                _logger.info(
                    f"Request to {url} returned {response.status_code}: {response.text}"
                )

                workers_total = response.json()
                return {
                    "type": "ir.actions.client",
                    "tag": "display_notification",
                    "params": {
                        "title": _("Everee Connection Successful"),
                        "message": _(
                            "Successfully connected. Workers found: ",
                            f"{len(workers_total)}",
                        ),
                        "type": "success",
                        "sticky": False,
                    },
                }
            else:
                _logger.error(
                    "Failed to connect to Everee API. Status Code: "
                    f"{response.status_code}, Response: {response.text}"
                )
                raise UserError(
                    _(
                        "Failed to connect to Everee API.\nStatus Code: ",
                        f"{response.status_code}\nResponse: {response.text}",
                    )
                )
        except requests.exceptions.RequestException as e:
            self.env["ir.logging"].sudo().create(
                {
                    "name": "Everee Connection Error",
                    "type": "server",
                    "level": "error",
                    "dbname": self._cr.dbname,
                    "message": f"Connection error: {str(e)}",
                    "path": "everee_base_connector/models/res_config_settings.py",
                    "func": "action_test_everee_connection",
                    "line": 27,  # approximate line, optional
                }
            )
            _logger.error(f"Connection error: {e}")
            raise UserError(_(f"Connection error: {e}")) from e
