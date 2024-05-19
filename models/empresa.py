from helper.create_class import create_class

empresa_field_mapping = {
    "id": {
        "db_field_name": "empresa_id",
        "is_pk": True,
        "type": int,
        "validation_rules": ["required"]
    },
    "nome": {
        "db_field_name": "empresa_nome",
        "type": str,
        "validation_rules": ["required"]
    },
    "tipo_industria": {
        "db_field_name": "empresa_tipo_industria",
        "type": str,
        "validation_rules": ["required"]
    },
    "tamanho": {
        "db_field_name": "empresa_tamanho",
        "type": str,
        "validation_rules": ["required"]
    },
    "pais_sede": {
        "db_field_name": "empresa_pais_sede",
        "type": str,
        "validation_rules": ["required"]
    },
    "cliente_id": {
        "db_field_name": "fk_cliente_id",
        "type": int,
        "validation_rules": ["required"],
        "foreign_key": {
            "model": "Cliente",
            "field": "id"
        }
    }
}

Empresa = create_class("Empresa", empresa_field_mapping, "empresa")