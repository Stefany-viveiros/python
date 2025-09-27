#Sistema gerenciador de nomes

nomes = []

def menu():
    print("=====Menu=====")
    print("✅ 1 - Cadastre seu nome")
    print("📝 2 - Listar nomes")
    print("❌ 3 - Sair do sistema")
    
    

while True:
    menu()
    opcao = input("Escolha sua opção: ")


    if opcao == "1":
        nome = input ("Digite seu nome: ")
    
        nomes.append(nome)
        print("Nome adicionado com sucesso!")

    elif opcao == "2":
        
        if len(nomes) == 0:
            print("Não existem nomes cadastrados")
        else:
            for podicao, nome in enumerate (nomes):
                print(f"{posicao} . {nome}")
               
            
            pos = input("Escolha o nome para deletar...")
            nomes.remove(nomes[pos])
            print("Nome especifico deletado")
    
        