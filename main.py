import importlib

from models.cliente import Cliente
from models.empresa import Empresa
from models.funcionario import Funcionario
perguntas_frequentes = importlib.import_module("models.pergunta-frequente")
Pergunta_Frequente = perguntas_frequentes.Pergunta_Frequente
from models.produto import Produto
from models.recurso import Recurso
tipo_plano = importlib.import_module("models.tipo-plano")
Tipo_Plano = tipo_plano.Tipo_Plano
tipo_produto = importlib.import_module("models.tipo-produto")
Tipo_Produto = tipo_produto.Tipo_Produto

from helper.safe_input import safe_input
from helper.should_continue import should_continue
from helper.create_crud import gerar_crud

from db.database import connect

all_models = [
    Cliente,
    Empresa,
    Funcionario,
    Pergunta_Frequente,
    Produto,
    Recurso,
    Tipo_Plano,
    Tipo_Produto,
]


def listar_crud(tipo_crud):
    print(f"Bem-vindo ao CRUD para {tipo_crud.name}!")
    _continue = 1
    while _continue == 1:
        print("Opções:\n1-LISTAR\n2-LISTAR UM\n3-CRIAR\n4-ATUALIZAR UM\n5-REMOVER UM\n0-SAIR\n")
        opcao = safe_input("Digite a opção que deseja: ", int)

        match opcao:
            case 1:
                dados = tipo_crud.listar()
                for dado in dados:
                    print(dado)
            case 2:
                identificador = safe_input("Digite o identificador: ", int)
                dado = tipo_crud.listar_pelo_identificador(identificador)
                print(dado)
            case 3:
                new_instance = {}
                for key, value in tipo_crud.field_mapping.items():
                    if "is_pk" in value and value["is_pk"]:
                        continue
                    
                    new_instance[key] = (
                        safe_input(
                            f"Digite o campo {key} do modelo {tipo_crud.name}: ",
                            value["type"]
                        )
                    )

                tipo_crud.criar(new_instance)
            case 4:
                identificador = safe_input("Digite o identificador: ", int)
                new_instance = {}
                for key, value in tipo_crud.field_mapping.items():
                    if "is_pk" in value and value["is_pk"]:
                        continue
                    
                    new_instance[key] = (
                        safe_input(
                            f"Digite o campo {key} do modelo {tipo_crud.name}: ",
                            value["type"]
                        )
                    )
                tipo_crud.atualizar_pelo_identificador(identificador, new_instance)
            case 5:
                identificador = safe_input("Digite o identificador: ", int)
                tipo_crud.remover_pelo_identificador(identificador)
            case 0:
                break
            case _:
                print("Opção inválida!")

        _continue = should_continue()


def main():
    has_connection, db_inst, conn = connect()
    if not has_connection:
        raise Exception("Falha na conexão com o banco de dados!")
    
    cruds = [crud for crud in list(map(lambda model: gerar_crud(model, db_inst, conn), all_models))]

    print("Bem-vindo ao programa de CRUDs!")

    _continue = 1
    while _continue == 1:
        for i in range(len(cruds)):
            crud = cruds[i]
            numero_opcao = i + 1
            print(f"{numero_opcao}-{crud.name}")

        opcao = safe_input("\nDigite o CRUD desejado: ", int)
        idx_crud_selecionado = next(
            filter(
                lambda idx_campo: idx_campo == opcao - 1,
                range(len(cruds))
            ),
            None
        )

        if idx_crud_selecionado is not None:
            crud = cruds[idx_crud_selecionado]
            listar_crud(crud)
        else:
            print("Opção inválida!")

        _continue = should_continue("Deseja continuar no programa de CRUD?")


if __name__ == '__main__':
    main()
