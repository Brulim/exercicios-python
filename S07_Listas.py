"""
### COLEÇÕES PYTHON

# LISTAS - List

Listas em Python funcionam como vetores/matrizes (arrays), com a diferença de serem
DINÂMICO e também de podermos colocar QUALQUER tipo de dado.
Representadas por []

lista1 = [10, 5, 2, 1, 4, 12]
print(lista1)
lista2 = ['a', 'b', 'c']
print(lista2)
lista3 = ['abc', 'def']
print(lista3)

lista1.sort() #ordena a lista
print(lista1)

lista1.append(42) #adicionando um único elemento na lista 1
print(lista1)
lista1.append(lista2) #Vai colocar o elemento lista 2 dentro de lista 1
print(lista1)

lista1.extend([5, 25, 55]) #coloca vários elementos dentro da lista
print(lista1)
lista1.extend(['abc'])
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
lista1.insert(2, 'Insert2')
print(lista1)

# É possível somar listas
lista1 = lista1 + lista2

# Inverter Listas
lista1.reverse()
#Ou
print(lista1[::-1])

# Contar quantos elementos existem dentro da lista
print(len(lista1))

# Remover o último elemento da lista
lista1.pop()
#ou especificando a posição do elemento
lista1.pop(2)

#Split (cria uma liste a partir de string separada pro espaços como padrão ou outro separador)

nome = 'Bruno Silva,Lima'
print(nome)
nome = nome.split()
print(nome)

ou

nome = 'Bruno Silva,Lima'
print(nome)
nome = nome.split(',')
print(nome)

#Pegar cada elemento de uma lista, atribuir espaço entre e montar uma string:
lista1 = ['a', 'a', 'b', 'cv', 'd', 'de']
nome = ' '.join(lista1)
print(nome)

#Iterando sobre listas
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

#While
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' pra sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

#Índice -1
O íncice -1 vai ser a última posição da lista. -2 penúltima e assim por diante
print(lista1[-1])

#len (tamanho de uma lista)

cores = ['verde', 'amarelo', 'azul', 'branco']

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

#Gerar indice em um for com enumerate

for indice, cor in enumerate(cores):
    print(indice, cor)

print(sum(lista)) # Soma da lista
print(max(lista)) # Valor máximo
print(min(lista)) # Valor mínimo

#Deep copy - cópia independente
listanova = lista.copy()

#Shallow Copy - o que for alterado em uma também será alterado na outra
listanova = lista


"""
cores = ['verde', 'amarelo', 'azul', 'branco']

#Gerar indice em um for com enumerate

for indice, cor in enumerate(cores):
    print(indice, cor)

