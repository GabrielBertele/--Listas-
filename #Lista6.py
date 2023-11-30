#Lista6
#Exercício1
class UnidadeMilitar:
    def mover(self):
        pass

    def atacar(self):
        pass

class Soldado(UnidadeMilitar):
    def mover(self):
        print("Soldado marchando em formação.")

    def atacar(self):
        print("Soldado atacando com sua espada enferrujada.")

class Arqueiro(UnidadeMilitar):
    def mover(self):
        print("Arqueiro se movendo furtivamente pelas sombras.")

    def atacar(self):
        print("Arqueiro disparando flechas de seu arco mágico.")

class Cavaleiro(UnidadeMilitar):
    def mover(self):
        print("Cavaleiro galopando com sua armadura reluzente.")

    def atacar(self):
        print("Cavaleiro investindo com sua lança de cavalaria.")

soldado1 = Soldado()
arqueiro1 = Arqueiro()
cavaleiro1 = Cavaleiro()

# Adicionando as unidades
unidades = [soldado1, arqueiro1, cavaleiro1]

for unidade in unidades:
    unidade.mover()
    unidade.atacar()
    print("\n")
#Exercício2
class Assinatura:
    def calcular_preco(self):
        pass

    def exibir_detalhes(self):
        pass


class AssinaturaSimples(Assinatura):
    def calcular_preco(self):
        return 29.99

    def exibir_detalhes(self):
        print("Assinatura Simples - Acesso a filmes e séries em qualidade padrão, 1080p.")


class AssinaturaPremium(Assinatura):
    def calcular_preco(self):
        return 49.99

    def exibir_detalhes(self):
        print("Assinatura Premium - Com a assinatura premium você têm acesso a todos filmes e séries no catálogo com a definição máxima, 4k.")


assinatura_simples = AssinaturaSimples()
assinatura_premium = AssinaturaPremium()

assinaturas = [assinatura_simples, assinatura_premium]

for assinatura in assinaturas:
    print(f"Tipo de Assinatura: {type(assinatura).__name__}")
    print(f"Preço: R$ {assinatura.calcular_preco():.2f}")
    assinatura.exibir_detalhes()
    print("\n")