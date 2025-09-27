
class Carro:

    #configuração inicial do objeto
    def __init__(self, nome, cor, modelo, ano, marca):
        #definir atributo
        self.nome = nome
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca

    def correr(self):
        print("Correndo muito........")

    def frear(self):
        print("Freiando.........pastilha esta ruim........")

    def ligar(self):
        print("ligando o carro.......", self.nome)

passatiCarro = Carro("Passati", "Preto", "v1", "2025", "BMW")
passatiCarro.ligar()

passatiCarro.correr()
passatiCarro.frear()
