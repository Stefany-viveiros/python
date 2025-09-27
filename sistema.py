from models.Pessoa import Pessoa

def menu():
    print("✅====MENU=====✅")
    print("1 - 📝 Criar Pessoa")
    print("2 - 📒 Listar Pessoas")
    print("3 - ❌ Limpar Lista")
    print("4 - 🔴 Sair do Sistema")



def inciarSistema():
    print("Sistema iniciado")
    pessoas = [] #criar lista de pessoas

    while(True):
        menu()
        opcao = input("Selecione uma opção...........")
        if opcao == "1":
            nome = input("Digite o nome da pessoa.....")
            email = input("Digite o email da pessoa......")
            pessoa = Pessoa(nome, email)
            pessoas.append(pessoa) #Adicionar pessoa a lista de pessoas
        elif opcao == "2":
            for pessoa in pessoas:
                print(pessoa)
                print(f'Nome: {pessoa.get_nome()}, Email: {pessoa.get_email()}')

#Lógica para inicar automaticamente
if __name__ == "__main__":
    inciarSistema()