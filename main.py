from controller.cliente_controller import cliente_controller


def exibir_menu():
    print("==MENU==")
    print("1 - Cadastrar Cliente")
    print("2 - Listar Cliente")
    print("3 - Sair do Sistema")

def main():
    clienteController = cliente_controller()

    while True:
        exibir_menu()
        opc = input("Escolha uma opção: ")

        if opc == "1":
            nome = input("Digite o nome: ")
            email = input("Digite seu email: ")
            idade = int(input("Digite a idade: "))
            #Salvar no Banco de dados
            clienteController.criar_cliente(nome, email, idade)

        elif opc == "2":
            #listar clientes do banco
            clientes = clienteController.listar_cliente()

            for index, cliente in enumerate(clientes, 1):
                print(f'{index}, {cliente}')

        elif opc == "3":
            print("Saindo do Sistema")
            break

        else:
            print("Opção Inválida")

if __name__ == "__main__":
    main()