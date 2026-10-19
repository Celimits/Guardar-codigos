'''
print ('Hello wrold!')

'''

'''
nome = str(input("Escreva seu nome: "))
idade = int(input("Escreva sua idade: "))
cidade = str(input("Escreva sua cidade: "))
print ('Seu nome é ', nome, ', tem ' , idade, 'anos' , 'e mora em ' , cidade)
'''
'''
usuario = str(input('Escreva seu usuario: '))
print ('Olá' , usuario , '!')
'''
'''
soma1 = int(input('Digite o primeiro valor '))
soma2 = int(input('Digite o segundo valor '))
total = soma1 + soma2
print('O valor da soma é:' , total)
'''
'''
valor1 = int(input('Digite o primeiro valor '))
valor2 = int(input('Digite o segundo valor '))
soma = valor1 + valor2
sub = valor1 - valor2
mult = valor1 * valor2
divisao = valor1 / valor2
print('')
print('O valor da soma é:' , soma)
print('O valor da subtração é:' , sub)
print('O valor da multiplicação é:' , mult)
print('O valor da divisão é:' , divisao)
'''
'''
dobro = int(input('Digite o valor que dejesa o dobro: '))
dobrov = dobro * 2
print ('O valor é' , dobro , 'e o dobro é' , dobrov)
'''
'''
value = int(input('Digite o valor que dejesa o triplo e a metade: '))
triplo = value * 3
metade = value / 2
print ('O valor é' , value , 'e o triplo é' , triplo , 'e a metade é' , metade)
'''

# ---------------- Exercícios 9 a 15 ----------------

# 9 - Nome completo
'''
primeiro = str(input('Digite seu primeiro nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
completo = primeiro + ' ' + sobrenome
print('Seu nome completo é:' , completo)
'''

# 10 - Ano de nascimento
'''
nascimento = int(input('Digite seu ano de nascimento: '))
idade = 2026 - nascimento
print('Você tem aproximadamente' , idade , 'anos')
'''

# 11 - Conversão de metros
'''
metros = float(input('Digite a medida em metros: '))
cm = metros * 100
mm = metros * 1000
print(metros , 'metros são' , cm , 'centímetros e' , mm , 'milímetros')
'''

# 12 - Minutos para segundos
'''
minutos = int(input('Digite a quantidade de minutos: '))
segundos = minutos * 60
print(minutos , 'minutos são' , segundos , 'segundos')
'''

# 13 - Horas para minutos
'''
horas = int(input('Digite a quantidade de horas: '))
minutos = horas * 60
print(horas , 'horas são' , minutos , 'minutos')
'''

# 14 - Temperatura
'''
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = celsius * 9 / 5 + 32
print(celsius , 'graus Celsius são' , fahrenheit , 'graus Fahrenheit')
'''

# 15 - Conversão de moeda
'''
reais = float(input('Digite o valor em reais: '))
cotacao = 5.00
dolares = reais / cotacao
print('Com' , reais , 'reais você compra' , dolares , 'dólares')
'''

# ---------------- Exercícios 16 a 30 ----------------

# 16 - Área do quadrado
'''
lado = float(input('Digite o tamanho do lado do quadrado: '))
area = lado * lado
print('A área do quadrado é:' , area)
'''

# 17 - Área do retângulo
'''
largura = float(input('Digite a largura do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))
area = largura * altura
print('A área do retângulo é:' , area)
'''

# 18 - Área do triângulo
'''
base = float(input('Digite a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))
area = (base * altura) / 2
print('A área do triângulo é:' , area)
'''

# 19 - Área do círculo
'''
raio = float(input('Digite o raio do círculo: '))
pi = 3.14
area = pi * raio ** 2
print('A área do círculo é:' , area)
'''

# 20 - Perímetro do retângulo
'''
largura = float(input('Digite a largura do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))
perimetro = 2 * (largura + altura)
print('O perímetro do retângulo é:' , perimetro)
'''

# 21 - Média de três notas
'''
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
print('A média é:' , f'{media:.2f}')
'''

# 22 - Salário por hora
'''
valorhora = float(input('Digite o valor recebido por hora: '))
horas = int(input('Digite o número de horas trabalhadas no mês: '))
salario = valorhora * horas
print('O salário bruto é:' , salario)
'''

# 23 - Aumento salarial
'''
salario = float(input('Digite o salário: '))
aumento = salario * 0.10
novosalario = salario + aumento
print('Salário original:' , salario)
print('Valor do aumento:' , aumento)
print('Novo salário:' , novosalario)
'''

