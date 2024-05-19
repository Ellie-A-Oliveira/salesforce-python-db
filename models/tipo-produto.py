from helper.create_class import create_class

tipo_produto_field_mapping = {
    "id": {
        "db_field_name": "tipo_prod_id",
        "is_pk": True,
        "type": int,
        "validation_rules": ["required"]
    },
    "nome": {
        "db_field_name": "tipo_prod_nome",
        "type": str,
        "validation_rules": ["required"]
    },
    "desc": {
        "db_field_name": "tipo_prod_desc",
        "type": str,
        "validation_rules": ["required"]
    },
    "prod_add_on": {
        "db_field_name": "tipo_prod_prod_add_on",
        "type": str,
        "validation_rules": ["required", "in:0,1"]
    },
    "nome_grupo": {
        "db_field_name": "tipo_prod_nome_grupo",
        "type": str,
        "validation_rules": ["required"]
    }
}

Tipo_Produto = create_class("Tipo_Produto", tipo_produto_field_mapping, "tipo_produto")