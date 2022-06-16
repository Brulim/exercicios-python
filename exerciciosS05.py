'''
1 - Faça um pograma qe receba dois números e mostre qual deles é maior.

print('Digite o valor 1')
v1 = int(input())
print('Digite o valor 2')
v2 = int(input())

if v1 > v2:
    print(f'O maior número é {v1}')

else:
    print(f'O maior número é {v2}')

2 - Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz
quadrada do número. Se for negativo, mostre uma mensagem dizendo que o número é inválido.

print('Digite um número positivo')
n = int(input())

if n >= 0:
    r = n ** 0.5
    print(f'A raiz quadrada do número informado é {r}')

else:
    print('O número é inválido')

8 - Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um
valor entre 0 e 10, onde casa a nota não possua um valor válido, este fato deve ser
informado ao usuário e o programa termina.

print('Digite a primeira nota')
n1 = float(input())
print('Digite a segunda nota')
n2 = float(input())
m = (n1+n2)/2

if n1 >= 0 and n1<=10 and n2 >= 0 and n2 <=10:
    print(m)

else:
    print('As duas notas devem estar entre 0 e 10')

11 - Escreva um programa que leia um número inteiro maior que zero e devolva, na tela, a
soma de todos os seus algarismos. Exemplo, 251 = 8. Se o número lido não for maior que zero
o progragrama terminará com a mensagem "número inválido".

#ajustei para Maior que zero e menor que mil para limitar os dígitos
no futuro imagino que possa ajustar utilizando algo parecido com foreach

print('Digite um número inteiro maior que zero e menor que 1000')
n = int(input())

if n >=0 and n<=1000:
    n1=str(n)
    soma = int(n1[0]) + int(n1[1]) + int(n1[2])
    print(soma)

else:
    print('Número inválido')

15 - Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este numero. Isto é, domingo se 1 e assim por diante.

#Até agora não aprendi sobre switch no curso python, poderia fazer com if, elsif e else

19 - Faça um programa para verificar se determinado número inteiro é divisível por 3 ou
5, mas não simultaneamente pelos dois.

'''

print('Digite um número inteiro maior que zero e menor que 1000')
n = int(input())

if n >=0 and n<=1000:
    n1=str(n)
    soma = int(n1[0]) + int(n1[1]) + int(n1[2])
    print(soma)

else:
    print('Número inválido')