# 24 - Desconto
'''
preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.15
precofinal = preco - desconto
print('Valor do desconto:' , desconto)
print('Preço final:' , precofinal)
'''

# 25 - Parcelamento
'''
total = float(input('Digite o valor total da compra: '))
parcelas = int(input('Digite a quantidade de parcelas: '))
valorparcela = total / parcelas
print('Cada parcela será de:' , valorparcela)
'''

# 26 - IMC
'''
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** 2
print('Seu IMC é:' , f'{imc:.2f}')
'''

# 27 - Média ponderada
'''
nota1 = float(input('Digite a primeira nota (peso 2): '))
nota2 = float(input('Digite a segunda nota (peso 3): '))
media = (nota1 * 2 + nota2 * 3) / 5
print('A média ponderada é:' , media)
'''

# 28 - Resto da divisão
'''
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
quociente = valor1 // valor2
resto = valor1 % valor2
print('O quociente é:' , quociente)
print('O resto é:' , resto)
'''

# 29 - Antecessor e sucessor
'''
numero = int(input('Digite um número inteiro: '))
antecessor = numero - 1
sucessor = numero + 1
print('O antecessor é:' , antecessor , 'e o sucessor é:' , sucessor)
'''

# 30 - Potência
'''
base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))
resultado = base ** expoente
print(base , 'elevado a' , expoente , 'é:' , resultado)
'''

# 31 - Positivo e negativo
'''
valor = int(input(('Digite um valor: ')))
if (valor > 0):
    print('É um valor positivo')
elif (valor == 0):
    print('É igual a 0')
else: print('É um valor negativo')
'''

# 32 - Maior de idade
'''
valori = int(input(('Digite a sua idade: ')))
if (valori >= 18):
    print('Tu é maior de idade bixão, vai aproveitar o resto da sua vida!')
else: print('Tu é menor de idade mlk, vai fazer merda enquanto pode!')
'''

# 33 - Par ou impar
'''
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
'''

