"""
1 - Faça um programa que possua um vetor denominado A que armazene 6 números inteiros.
O programa deve executar os seguintes passos:
(a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, 7.
(b) Armazene em uma veriável inteira (simples) a soma entre os valores das posições
A[0], A[1] e A[5] do vetor e mostre na tela esta soma.
(c) Modigique o vetor na posição 4, atribuinto a esta posição o valor 100.
(d) Mostre na tela cada valor do vetor A, um em cada linha.

A = [1, 0, 5, -2, -5, 7]

soma = A[0] + A[1] + A[5]
print(soma)

A[4] = 100
print(A)

indice = 0
while indice < len(A):
    print(A[indice])
    indice = indice + 1

3 - Ler um conjunto de números reais, armazenando-o em vetor e calcular o quadrado dos
componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos tem 10
elementos cada. Imprimir todos os conjuntos.

a = [1, 0, 5, 1.5, -5, 7, 2, 4, 4, 8]
q = []
indice = 0

while indice < len(a):
    app = a[indice] ** 2
    q.append(app)
    indice = indice + 1
print(a)
print(q)

4 - Faça um programa que leia um vetor de o posições e, em seguida, leia também dois valores
X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa deverá
escrever a soma dos valores encontrados nas respectivas posições X e Y

a = [1, 0, 5, 1.5, -5, 7, 2, 4]
x = a[0]
y = a[2]
print(x + y)

5 - Leia um vetor de 10 posições. Contar e escrever quantos valores pares ele possui.

v = [1, 0, 5, 2, 4, 7, 2, 15, 30, 45]
pares = []
indice = 0

while indice < len(v):
    resto = v[indice] % 2
    if resto == 0:
        par = v[indice]
        pares.append(par)
    indice = indice + 1
print(pares)
elementos = len(pares)
print(f'Há {elementos} elementos pares na lista.')



"""

v = [1, 0, 5, 2, 4, 7, 2, 15, 30, 45]
pares = []
indice = 0

while indice < len(v):
    resto = v[indice] % 2
    if resto == 0:
        par = v[indice]
        pares.append(par)
    indice = indice + 1
print(pares)
elementos = len(pares)
print(f'Há {elementos} elementos pares na lista.')
