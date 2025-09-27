
class ContaBancaria:

    def __init__(self, saldo):
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
            return True
        else:
            return False

    def get_saldo(self):
        return self.saldo

contaStefany = ContaBancaria(500)

contaStefany.sacar(50)
contaStefany.depositar(100)

print(contaStefany.get_saldo())