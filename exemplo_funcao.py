nomes = []

def menu():
    print("=====Menu=====")
    print("✅ 1 - Cadastre seu nome")
    print("📝 2 - Listar nomes")
    print("❌ 3 - Sair do sistema")
    
    opcao = input("Escolha sua opção: ")

while True:
    menu()


    if opcao == "1":
        nomes = input ("Digite seu nome: ")
    
        nomes.append(nome)
        print("Nome adicionado com sucesso!")

         elif opcao == "2":
        #len - length de tamanho
        if len(nomes) == 0:
            print("Não existem nomes cadastrados")
        else:
            for nome in nomes:
                print(nome)
        
    elif opcao == "9":
        print("Saindo do Sistema")
        break
    else:
        print("Opção inexistente, tente novamente...")