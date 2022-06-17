"""
TEORIA - RANGES

#Forma 1

range(valor_de_parada)
OBS: valor_de_parada não inclusive (inicio padrão 0, e passo de 1 em 1)

for num in range(11):
    print(num)

#Forma 2

range(valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusive (início especificado pelo usuário, passo de 1 em 1)

for num in range(1, 11):
    print(num)

#Forma 3
range(valor_de_inicio, valor_de_parada, passo)

for num in range(1, 11, 2):
    print(num)

#forma 4
OBS: O mesmo da 3, trabalhando com contagem regressiva.

for num in range(10, 0, -1):
    print(num)

TEORIA - LOOP WHILE

Forma geral

while expressão_booleana:
    //execução do loop (bloco será repetido enquanto a booleana for verdadeira)
#Muito cuidado com o critério de parada para não causar um loop infinito

numero = 1

while numero < 10:
    print(numero)
    numero = numero + 1

TEORIA - SAINDO DE LOOPS COM BREAK

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop')

#Outro exemplo

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break

EXERCÍCIOS

1 - Faça um programa que mostre os cinco primeiros múltiplos de 3,
considerando números maiores que 0.
#Ajustei para retornar os 5 múltimplos de qualquer número maior que 0 informado.

n = int(input("Digite um número natural maior que 0: "))
parada = n*5+1

if n > 0:
    for r in range(n, parada, n):
        print(r)
else:
    print('Valor inválido.')

5 - Faça um programa que peça ao usuário para digitar 10 valores e some-os.

qtd = 10
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}º valor: '))
    soma = soma + num
print(f'A soma dos valores é {soma}')

7 - Faça um programa que leia 5 inteiros positivos, ignorando não positivos
e imprima sua média.
# Não consegui ignorar os não positivos

qtd = 5
soma = 0
media = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}º valor (positivo): '))
    soma = soma + num
    media = soma/qtd
print(f'A media dos valores é {media}')



"""

qtd = 5
soma = 0
media = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}º valor (positivo): '))
    soma = soma + num
    media = soma/qtd
print(f'A media dos valores é {media}')
