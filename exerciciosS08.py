"""
EXERCÍCIOS PYTHOS - SEÇÃO 08

1 - Crie uma função que recebe como parâmetro um número inteiro e devolve dobro.

def dobro(n):
    return n ** 2

print(dobro(2))

2 - Faça uma função que recebe a data atual (dia, mês e ano em inteiro) e exiba-a
na tela no formato textual pro extenso. Exemplo: Data:01/01/2000, Imprimir:
1 de janeiro de 2000.

meses = {'01': 'janeiro', '02': 'fevereiro', '03': 'março', '04': 'abril',
'05': 'maio', '06': 'junho', '07': 'julho', '08': 'agosto',
'09': 'setembro', '10': 'outubro', '11': 'novembro', '12': 'dezembro'}

print(meses.get('12')) #Apenas testando o dict

def data(dd, mm, aaaa):
    return f"{dd} de {meses.get(mm)} de {aaaa}"

print(data(16, '07', 1982)) #Tive que informar mês como string por conta do 0

3 - Faça uma função para verificar se um número é positivo ou negativo. Sendo que
o retorno será 1 se positivo, -1 se negativo e 0 se for 0.

def positivo(num):
    if num == 0:
        return 0
    elif num > 0:
        return 1
    return -1

print(positivo(10))
print(positivo(0))
print(positivo(-5))

11 Elabore uma função que recebe três notas e uma letra como parâmetro.
Se a letra for A, a função deverá calcular a média aritmética das notas;
se for P, calcular a média ponderada com pesos 5, 3 e 2.

def media(n1, n2, n3, tipo):
    if tipo == 'A':
        return (n1 + n2 + n3)/3
    elif tipo == 'P':
        return (n1*5 + n2*3 + n3*2)/10
    return 'Tipo inválido'

print(media(9, 8, 7, 'A'))
print(media(10, 10, 10, 'P'))
print(media(10, 10, 10, 'Z'))

"""

def media(n1, n2, n3, tipo):
    if tipo == 'A':
        return (n1 + n2 + n3)/3
    elif tipo == 'P':
        return (n1*5 + n2*3 + n3*2)/10
    return 'Tipo inválido'

print(media(9, 8, 7, 'A'))
print(media(10, 10, 10, 'P'))
print(media(10, 10, 10, 'Z'))
