# 1
print('Hello wrold!')

# 2
nome = str(input("Escreva seu nome: "))
idade = int(input("Escreva sua idade: "))
cidade = str(input("Escreva sua cidade: "))
print('Seu nome é ', nome, ', tem ', idade, 'anos', 'e mora em ', cidade)

# 3
usuario = str(input('Escreva seu usuario: '))
print('Olá', usuario, '!')

# 4
soma1 = int(input('Digite o primeiro valor '))
soma2 = int(input('Digite o segundo valor '))
total = soma1 + soma2
print('O valor da soma é:', total)

# 5
valor1 = int(input('Digite o primeiro valor '))
valor2 = int(input('Digite o segundo valor '))
soma = valor1 + valor2
sub = valor1 - valor2
mult = valor1 * valor2
divisao = valor1 / valor2
print('')
print('O valor da soma é:', soma)
print('O valor da subtração é:', sub)
print('O valor da multiplicação é:', mult)
print('O valor da divisão é:', divisao)

# 6
dobro = int(input('Digite o valor que dejesa o dobro: '))
dobrov = dobro * 2
print('O valor é', dobro, 'e o dobro é', dobrov)

# 7
value = int(input('Digite o valor que dejesa o triplo e a metade: '))
triplo = value * 3
metade = value / 2
print('O valor é', value, 'e o triplo é', triplo, 'e a metade é', metade)

# 9
primeiro = str(input('Digite seu primeiro nome: '))
sobrenome = str(input('Digite seu sobrenome: '))
completo = primeiro + ' ' + sobrenome
print('Seu nome completo é:', completo)

# 10
nascimento = int(input('Digite seu ano de nascimento: '))
idade = 2026 - nascimento
print('Você tem aproximadamente', idade, 'anos')

# 11
metros = float(input('Digite a medida em metros: '))
cm = metros * 100
mm = metros * 1000
print(metros, 'metros são', cm, 'centímetros e', mm, 'milímetros')

# 12
minutos = int(input('Digite a quantidade de minutos: '))
segundos = minutos * 60
print(minutos, 'minutos são', segundos, 'segundos')

# 13
horas = int(input('Digite a quantidade de horas: '))
minutos = horas * 60
print(horas, 'horas são', minutos, 'minutos')

# 14
celsius = float(input('Digite a temperatura em Celsius: '))
fahrenheit = celsius * 9 / 5 + 32
print(celsius, 'graus Celsius são', fahrenheit, 'graus Fahrenheit')

# 15
reais = float(input('Digite o valor em reais: '))
cotacao = 5.00
dolares = reais / cotacao
print('Com', reais, 'reais você compra', dolares, 'dólares')

# 16
lado = float(input('Digite o tamanho do lado do quadrado: '))
area = lado * lado
print('A área do quadrado é:', area)

# 17
largura = float(input('Digite a largura do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))
area = largura * altura
print('A área do retângulo é:', area)

# 18
base = float(input('Digite a base do triângulo: '))
altura = float(input('Digite a altura do triângulo: '))
area = (base * altura) / 2
print('A área do triângulo é:', area)

# 19
raio = float(input('Digite o raio do círculo: '))
pi = 3.14
area = pi * raio ** 2
print('A área do círculo é:', area)

# 20
largura = float(input('Digite a largura do retângulo: '))
altura = float(input('Digite a altura do retângulo: '))
perimetro = 2 * (largura + altura)
print('O perímetro do retângulo é:', perimetro)

# 21
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
print('A média é:', f'{media:.2f}')

# 22
valorhora = float(input('Digite o valor recebido por hora: '))
horas = int(input('Digite o número de horas trabalhadas no mês: '))
salario = valorhora * horas
print('O salário bruto é:', salario)

# 23
salario = float(input('Digite o salário: '))
aumento = salario * 0.10
novosalario = salario + aumento
print('Salário original:', salario)
print('Valor do aumento:', aumento)
print('Novo salário:', novosalario)

# 24
preco = float(input('Digite o preço do produto: '))
desconto = preco * 0.15
precofinal = preco - desconto
print('Valor do desconto:', desconto)
print('Preço final:', precofinal)

# 25
total = float(input('Digite o valor total da compra: '))
parcelas = int(input('Digite a quantidade de parcelas: '))
valorparcela = total / parcelas
print('Cada parcela será de:', valorparcela)

# 26
peso = float(input('Digite seu peso em kg: '))
altura = float(input('Digite sua altura em metros: '))
imc = peso / altura ** 2
print('Seu IMC é:', f'{imc:.2f}')

# 27
nota1 = float(input('Digite a primeira nota (peso 2): '))
nota2 = float(input('Digite a segunda nota (peso 3): '))
media = (nota1 * 2 + nota2 * 3) / 5
print('A média ponderada é:', media)

# 28
valor1 = int(input('Digite o primeiro valor: '))
valor2 = int(input('Digite o segundo valor: '))
quociente = valor1 // valor2
resto = valor1 % valor2
print('O quociente é:', quociente)
print('O resto é:', resto)

# 29
numero = int(input('Digite um número inteiro: '))
antecessor = numero - 1
sucessor = numero + 1
print('O antecessor é:', antecessor, 'e o sucessor é:', sucessor)

# 30
base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))
resultado = base ** expoente
print(base, 'elevado a', expoente, 'é:', resultado)

