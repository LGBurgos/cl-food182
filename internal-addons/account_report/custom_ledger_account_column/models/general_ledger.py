from odoo import models

# Helper reutilizable: inyecta código, nombre de cuenta y referencia del movimiento
def inject_account_columns(lines):
    current_account_code = ""
    current_account_name = ""

    for line in lines:
        if line.get("level") == 1 and line.get("name"):
            current_account_name = line["name"]
            current_account_code = line.get("columns", [{}])[0].get("name", "")

        if line.get("caret_options") == "account.move.line":
            # move reference: prefer line['name'] (habitual en reportes), sino fallback a la primera columna
            move_ref = line.get("name") or line.get("columns", [{}])[0].get("name", "")
            line.setdefault("columns", [])
            # Insertar en el orden: código cuenta, nombre cuenta, referencia movimiento
            line["columns"].insert(0, {
                "name": current_account_code,
                "no_format": current_account_code,
            })
            line["columns"].insert(1, {
                "name": current_account_name,
                "no_format": current_account_name,
            })
            line["columns"].insert(2, {
                "name": move_ref,
                "no_format": move_ref,
            })

    return lines
