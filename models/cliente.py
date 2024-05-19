from helper.create_class import create_class

cliente_field_mapping = {
    "id": {
        "db_field_name": "clie_id",
        "is_pk": True,
        "type": int,
        "validation_rules": []
    },
    "nome": {
        "db_field_name": "clie_nome",
        "type": str,
        "validation_rules": ["required"]
    },
    "sobrenome": {
        "db_field_name": "clie_sobrenome",
        "type": str,
        "validation_rules": ["required"]
    },
    "email": {
        "db_field_name": "clie_email",
        "type": str,
        "validation_rules": ["required", "email"]
    },
    "tipo": {
        "db_field_name": "clie_tipo",
        "type": str,
        "validation_rules": ["required"]
    },
    "idioma": {
        "db_field_name": "clie_idioma",
        "type": str,
        "validation_rules": ["required"]
    },
    "pais": {
        "db_field_name": "clie_pais",
        "type": str,
        "validation_rules": ["required"]
    },
    "telefone": {
        "db_field_name": "clie_telefone",
        "type": str,
        "validation_rules": ["required"]
    }
}

Cliente = create_class("Cliente", cliente_field_mapping, "cliente")