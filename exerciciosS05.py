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

#Até agora não aprendi sobre switch no curso python, poderia fazer com if, elif e else

19 - Faça um programa para verificar se determinado número inteiro é divisível por 3 ou
5, mas não simultaneamente pelos dois.

print('Digite um número para testar')
n = int(input())

t1 = n % 3
t2 = n % 5

if t1 + t2 == 0:
    print('Teste falhou pois os dois números são divisíveis')
elif t1 == 0 or t2 == 0:
    print('Passou no teste!!!')
else:
    print('Teste falhou pois nenhum é divisível')

21 - Escreva um menu de opções abaixo, leia qual opção o usuário escolheu,
execute a operação escolhida, escreva uma mensagem de erro se a opção for inválida.
Escolha a opção:
1 - Soma de 2 números.
2 - Diferença entre 2 números (maior pelo menor).
3 - Produto entre 2 números.
4 - Divisão entre 2 números (o denominador não pode ser zero)
Opção:

print('Selecione uma das opções abaixo:')
print('1 - Soma de 2 números.')
print('2 - Diferença entre 2 números (maior pelo menor).')
print('3 - Produto entre 2 números.')
print('4 - Divisão entre 2 números (o denominador não pode ser zero)')
print('Opção:')
s = int(input())

if s == 1:
    print('Selecione o primeiro numero')
    n1 = int(input())
    print('Selecione o segundo numero')
    n2 = int(input())
    r = n1 + n2
    print(f'O resultado da soma é {r}')

elif s == 2:
    print('Selecione o primeiro numero')
    n1 = int(input())
    print('Selecione o segundo numero')
    n2 = int(input())
    if n1 > n2:
        r = n1 - n2
        print(f'A diferença entre os dois números é {r}')
    elif n2 > n1:
        r = n2 - n1
        print(f'A diferença entre os dois números é {r}')
    else:
        print('A diferença entre os dois números é 0')

elif s == 3:
    print('Selecione o primeiro numero')
    n1 = int(input())
    print('Selecione o segundo numero')
    n2 = int(input())
    r = n1 * n2
    print(f'O resultado da multiplicação foi {r}')

elif s == 4:
    print('Selecione o numerador')
    n1 = float(input())
    print('Selecione o denominador')
    n2 = float(input())
    if n2 == 0:
        print('O denominador não pode ser 0')
    else:
        r = n1 / n2
        print(f'O resultado da divisão foi {r}')

else:
    print('Opção inválida')

'''

print('Selecione uma das opções abaixo:')
print('1 - Soma de 2 números.')
print('2 - Diferença entre 2 números (maior pelo menor).')
print('3 - Produto entre 2 números.')
print('4 - Divisão entre 2 números (o denominador não pode ser zero)')
print('Opção:')
s = int(input())

if s == 1:
    print('Selecione o primeiro numero')
    n1 = int(input())
    print('Selecione o segundo numero')
    n2 = int(input())
    r = n1 + n2
    print(f'O resultado da soma é {r}')

elif s == 2:
    print('Selecione o primeiro numero')
    n1 = int(input())
    print('Selecione o segundo numero')
    n2 = int(input())
    if n1 > n2:
        r = n1 - n2
        print(f'A diferença entre os dois números é {r}')
    elif n2 > n1:
        r = n2 - n1
        print(f'A diferença entre os dois números é {r}')
    else:
        print('A diferença entre os dois números é 0')

elif s == 3:
    print('Selecione o primeiro numero')
    n1 = int(input())
    print('Selecione o segundo numero')
    n2 = int(input())
    r = n1 * n2
    print(f'O resultado da multiplicação foi {r}')

elif s == 4:
    print('Selecione o numerador')
    n1 = float(input())
    print('Selecione o denominador')
    n2 = float(input())
    if n2 == 0:
        print('O denominador não pode ser 0')
    else:
        r = n1 / n2
        print(f'O resultado da divisão foi {r}')

else:
    print('Opção inválida')
