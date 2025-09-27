print("Bem vindo ao sistema")
print("Digite se você é maior de idade")
valor =  float(input("Digite 1 para maior 0 para menor: "))

if valor == 1:
    print("Você é maior de idade")
elif valor == 0:
    print("Você é menor de idade")
else:
    print("É uma opção inválida")
