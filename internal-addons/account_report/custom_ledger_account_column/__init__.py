from . import models


def post_init_hook(env):
    registry = env.registry
    # Evitamos errores si el modelo no está presente
    if "account.general.ledger" not in registry.models:
        return
    Model = registry["account.general.ledger"]
    Original = getattr(Model, "_get_lines", None)
    Original_cols = getattr(Model, "_get_columns_name", None)

    def _get_lines(self, options, line_id=None):
        lines = Original(self, options, line_id) if Original else []
        current_account_code = ""
        current_account_name = ""
        for line in lines:
            if line.get("level") == 1 and line.get("name"):
                current_account_name = line["name"]
                current_account_code = line.get("columns", [{}])[0].get("name", "")
            if line.get("caret_options") == "account.move.line":
                line.setdefault("columns", [])
                # referencia del movimiento: preferimos line['name'] si existe
                move_ref = line.get("name") or line.get("columns", [{}])[0].get("name", "")
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

    Model._get_lines = _get_lines

    def _get_columns_name(self, options):
        cols = Original_cols(self, options) if Original_cols else []
        # Añadimos encabezados al inicio: código cuenta, nombre cuenta, referencia movimiento
        return [
            "Código cuenta",
            "Cuenta",
            "Referencia movimiento",
        ] + cols

    Model._get_columns_name = _get_columns_name
