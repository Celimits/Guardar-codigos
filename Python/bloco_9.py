import keyboard
'''
Bloco 9 - Orientacao a objetos: classes e objetos
Nivel sugerido: Avancado introdutorio
Foco: representar entidades usando classes, atributos, metodos e objetos que possuem estado proprio.
'''
#124
'''
class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

Raphael = pessoa('Raphael', 29)
print(Raphael.idade)
#125
Marcelo = pessoa('Marcelo', 15)
Felipe = pessoa('Felipe', 15)
print (Marcelo.nome)
print (Felipe.nome)
'''
#126
'''
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def mostrar(self):
        print(self.nome)
        print(self.idade)
Raphael = Pessoa('Raphael', 29)
Raphael.mostrar()
'''
#127
'''
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

Arroz = Produto('Arroz', 'R$25,00')
Feijão = Produto('Feijão', 'R$15,00')
Mistura = Produto('Mistura', 'R$45,00')
print(f'O {Arroz.nome} esta por {Arroz.preco}')
print(f'O {Feijão.nome} esta por {Feijão.preco}')
print(f'A {Mistura.nome} esta por {Mistura.preco}')

'''
#128
'''
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
    def aplicar_desconto(self, desconto):
        self.preco = self.preco - (self.preco * desconto/100)

Arroz = Produto('Arroz', 25)
Feijão = Produto('Feijão', 15)
Mistura = Produto('Mistura', 45)
Arroz.aplicar_desconto(20)
print(f'O {Arroz.nome} esta por {Arroz.preco}')
print(f'O {Feijão.nome} esta por {Feijão.preco}')
print(f'A {Mistura.nome} esta por {Mistura.preco}')     
'''
#129
'''
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo = self.saldo - valor
        else:
            print('Saldo insuficiente!')

Conta1 = ContaBancaria('Marcelo', 500)
Conta1.depositar(200)
Conta1.sacar(100)

print(f'Titular: {Conta1.titular}')
print(f'Saldo: R$ {Conta1.saldo}')
'''
'''
130. Aluno
Crie uma classe Aluno com nome e uma lista de notas. Implemente um metodo calcular_media() que
retorne a media do aluno.
'''
#130
'''
class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)


aluno = Aluno("Marcelo", [8, 7, 9])
print(aluno.calcular_media())
'''
#131. Situacao do aluno
'''
class Aluno:
    def __init__(self, aluno, nota):
        self.aluno = aluno
        self.nota = nota

    def situacao(self):
        if (self.nota >= 6):
            return 'Aprovado'
        else:
            return 'Reprovado'

aluno = Aluno(input('Digte o nome do aluno: '), int(input('Quantos que ele tirou? ')))

print(aluno.situacao())
'''
#132. Retangulo como objeto
'''
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
    def calcular_area(self):
        self.area = self.largura * self.altura
        return self.area
    def calcular_perimetro(self):
        self.perimetro = (self.largura * 2) + (self.altura * 2)
        return self.perimetro

largura = float(input('Digite a largura: '))
altura = float(input('Digite a altura: '))

retangulo = Retangulo(largura, altura)

print(f'Área: {retangulo.calcular_area()}')
print(f'Perímetro: {retangulo.calcular_perimetro()}')
'''
#133. Carro
#utilizei ia nessa para poder saber com utilizar a biblioteclada keybord e poder fazer o carro acelerar e freiar com o teclado apenas.
'''
class Carro:
    def __init__(self, modelo, velocidadeA=0, velocidadeM=100):
        self.modelo = modelo
        self.velocidadeA = velocidadeA
        self.velocidadeM = velocidadeM

    def acelerar(self):
        if self.velocidadeA < self.velocidadeM:
            self.velocidadeA += 1
            print("Você acelerou 1!")
            print(f'Sua velocidade atual é: {self.velocidadeA}KM/H')
        else:
            print("Velocidade máxima atingida!")

    def freiar(self):
        if self.velocidadeA > 0:
            self.velocidadeA -= 1
            print("Você freou 1!")
        else:
            print("O carro já está parado!")


carro = Carro("Fusca")

print("Pressione W para acelerar e S para frear.")
print("Pressione ESC para sair.")

while True:
    if keyboard.is_pressed("w"):
        carro.acelerar()
        keyboard.wait("w")
    elif keyboard.is_pressed("s"):
        carro.freiar()
        keyboard.wait("s")
    elif keyboard.is_pressed("esc"):
        break
'''
#134
'''
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

class Biblioteca:
    def __init__(self):
        self.livros = []

    def adicionar(self, livro):
        self.livros.append(livro)

    def listar(self):
        for livro in self.livros:
            print(livro.titulo, livro.autor, livro.disponivel)

    def emprestar(self, livro):
        livro.disponivel = False

    def devolver(self, livro):
        livro.disponivel = True

livro1 = Livro('Dom Casmurro', 'Machado de Assis')
livro2 = Livro('O Pequeno Príncipe', 'Saint-Exupéry')

biblioteca = Biblioteca()
biblioteca.adicionar(livro1)
biblioteca.adicionar(livro2)

biblioteca.listar()
biblioteca.emprestar(livro1)
biblioteca.listar()
biblioteca.devolver(livro1)
biblioteca.listar()
'''
#135
'''
class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

produtos = []

produto1 = Produto(input('Registe o produto 1: '), int(input('Registre o valor do produto 1: ')))
produto2 = Produto(input('Registe o produto 2: '), int(input('Registre o valor do produto 2: ')))
produto3 = Produto(input('Registe o produto 3: '), int(input('Registre o valor do produto 3: ')))

produtos = produtos + [produto1, produto2, produto3]

print('Produtos cadastrados:')
for produto in produtos:
    print(produto.nome, produto.preco)

busca = input('Digite o nome do produto que deseja buscar: ')

for produto in produtos:
    if produto.nome == busca:
        print(produto.nome, produto.preco)

total = 0
for produto in produtos:
    total = total + produto.preco

print(f'Valor total: R$ {total}')
'''