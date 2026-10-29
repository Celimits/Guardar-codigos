import calculos


'''
Bloco 8 - Arquivos, excecoes e organizacao
Nivel sugerido: Intermediario para avancado
Foco: persistir dados em arquivos, tratar erros esperados e separar codigo em modulos.
'''
#116
'''
with open("python.txt", "w", encoding="utf-8") as nome:
    nome.write(str(input('Digite o seu nome: ')))
'''
#117
'''
registro = ''
while registro != 'sair':
    registro = str(input('Digite o seu nome: '))
    if registro == 'sair':
        break
    with open("python.txt", "a", encoding="utf-8") as Nomes:
        Nomes.write(registro + "\n")

'''
'''
#118
with open("python.txt", "r", encoding="utf-8") as conteudos:
    conteudo = conteudos.read()
print(conteudo)
'''
#119
'''
with open("python.txt", "r", encoding="utf-8") as ler:
    for linha in ler:
        print(linha.strip())
'''
#120
'''
quantidade = 0
with open("python.txt", "r", encoding="utf-8") as ler:
    for linha in ler:
        quantidade += 1
print(quantidade)
'''
#121
'''
try:
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite um valor: '))
    print(f'A divisão é {valor1/valor2}')
except ValueError:
    print('Digite um numero inteiro')
'''
#122
'''
try:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))

    resultado = num1 / num2
    print(f'O resultado da divisão é: {resultado}')

except ValueError:
    print('Erro: digite apenas números válidos.')

except ZeroDivisionError:
    print('Erro: não é possível dividir por zero.')
'''
#123
'''
calculos.somar()
calculos.diminuir()
'''
#124