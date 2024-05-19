from helper.create_class import create_class

tipo_plano_field_mapping = {
    "id": {
        "db_field_name": "tipo_plano_id",
        "is_pk": True,
        "type": int,
        "validation_rules": ["required"]
    },
    "nome": {
        "db_field_name": "tipo_plano_nome",
        "type": str,
        "validation_rules": ["required"]
    },
    "descricao": {
        "db_field_name": "tipo_plano_desc",
        "type": str,
        "validation_rules": ["required"]
    },
    "preco": {
        "db_field_name": "tipo_plano_preco",
        "type": float,
        "validation_rules": ["required"]
    },
    "tipo_preco": {
        "db_field_name": "tipo_plano_preco",
        "type": str,
        "validation_rules": ["required"]
    },
    "nivel_plano": {
        "db_field_name": "tipo_plano_nivel_plano",
        "type": str,
        "validation_rules": ["required"]
    },
    "teste_gratis_disponivel": {
        "db_field_name": "tipo_plano_teste_gratis_disponivel",
        "type": bool,
        "validation_rules": ["required"]
    }
}

Tipo_Plano = create_class("Tipo_Plano", tipo_plano_field_mapping, "tipo_plano")