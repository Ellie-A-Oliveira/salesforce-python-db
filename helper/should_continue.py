from helper.safe_input import safe_input

def should_continue(message: str = "Deseja continuar?") -> bool:
    _continue = True
    while _continue == True:
        opcao = safe_input(message + " (1-SIM;0-NÃO) ", int)

        if opcao != 1 and opcao != 0:
            print("Número digitado inválido!")
        else:
            return opcao == 1
