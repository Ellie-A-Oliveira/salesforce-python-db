from helper.create_class import create_class

recurso_field_mapping = {
    "id": {
        "db_field_name": "recursos_id",
        "is_pk": True,
        "type": int,
        "validation_rules": ["required"]
    },
    "nome": {
        "db_field_name": "recursos_nome",
        "type": str,
        "validation_rules": ["required"]
    },
    "notas": {
        "db_field_name": "recursos_notas",
        "type": float,
        "validation_rules": ["required"]
    },
    "descricao": {
        "db_field_name": "recursos_desc",
        "type": str,
        "validation_rules": ["required"]
    },
    "categoria": {
        "db_field_name": "recursos_categ",
        "type": str,
        "validation_rules": ["required"]
    }
}

Recurso = create_class("Recurso", recurso_field_mapping, "recursos")