#34 - Maior entre dois numeros
'''
numberone = int(input("Digite um número para comparar: "))
numbertwo = int(input("Digite o segundo número para comparar: "))
if(numberone > numbertwo):
    print('O número' , numberone , 'é maior que' , numbertwo)
elif(numbertwo == numberone):
    print('O número' , numberone , 'é igual ao' , numbertwo)
else:print('O número' , numberone , 'é menor que' , numbertwo)
'''
'''
#35

number1 = int(input("Digite um número para comparar: "))
number2 = int(input("Digite o segundo número para comparar: "))
number3 = int(input("Digite o segundo número para comparar: "))
if(number1 > number2 and number1 > number3):
    print('O número' , number1 , 'é maior que' , number2 , 'e' , number3)
elif(number2 > number1 and number2 > number3):
    print('O número' , number2 , 'é maior que o' , number1 , 'e' , number3)
else:print('O número' , number3 , 'é maior que' , number2 , 'e' , number1)

#37. Aprovacao

nota = float(input('Qual a sua nota? '))
if (nota >= 6):
    print('Você esta aprovado!')
else: print('Você esta reprovado')

#38. Aprovado, recuperacao ou reprovado

notaf = float(input('Qual a sua nota final? '))
if (notaf >= 7):
    print('Você esta aprovado!')
elif (notaf >= 5 and notaf > 7):
    print('Você esta de recperação')
else: print('Você esta reprovado')

#39. Faixa etaria

faixaetaria = int(input('Qual é a sua idade para informar sua faixa etaria? '))
if(faixaetaria > 0 and faixaetaria <= 11):
    print('Você ainda é uma criança que farma aura 67 vezes!')
elif(faixaetaria >= 12 and faixaetaria <= 18):
    print('Você ja está na adolescencia, melhor fase da vida')
elif (faixaetaria >= 18 and faixaetaria <= 59):
    print('Você ja esta na vda adulta, vai tirar a carteira e conquistar as suas coisinhas no caminho certo!')
elif (faixaetaria <= 0):
    print ('Error 404, verifique a sua idade')
else: print('Você ja esta idoso, aproveite seu finalzinho!')

#40. Senha simples

for tentativa in range(3):
    senha = input('Qual é a senha? ')
    if (senha == 'admin'):
        print('Acesso liberado!')
        print('Seja bem vindo!!')
        break
    else:
        print('Acesso negado :(')
        print('Tentativas restantes:', 2 - tentativa)

#41. Login simples
for tentativas in range(3):
    user = input('Qual é o user? ')
    senha = input('Qual é a senha? ')
    if (user == 'admin' and senha == 'admin'):
        print('Acesso liberado!')
        print('Seja bem vindo!!')
        break
    else:
        print('Acesso negado :(')
        print('Tentativas restantes:', 2 - tentativas)

#42. Multiplo de 5 
numerode5 = int(input('Digite um número inteiro: '))

if numerode5 % 5 == 0:
    print('É múltiplo de 5')
else:
    print('Não é múltiplo de 5')
#43. Divisivel por 3 e 5
numero = int(input('Digite um número: '))

if numero % 3 == 0 and numero % 5 == 0:
    print('É divisível por 3 e 5')
else:
    print('Não é divisível por 3 e 5')
#44. Ano bissexto
ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    print('Ano bissexto')
else:
    print('Não é ano bissexto')

#45. Desconto
valor = float(input('Digite o valor da compra: R$ '))

if valor >= 200:
    valor = valor * 0.90

print('Valor final: R$', valor)

#46. Frete
valor = float(input('Digite o valor da compra: R$ '))

if valor >= 150:
    total = valor
else:
    total = valor + 20

print('Total final: R$', total)

#47. 47. Calculadora com escolha
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação (+, -, * ou /): ')

if operacao == '+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    if num2 == 0:
        print('Não é possível dividir por zero!')
    else:
        print(num1 / num2)
else:
    print('Operação inválida!')
#48. Triangulo possivel
lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if (lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2):
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')
'''
#
'''
a = float(input("Digite o lado A: "))
b = float(input("Digite o lado B: "))
c = float(input("Digite o lado C: "))

# Verifica se os lados formam um triângulo
if(a < b + c and b < a + c and c < a + b):
    if a == b == c:
        print("Triângulo Equilátero (todos os lados iguais).")
    elif a == b or a == c or b == c:
        print("Triângulo Isósceles (dois lados iguais).")
    else:
        print("Triângulo Escaleno (todos os lados diferentes).")
else:
    print("Os lados informados não formam um triângulo.")

#50
salario = float(input("Digite o salário: R$ "))

if (salario <= 2000):
    aliquota = 0.0
elif salario <= 4000:
    aliquota = 0.10
else:
    aliquota = 0.20

imposto = salario * aliquota
salario_liquido = salario - imposto

print(f"Valor do imposto: R$ {imposto:.2f}")
print(f"Salário restante: R$ {salario_liquido:.2f}")
'''
#51
'''
numero = 0
for numero in range (0,10):
    print (numero + 1)
'''

#52
'''for contagem in range (10, -1, -1):
    print(contagem)
print('Fim')'''

