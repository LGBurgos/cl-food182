from odoo import models

# Helper reutilizable: inyecta código y nombre de cuenta en las líneas ya construidas.
def inject_account_columns(lines):
    current_account_code = ""
    current_account_name = ""

    for line in lines:
        if line.get("level") == 1 and line.get("name"):
            current_account_name = line["name"]
            current_account_code = line.get("columns", [{}])[0].get("name", "")

        if line.get("caret_options") == "account.move.line":
            line.setdefault("columns", [])
            line["columns"].insert(0, {
                "name": current_account_code,
                "no_format": current_account_code,
            })
            line["columns"].insert(1, {
                "name": current_account_name,
                "no_format": current_account_name,
            })

    return lines