# 31
valor = int(input(('Digite um valor: ')))
if (valor > 0):
    print('É um valor positivo')
elif (valor == 0):
    print('É igual a 0')
else:
    print('É um valor negativo')

# 32
valori = int(input(('Digite a sua idade: ')))
if (valori >= 18):
    print('Tu é maior de idade bixão, vai aproveitar o resto da sua vida!')
else:
    print('Tu é menor de idade mlk, vai fazer merda enquanto pode!')

# 33
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")

# 34
numberone = int(input("Digite um número para comparar: "))
numbertwo = int(input("Digite o segundo número para comparar: "))
if (numberone > numbertwo):
    print('O número', numberone, 'é maior que', numbertwo)
elif (numbertwo == numberone):
    print('O número', numberone, 'é igual ao', numbertwo)
else:
    print('O número', numberone, 'é menor que', numbertwo)

# 35
number1 = int(input("Digite um número para comparar: "))
number2 = int(input("Digite o segundo número para comparar: "))
number3 = int(input("Digite o segundo número para comparar: "))
if (number1 > number2 and number1 > number3):
    print('O número', number1, 'é maior que', number2, 'e', number3)
elif (number2 > number1 and number2 > number3):
    print('O número', number2, 'é maior que o', number1, 'e', number3)
else:
    print('O número', number3, 'é maior que', number2, 'e', number1)

# 37
nota = float(input('Qual a sua nota? '))
if (nota >= 6):
    print('Você esta aprovado!')
else:
    print('Você esta reprovado')

# 38
notaf = float(input('Qual a sua nota final? '))
if (notaf >= 7):
    print('Você esta aprovado!')
elif (notaf >= 5 and notaf > 7):
    print('Você esta de recperação')
else:
    print('Você esta reprovado')

# 39
faixaetaria = int(input('Qual é a sua idade para informar sua faixa etaria? '))
if (faixaetaria > 0 and faixaetaria <= 11):
    print('Você ainda é uma criança que farma aura 67 vezes!')
elif (faixaetaria >= 12 and faixaetaria <= 18):
    print('Você ja está na adolescencia, melhor fase da vida')
elif (faixaetaria >= 18 and faixaetaria <= 59):
    print('Você ja esta na vda adulta, vai tirar a carteira e conquistar as suas coisinhas no caminho certo!')
elif (faixaetaria <= 0):
    print('Error 404, verifique a sua idade')
else:
    print('Você ja esta idoso, aproveite seu finalzinho!')

# 40
for tentativa in range(3):
    senha = input('Qual é a senha? ')
    if (senha == 'admin'):
        print('Acesso liberado!')
        print('Seja bem vindo!!')
        break
    else:
        print('Acesso negado :(')
        print('Tentativas restantes:', 2 - tentativa)

# 41
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

# 42
numerode5 = int(input('Digite um número inteiro: '))

if numerode5 % 5 == 0:
    print('É múltiplo de 5')
else:
    print('Não é múltiplo de 5')

# 43
numero = int(input('Digite um número: '))

if numero % 3 == 0 and numero % 5 == 0:
    print('É divisível por 3 e 5')
else:
    print('Não é divisível por 3 e 5')

# 44
ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    print('Ano bissexto')
else:
    print('Não é ano bissexto')

# 45
valor = float(input('Digite o valor da compra: R$ '))

if valor >= 200:
    valor = valor * 0.90

print('Valor final: R$', valor)

# 46
valor = float(input('Digite o valor da compra: R$ '))

if valor >= 150:
    total = valor
else:
    total = valor + 20

print('Total final: R$', total)

# 47
num1 = float(input('Digite o primeiro número: '))
num2 = float(input('Digite o segundo número: '))
operacao = input('Digite a operação (+, - , * ou /): ')

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

# 48
lado1 = float(input('Digite o primeiro lado: '))
lado2 = float(input('Digite o segundo lado: '))
lado3 = float(input('Digite o terceiro lado: '))

if (lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2):
    print('Pode formar um triângulo')
else:
    print('Não pode formar um triângulo')