#53
'''
for par in range (0, 101, +2):
    print (par)
'''
#54
'''
for impar in range (1, 100, +2):
    print (impar)
'''
#55
'''
tabuada = int(input('Digite um numero para saber a tabuada dele: '))
for multiplicação in range (11):
    resultado = tabuada * multiplicação
    print(f'{tabuada} x {multiplicação} = {resultado}')
'''
#56
'''
soma = 0
n = int(input('Digite um valor: '))
for i in range(n+1):
    soma = soma + i

print(soma)
'''
#57
'''
fat = int(input('Digite um valor: '))
multiplicação = 1

while (fat < 0):
    print('Apenas numeros positivos')
    fat = int(input('Digite um numero positivo'))
for i in range(1, fat + 1):
    multiplicação = i * multiplicação
print(multiplicação)
'''
#58
'''
pares = 0
for i in range (1, 11):
    n1 = int(input('Digite um numero: '))
    if(n1 % 2 == 0):
        pares = pares + 1
print(f'Tem {pares} numeros pares')
'''
#59
'''
positivo = 0
for i in range (1,11)
    n1 = int(input('Digite um numero: '))
    if(n1 > 0):
        positivo = positivo + n1
print(f'A soma de todos é {positivo}')
'''
#60
'''
maior = int(input('Digite um valor: '))

for repet in range (4):
    n = int(input('Digite outro numero: '))
    if (n > maior):
print (f'o maior numero digitado foi {n}')
'''
#61
'''
menor = 1

for repet in range (5):
    n = int(input('Digite outro numero: '))
    if (n < menor):
        menor = n
print(f'o menor numero digitado foi {menor}')
'''
#62
'''
soma = 0

for i in range(5):
    nota = float(input('Digite uma nota: '))
    soma = soma + nota

media = soma / 5

print(f'A média das notas é {media}')

'''
#63
'''
senha_correta = '1234'
senha = ''

while (senha != senha_correta):
    senha = input('Digite a senha: ')

print('Acesso permitido')
'''
#64
'''
n = int(input('Digite um numero positivo: '))

while (n <= 0):
    n = int(input('Digite outro numero positivo: '))

print(f'O numero digitado foi {n}')
'''
#65
'''
opcao = 1

while (opcao != 0):
    print('1 - Dizer ola')
    print('2 - Mostrar uma mensagem')
    print('0 - Sair')

    opcao = int(input('Digite uma opcao: '))

    if (opcao == 1):
        print('Ola!')
    elif (opcao == 2):
        print('Essa é uma mensagem')
    elif (opcao == 0):
        print('Fim')
'''
#66
'''
soma = 0
n = int(input('Digite um numero: '))

while (n != 0):
    soma = soma + n
    n = int(input('Digite outro numero: '))

print(f'A soma é {soma}')
'''
#67
'''
soma = 0
quantidade = 0

nota = float(input('Digite uma nota: '))

while (nota != -1):
    soma = soma + nota
    quantidade = quantidade + 1
    nota = float(input('Digite outra nota: '))

if (quantidade > 0):
    media = soma / quantidade
    print(f'Quantidade de notas: {quantidade}')
    print(f'Media: {media}')
else:
    print('Nenhuma nota foi digitada')
'''
#68
'''
secreto = 50
palpite = int(input('Digite um palpite: '))

while (palpite != secreto):
    if (palpite > secreto):
        print('O numero é menor')
    else:
        print('O numero é maior')

    palpite = int(input('Digite outro palpite: '))

print('Acertou!')
'''
#69
'''
n = int(input('Digite um numero maior que 1: '))
divisores = 0

for i in range(1, n + 1):
    if (n % i == 0):
        divisores = divisores + 1

if (divisores == 2):
    print('O numero é primo')
else:
    print('O numero não é primo')
'''
#70
'''
inicio = int(input('Digite o primeiro numero: '))
fim = int(input('Digite o segundo numero: '))

for n in range(inicio, fim + 1):
    divisores = 0

    for i in range(1, n + 1):
        if (n % i == 0):
            divisores = divisores + 1

    if (divisores == 2):
        print(n)
'''
#71
'''
quantidade = str(input('Qual a sua palavra que deseja saber o comprimento? '))
print(len(quantidade))
'''
#72
'''
maiuscula = str(input('Qual a sua palavra que deseja ver maiuscula: '))
mai = maiuscula.upper()
min = maiuscula.lower()
print(f'Maiusculo fica: {mai}')
print(f'Minusculo fica: {min}')
'''
#73
'''
yourtext = str(input('Qual a sua palavra que deseja? '))
print(f'A ultima letra de {yourtext} é: {yourtext[len(yourtext)-1]}')
print(f'A primeira letra de {yourtext} é: {yourtext[0]}')
'''
#74
'''
palavra = str(input('Digite a sua palavra e te digo quantas vezes a letra "A" aparece: '))
total = palavra.lower().count("a")
print(f'A letra "A" aparece {total} vezes na palavra {palavra}.')
'''
#75
'''
palavra = input("Digite uma palavra: ")
palavra_limpa = palavra.strip().lower()
palavra_invertida = palavra_limpa[::-1]
if palavra_limpa == palavra_invertida:
    print(f'A palavra "{palavra}" é um palíndromo!')
else:
    print(f'A palavra "{palavra}" não é um palíndromo.')
'''
#76
'''
texto = input("Digite uma palavra ou frase: ")
invertido = ""
for i in range(len(texto) - 1, -1, -1):
    invertido += texto[i]
print(invertido)
'''
#77
'''
nome = input("Digite uma frase")
print(nome.split('o'))
'''
#78
'''
frase = input('Digite uma frase: ')
palavras = frase.split()
quantidade = (len(palavras)-1)
print(f'A palavra {frase} contêm {quantidade} espaços')
'''
#79
'''
nome = input('Digite uma frase: ')
palavra = input('Digite a palavra que você quer alterar: ')
alternativa = input('Digite a nova palavra: ')
nome = nome.replace(palavra, alternativa)
print(f'A frase foi alterada com sucesso.')
print(f'A palavra {palavra} foi alterada para {alternativa}.')
print(f'Nova frase: {nome}')
'''
#80
'''
email = input("Digite o seu email: ")
verificação = email.split('@')

if ('.' in verificação):
    print('Você passou na verificação')
else: print('Você não passou na verificação')
'''
#81
'''
lista1 = ['Marcelo', 'Victor', 'Azambuja', 'Zei']
for i in (lista1):
    print(i)
'''
#82.
'''
lista = []
for i in range(0, 5, + 1):
    lista.append(input('Digite um nome: '))
print(lista)
'''
#83. 
'''
lista = []
for i in range(0, 5, 1):
    lista.append(int(input('Digite um numero: ')))
soma = 0
for numero in lista:
    soma += numero
print(lista)
print('Soma:', soma)
'''

