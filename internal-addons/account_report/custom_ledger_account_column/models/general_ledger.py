from odoo import models

class GeneralLedgerReport(models.AbstractModel):
    _inherit = "account.general.ledger"

    def _get_lines(self, options, line_id=None):
        lines = super()._get_lines(options, line_id)

        current_account_code = ""
        current_account_name = ""

        for line in lines:
            # Detect account header
            if line.get("level") == 1 and line.get("name"):
                current_account_name = line["name"]
                current_account_code = line.get("columns", [{}])[0].get("name", "")

            # Detect move line entries
            if line.get("caret_options") == "account.move.line":
                line.setdefault("columns", [])

                # Insert invisible columns at the beginning for export
                line["columns"].insert(0, {
                    "name": current_account_code,
                    "no_format": current_account_code,
                })
                line["columns"].insert(1, {
                    "name": current_account_name,
                    "no_format": current_account_name,
                })

        return lines
