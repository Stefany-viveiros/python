print("💵 Bem vindo ao Banco Girabonk 🏦")
saldo = float(input("Digite seu saldo....R$"))

transferencia = float(input("Qual o valor da transferência? R$"))


if saldo >= transferencia:
    print("Saldo suficiente✅")

    saldo = saldo - transferencia
    print("Seu saldo atual é de R$", saldo)
else:
    print("saldo insuficiente❌")


#Validar se ela possui saldo suficiente para a transferência