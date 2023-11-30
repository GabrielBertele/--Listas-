#Lista8
#Exercício1
import random
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def exibirDescricao(self):
        print(f"Este é um animal chamado {self.nome}")

class Carnivoro(Animal):
    def caçar(self):
        print(f"{self.nome} está caçando!")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("É um animal carnívoro")

class Herbivoro(Animal):
    def pastar(self):
        print(f"{self.nome} está pastando!")

    def exibirDescricao(self):
        super().exibirDescricao()
        print("É um animal herbívoro")

class Onivoro(Carnivoro, Herbivoro):
    def comer(self):
        escolha = random.randint(0, 1)
        if escolha == 0:
            self.caçar()
        else:
            self.pastar()

    def exibirDescricao(self):
        super().exibirDescricao()
        print("É um animal onívoro")

# Exemplo de uso:

animal_carnivoro = Carnivoro("Leão")
animal_carnivoro.exibirDescricao()
animal_carnivoro.caçar()

print('\n')

animal_herbivoro = Herbivoro("Cavalo")
animal_herbivoro.exibirDescricao()
animal_herbivoro.pastar()

print('\n')

animal_onivoro = Onivoro("Urso")
animal_onivoro.exibirDescricao()
animal_onivoro.comer()
