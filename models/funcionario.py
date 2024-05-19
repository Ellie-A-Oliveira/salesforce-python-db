
from helper.create_class import create_class

funcionario_field_mapping = {
    "id": {
        "db_field_name": "func_id",
        "is_pk": True,
        "type": int,
        "validation_rules": ["required"]
    },
    "nome": {
        "db_field_name": "func_nome",
        "type": str,
        "validation_rules": ["required"]
    },
    "sobrenome": {
        "db_field_name": "func_sobrenome",
        "type": str,
        "validation_rules": ["required"]
    },
    "cargo": {
        "db_field_name": "func_cargo",
        "type": str,
        "validation_rules": ["required"]
    },
    "email": {
        "db_field_name": "func_email",
        "type": str,
        "validation_rules": ["required", "email"]
    },
    "telefone": {
        "db_field_name": "func_telefone",
        "type": str,
        "validation_rules": ["required"]
    },
    "salario": {
        "db_field_name": "func_salario",
        "type": float,
        "validation_rules": ["required"]
    }
}

Funcionario = create_class("Funcionario", funcionario_field_mapping, "funcionario")