#84
'''
lista = []

for i in range(0, 5, 1):
    lista.append(int(input('Digite um numero: ')))

maior = lista[0]

for numero in (lista):
    if (numero > maior):
        maior = numero

print(lista)
print('Maior:', maior)
'''
#85
'''
lista = []

for i in range(0, 5, 1):
    lista.append(int(input('Digite um numero: ')))

menor = lista[0]

for numero in lista:
    if (numero < menor):
        menor = numero

print(lista)
print('Menor:', menor)
'''
#86
'''
lista = []

for i in range(0, 5, 1):
    lista.append(float(input('Digite uma nota: ')))
soma = 0

for nota in lista:
    soma += nota

media = soma / 5

print(lista)
print('Media:', media)
'''
#87
'''
lista = []
listadepares = []
for i in range(10):
    numero = int(input('Digite 10 numeros'))
    if numero % 2 == 0:
        listadepares.append(numero)
else:
    print('Não tem numeros pares')
print(f'Numeros pares: {listadepares}')
'''
#88
'''
listanomes = ['Victor', 'marcelo', 'Raphael']
print(listanomes)
for i in range(3):
    remover = input('Escolha um nome para remover: ')
    if (remover in listanomes):
        listanomes.remove(remover)
        print(listanomes)
    else:
        print('Este nome não existe')
'''
#89
'''
produtos = []

for i in range(5):
    produto = input("Digite um produto: ")
    produtos.append(produto)

busca = input("Digite o produto que deseja buscar: ")

if (busca in produtos):
    print("Produto cadastrado.")
else:
    print("Produto não cadastrado.")
'''
#90
'''
numeros = []

for i in range(6):
    numero = int(input("Digite um número: "))
    numeros.append(numero)

numeros.sort()

print("Ordem crescente:", numeros)
print("Ordem decrescente:", numeros[::-1])
'''
#91.
'''
listas = []

for i in range(10):
    numero = int(input('Digite 1 numero 10 vezes: '))
    listas.append(numero)

novalista = set(listas)
print(novalista)
'''

#92.
'''
conjunto1 = {1,2,3,4}
conjunto2 = {2,3,5,6}

doisjuntos = conjunto1 & conjunto2
print (f'O conjunto 1 é: {conjunto1}')
print (f'O conjunto 2 é: {conjunto2}')
print (f'Os dois juntos são {doisjuntos}')
'''
#93.
'''
tupla = (12, 10)
print (f'A coordenada x é = {tupla[0]}')
print (f'A coordenada y é = {tupla[1]}')
'''
#94.
'''
pessoa = {'nome': 'Marcelo','idade': 15,'cidade': 'Uberlândia'}
print(f'Meu nome é {pessoa["nome"]}, tenho {pessoa["idade"]} anos e moro em {pessoa["cidade"]}')
'''
#95
'''
nome = input('Digite o nome do aluno: ')
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

aluno = {'nome': nome, 'nota1': nota1, 'nota2': nota2}

aluno['media'] = (nota1 + nota2) / 2

print(aluno)
'''
#96
'''
produtos = [{'nome': 'Camisa', 'preco': 50},{'nome': 'Calça', 'preco': 100},{'nome': 'Bota', 'preco': 200}]
for produto in (produtos):
    print(f'Produto: {produto["nome"]} - Preço: R${produto["preco"]}')
'''
#97
'''
produtos = [{'nome': 'Camisa', 'preco': 50},{'nome': 'Calça', 'preco': 100},{'nome': 'Bota', 'preco': 200}]
mais_caro = produtos[0]

for produto in (produtos):
    if (produto['preco'] > mais_caro['preco']):
        mais_caro = produto
print(f'O produto mais caro é {mais_caro["nome"]}, custando R${mais_caro["preco"]}')
'''
