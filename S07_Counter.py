"""
COUNTER (Contador)
Collections -> high-perfomance Container Datetypes

Counter -> Recebe um iterável como parâmetro e cria um objeto do tipo Collections Counter
que é parecido com um dicionário, contendo como chave o elemento da lista passada como
parâmetro e como valor o número de ocorrências desse elemento.

# Utilizando counters

# Realizando o import
from collections import Counter

lista = [1, 1, 1, 2, 2, 3, 3, 3, 3, 1, 1, 2, 2, 4, 4, 4, 5, 5, 5, 3, 45, 34, 66]

# Utilizando o counter
res = Counter(lista)

print(type(res))
print(res)

# Veja que, para cada elemento da lista, o Counter criou uma chave e colocou como
valor a quantidade de ocorrência.

#Exemplo 2
print(Counter('Bruno Liiima'))

#Exemplo 3
texto = " Estados Unidos vários anos após a restauração da Sociedade, assumindo o
trabalho pastoral e ensinando teologia em Conewago, Pensilvânia, antes de se tornar
professor em tempo integral na Universidade de Georgetown. Lá, ele também tornou-se
no segundo bibliotecário dedicado da biblioteca de Georgetown. Eventualmente, Feiner
 tornou-se presidente da universidade em 1826. Enquanto presidente, ele ensinou
 teologia em Georgetown e ministrou à congregação na Igreja da Santíssima Trindade.
"

palavras = texto.split()
res = Counter(palavras)
print(res)

# Encontrando as 5 palavras com mais ocorrência no texto
print(res.most_common(5))

"""

