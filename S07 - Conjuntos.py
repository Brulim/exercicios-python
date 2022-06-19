"""
CONJUNTOS - set

-Conjuntos faz referência a teoria dos conjuntos da matemática.
- No Python os conjuntos são chamados de Sets.
- Sets (conjuntos) não possuem valores duplicados;
-Conjuntos não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não
nos importamos com a ordenação deles. Quando não precisamos se preocupar com chaves,
valores e itens duplicados.

Os conjutnos (sets) são referenciados em Python com chaves {}

Diferença entre conjuntos e mapas em Python:
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

# Definindo um conjunto:

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3}) # Repare que temos valores repetidos.

print(s)
print(type(s))

# OBS.: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Podemos verificar se determinado elemento está no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos')

tupla = 99, 2, 34, 23, 2, 12, 1, 44, 5, 34
print(f'Tupla: {tupla} com {len(tupla)} elementos')

dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos')
#dicionário também vai ficar com 8 pois não repete chaves

conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos')
print(type(conjunto))

# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu
# Informam manualmente a cidade de onde vieram.
# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar
novos elementos e ter repetição.

cidades = ['Guarujá', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Cuiaba', 'São Paulo']
print(cidades)
print(len(cidades)) #Quantas pessoas informando cidades
#Agora queremos saber quantas cidades distintas temos:
print(len(set(cidades)))

#Adicionando elementos em um conjunto
s = {1, 2, 3}
s.add(4) #Duplicidade não gera erro, simplesmente é ignorado.
print(s)

#Remover elementos em um conjunto
s = {1, 2, 3}
print(s)
#Forma 1
s.remove(3) #Não é indice, é o valor a ser removido. Se não tiver retorna KeyError.
print(s)
#Forma 1
s.discard(2) #OBS: Se o valor não for encontrado não gera erro.
print(s)

#Copiando um conjunto para outro.
s = {1, 2, 3}
print(s)
#Forma 1 - Deep Copy
novo = s.copy() #Dois objetos independentes
print(s)
#Forma 1 - Shallow Copy - Dois elementos espelhados
novo = s
print(s)

s.clear() # Remove todos os elementos de um conjunto

# Métodos matemáticos de conjuntos

#Imagene que temso dois conjuntos: Estudantes Python e Estudantes Java

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Bruno'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Bruno'}

#Veja que alguns alunos estudam os dois.

#Precisamos gerar um conjuntos com nomes de estudantes únicos

# Forma 1 - Utilizando union
unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

#Forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos.
#Forma1
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)
#Forma2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

#Gerar um conjunte de estudantes que não estão em outro curso

so_python = estudantes_python.difference(estudantes_java) #excluindo intersect
print(so_python)

so_java = estudantes_java.difference(estudantes_python) #excluindo intersect
print(so_java)

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))

"""

s = {1, 2, 3, 4, 5, 6}
print(sum(s))
print(max(s))
print(min(s))
print(len(s))


