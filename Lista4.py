#Lista4
#Exercício1
import math

class FiguraGeometrica:
    def calcularArea(self):
        pass

    def calcularPerimetro(self):
        pass

class Retangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return self.base * self.altura

    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)

    def definirBaseAltura(self, base, altura):
        self.base = base
        self.altura = altura

class Triangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcularArea(self):
        return 0.5 * self.base * self.altura

    def calcularPerimetro(self):
        print('Para calcular o perímetro do triangulo é necessário saber o tamanhos dos lados do mesmo')
        return None

    def definirBaseAltura(self, base, altura):
        self.base = base
        self.altura = altura

class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def calcularArea(self):
        return math.pi * self.raio**2

    def calcularPerimetro(self):
        return 2 * math.pi * self.raio

    def definirRaio(self, raio):
        self.raio = raio


retangulo = Retangulo(0, 0) 
triangulo = Triangulo(0, 0)
circulo = Circulo(0)

#Inserir os números que deseja saber a área e perímetro!
retangulo.definirBaseAltura(10, 5)
triangulo.definirBaseAltura(7, 3)
circulo.definirRaio(5)

print("Área e perímetro do Retângulo:")
print("A área é:", retangulo.calcularArea())
print("O perímetro é:", retangulo.calcularPerimetro())

print("\nÁrea e perímetro do Triângulo:")
print("A área é:", triangulo.calcularArea())
print("O perímetro é:", triangulo.calcularPerimetro())

print("\nÁrea e perímetro do Círculo:")
print("A área é:", circulo.calcularArea())
print("O perímetro é:", circulo.calcularPerimetro())

#Exercício2
class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def acelerar(self):
        print("Acelerando o veículo!")

    def frear(self):
        print("Freando o veículo!")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, cor):
        super().__init__(marca, modelo, ano)
        self.cor = cor

    def ligar_radio(self):
        print("Ligando o rádio do carro!")

    def abrir_porta(self):
        print("Abrindo a porta do carro!")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindrada):
        super().__init__(marca, modelo, ano)
        self.cilindrada = cilindrada

    def empinar(self):
        print("Empinando a moto!")

    def buzinar(self):
        print("Buzinando a moto!")

class Caminhao(Veiculo):
    def __init__(self, marca, modelo, ano, carga_maxima):
        super().__init__(marca, modelo, ano)
        self.carga_maxima = carga_maxima

    def carregar(self):
        print("Carregando o caminhão!")

    def descarregar(self):
        print("Descarregando o caminhão!")


carro = Carro("Toyota", "Corolla", 2023, "Prata")
moto = Moto("Harley-Davidson", "Sportster", 2022, "1200cc")
caminhao = Caminhao("Mercedes-Benz", "Actros", 2021, "20 toneladas")

print("Carro:")
carro.acelerar()
carro.frear()
carro.ligar_radio()
carro.abrir_porta()

print("\nMoto:")
moto.acelerar()
moto.frear()
moto.empinar()
moto.buzinar()

print("\nCaminhão:")
caminhao.acelerar()
caminhao.frear()
caminhao.carregar()
caminhao.descarregar()

#Exercício3

class Criptografia:
    def cifrar(self, texto):
        pass

    def decifrar(self, texto_cifrado):
        pass

class CifraCesar(Criptografia):
    def __init__(self, deslocamento):
        self.deslocamento = deslocamento

    def cifrar(self, texto):
        texto_cifrado = ""
        for char in texto:
            if char.isalpha():
                base = ord('A') if char.isupper() else ord('a')
                texto_cifrado += chr((ord(char) - base + self.deslocamento) % 26 + base)
            else:
                texto_cifrado += char
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        return self.cifrar(texto_cifrado)

class CifraXor(Criptografia):
    def __init__(self, chave):
        self.chave = chave

    def cifrar(self, texto):
        texto_cifrado = ""
        for char in texto:
            texto_cifrado += chr(ord(char) ^ self.chave)
        return texto_cifrado

    def decifrar(self, texto_cifrado):
        return self.cifrar(texto_cifrado)

cifra_cesar = CifraCesar(deslocamento=3)


cifra_xor = CifraXor(chave=5)

texto_original = "oie, me chamo gabriel!"

texto_cifrado_cesar = cifra_cesar.cifrar(texto_original)
texto_decifrado_cesar = cifra_cesar.decifrar(texto_cifrado_cesar)

texto_cifrado_xor = cifra_xor.cifrar(texto_original)
texto_decifrado_xor = cifra_xor.decifrar(texto_cifrado_xor)

print("Texto Original:", texto_original)
print("Cifrado (Cifra de César):", texto_cifrado_cesar)
print("Decifrado (Cifra de César):", texto_decifrado_cesar)
print("\nCifrado (Cifra XOR):", texto_cifrado_xor)
print("Decifrado (Cifra XOR):", texto_decifrado_xor)

