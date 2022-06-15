"""
EXERCÍCIOS SEÇÃO 4 - Varíáveis e Tipos de Dados em Python

1 - Faça um programa que leia um número inteiro e o imprima:

num = 5
print(num)

2 - Ler e imprimir um número real:

# type = float (lembrar de utilizar ponto e não vírgula)

num = '2.5'
print(num)

3 - Peça para o usuário digitar três valores inteiros e imprima a soma deles:

# Tentei conforme o código abaixo mas o resultado foi somador como string:

print('Digite valor 1')
valor1 = input()

print('Digite valor 2')
valor2 = input()

print('Digite valor 3')
valor3 = input()

resultado = valor1 + valor2 + valor3

print(f'A soma dos valores é {resultado}')

#Desta forma deu certo:

print('Digite valor 1')
valor1 = input()

print('Digite valor 2')
valor2 = input()

print('Digite valor 3')
valor3 = input()

resultado = int(valor1) + int(valor2) + int(valor3)

print(f'A soma dos valores é {resultado}')

4 - Ler um número real e retornar o quadrado desse número.

num = 2.2
quadrado = num ** 2
print(quadrado)

5 - Leia um número real e imprima a quinta parte desse número

num = 15.5
resultado = num / 5
print(resultado)

6 - Leila uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit
A fórmula de conversão é: F = C*(9.0/5.0)+32.0

c = 30
fahrenheit = c*(9/5)+32
print(fahrenheit)

7 - Fahrenheit para Celcius
C = 5.0 * (F - 32.0)/9.0

f = 80
celcius = 5*(f - 32)/9
print(celcius)

8 - Kelvin para Celsius
C = K - 273,15

k = 320
celcius = k - 273.15
print(celcius)

9 - Celcius para Kelvin
K = C + 273,15

c = 40
kelvin = c + 273.15
print(kelvin)

10 à 27 - Mais exercícios de conversões

28 - Faça a leitura de três valores e apresente como resultado a soma do quadrado dos três valores lidos.

v1 = 2
v2 = 3
v3 = 4
resultado = (v1 ** 2) + (v2 ** 2) + (v3 ** 2)
print(resultado)

35 - Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação hipotenusa é igual
a raiz quadrada da soma dos quadrados dos catetos, faça um programa que recebe os catetos e imprima o resultado da operação.

#Encontrei alguns métodos envolvendo raiz quadrada. Achei mais simples elevar a 0,5.

a = 3
b = 4

resultado = ((a ** 2) + (b ** 2)) ** 0.5
print(resultado)

45 - Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela
ASCII para resolver o problema.

#A tabela ASCII possui códigos numérios vinculados aos caracteres.
Verifiquei que o caractere minúsculo está 32 posições acima do maiúsculo.
A partir daí segui com a lógica. chr(codigo)  ord(caractere)

maiuscula = 'A'
ord = ord(maiuscula)
min = chr(ord+32)

print(min)

46 - Faça um programa que leia um número inteiro positivo de 3 dígitos e o inverta

num = 123
numeroInvertido = int(str(num)[::-1]);

print(numeroInvertido)

47 - Leia um número de 4 dígitos e imprima 1 dígito por linha

num = 1234
n=str(num)

print(n[0])
print(n[1])
print(n[2])
print(n[3])

48 - Leia um valor inteiro em Segundos, imprima-o em horas, minutos e segundos.

print('Digite quantos segundos deseja converter')
sec = int(input())
h=int(sec/3600)
sec2 = sec-(h*3600)
m=int(sec2/60)
s = (sec2)-(m*60)
print(f'{sec} segundos equivale a {h}h:{m}m:{s}s')

49 - Faça um programa que leia um horário (hora, minuto e segundo) de início e a duração em segundos;
O programa deve resultar com o novo horário (término).

print('Digite hora de inicio')
hi = int(input())
print('Digite minuto')
mi = int(input())
print('Digite segundo')
si = int(input())
print('Digite duração em segundos')
t = int(input())

tt = int(hi*3600 + mi*60 + si + t)

h=int(tt/3600)
sec2 = tt-(h*3600)
m=int(sec2/60)
s = (sec2)-(m*60)
print(f'Horário do término é {h}h:{m}m:{s}s')

"""
print('Digite hora de inicio')
hi = int(input())
print('Digite minuto')
mi = int(input())
print('Digite segundo')
si = int(input())
print('Digite duração em segundos')
t = int(input())

tt = int(hi*3600 + mi*60 + si + t)

h=int(tt/3600)
sec2 = tt-(h*3600)
m=int(sec2/60)
s = (sec2)-(m*60)
print(f'Horário do término é {h}h:{m}m:{s}s')

