"""
TUPLAS (tuple)

Tuplas são bastante parecidas com listas.
Existem duas diferenças básicas:
1 - As tuplas são representadas por parênteses ()
2 - As tuplas são imutáveis.

# CUIDADO 1: As tuplas são representadas por (), mas veja:

tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)

print(type(tupla2))

CUIDADO 2: Tupla com 1 elemento:
tupla3 = (4) #Isso não é uma tupla
tupla4 = (4,) #Isso é uma tupla
tupla5 = 4, #Isso é uma tupla

#Podemos concluir que tuplas são definidas pela vírgula.

# Podemos gerar uma tupla dinamicamente com range (inicio,fim,passo)
tupla = tuple(range(11))

# Desempacotamento de tupla (nº elementos precisa ser igual)

tupla = ('Bruno Lima', 'Programador Python')

nome, atr = tupla

print(nome)
print(atr)

#Não existem métodos de adiçãoe remoção em tuplas (imutaveis)
#sum, max, min (funciona se todos valores forem int)
#len funciona normalmente

# Concatenação de tuplas
tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

print(tupla1 + tupla2)

print(tupla1)
print(tupla2)
tupla1 = tupla1 + tupla2
print(tupla1)
# Tuplas são imutáveis mas seu valor pode ser reescrito

#Verificar se determinado elemento está contido na tupla
tupla1 = (1, 2, 3)
print(3 in tupla1) #True

# Iterando sobre uma tupla
tupla1 = (1, 2, 3)
for n in tupla1:
    print(n)

for indice, valor in enumerate(tupla1):
    print(indice, valor)

# Contanto elementos denro de uma tupla
tupla = (1, 2, 3, 'a', 'a', 'b', 'b')

print(tupla.count('a'))

nome = tuple('Bruno Lima')
print(nome)
print(nome.count('u'))

# Dicas na utilização de tuplas
- Devemos utilizar tuplas sempre que não precisarmos modificar dados
dentro de uma coleção. Exemplo: Meses ou dias da semana.

# Tuplas são mais rápidas do que listas.
# Tuplas deixam seu código mais seguro. (imutável)

"""
tupla = (1, 2, 3, 'a', 'a', 'b', 'b')

print(tupla.count('a'))

nome = tuple('Bruno Lima')
print(nome)

