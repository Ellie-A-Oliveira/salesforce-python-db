from helper.safe_input import safe_input
from helper.should_continue import should_continue
from db.database import select, update, insert, delete

class Crud:
    def __init__(self, model, db_inst, conn):
        identifiers = []
        
        for key, value in model.field_mapping.items():
            if "is_pk" in value and value["is_pk"]:
                identifiers.append(key)

        if len(identifiers) == 0:
            raise Exception("Um campo identificador deve existir nos campos!")
        elif len(identifiers) > 1:
            raise Exception("Apenas um campo identificador pode ser declarado nos campos!")
        else:
            pk = identifiers[0]
            self.pk = model.field_mapping[pk]["db_field_name"]
            
        self.table_name = model.db_table_name
        self.field_mapping = model.field_mapping
        self.name = model.__name__
        self.db_inst = db_inst
        self.model = model
        self.conn = conn
    

    def criar(self, new_instance):
        try:
            instance = self.model.create_from_dict(new_instance)
            mapped_instance = instance.map_to_db()
            return insert(
                self.conn,
                self.db_inst,
                self.table_name,
                ", ".join(mapped_instance.keys()),
                ", ".join([f"'{value}'" for value in mapped_instance.values()]),
            )
        except Exception as e:
            print(e)
    
    def listar(self):
        return select(self.db_inst, self.table_name, "*")

    def listar_pelo_identificador(self, identificador):
        return select(self.db_inst, self.table_name, "*", f"{self.pk} = '{identificador}'")

    def atualizar_pelo_identificador(self, identificador, new_instance):
        instance = self.model.create_from_dict(new_instance)
        mapped_instance = instance.map_to_db()
        return update(self.conn, self.db_inst, self.table_name, mapped_instance, f"{self.pk} = '{identificador}'")

    def remover_pelo_identificador(self, identificador):
        return delete(self.conn, self.db_inst, self.table_name, f"{self.pk} = '{identificador}'")


def gerar_crud(model, db_inst, conn):
    return Crud(model, db_inst, conn)
