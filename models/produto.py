from helper.create_class import create_class
from helper.dateformat import dateformat

produto_field_mapping = {
    "id": {
        "db_field_name": "prod_id",
        "is_pk": True,
        "type": int,
        "validation_rules": ["required"]
    },
    "preco": {
        "db_field_name": "prod_preco",
        "type": float,
        "validation_rules": ["required"]
    },
    "status": {
        "db_field_name": "prod_status",
        "type": str,
        "validation_rules": ["required"]
    },
    "teste_gratis_ate": {
        "db_field_name": "prod_teste_gratis_ate",
        "type": dateformat,
        "validation_rules": []
    },
    "tipo_produto_id": {
        "db_field_name": "fk_tipo_produto_id_prod",
        "type": int,
        "validation_rules": ["required"],
        "foreign_key": {
            "model": "Tipo_Produto",
            "field": "id"
        }
    },
    "empresa_id": {
        "db_field_name": "fk_empresa_empresa_id",
        "type": int,
        "validation_rules": ["required"],
        "foreign_key": {
            "model": "Empresa",
            "field": "id"
        }
    }
}

Produto = create_class("Produto", produto_field_mapping, "produto")