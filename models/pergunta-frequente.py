# based on the other models, generate using db table below
# CREATE TABLE PERGUNTAS_FREQUENTES (perg_id number(5) generated AS IDENTITY not null ,perg_perguntas varchar(90) not null,perg_respostas varchar(90) not null,FK_TIPO_PRODUTO_id_perg number(5)constraint FK_TIPO_PRODUTO_id_perg_fk references tipo_produto not null

from helper.create_class import create_class

pergunta_frequente_field_mapping = {
    "id": {
        "db_field_name": "perg_id",
        "is_pk": True,
        "type": int,
        "validation_rules": ["required"]
    },
    "pergunta": {
        "db_field_name": "perg_perguntas",
        "type": str,
        "validation_rules": ["required"]
    },
    "resposta": {
        "db_field_name": "perg_respostas",
        "type": str,
        "validation_rules": ["required"]
    },
    "tipo_produto_id": {
        "db_field_name": "fk_tipo_produto_id_perg",
        "type": int,
        "validation_rules": ["required"]
    }
}

Pergunta_Frequente = create_class("Pergunta_Frequente", pergunta_frequente_field_mapping, "perguntas_frequentes")