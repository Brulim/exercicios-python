"""
DICIONÁRIOS - dict
OBS.: Em algumas linguagens de programação, os dicionários Python
são conhecidos por mapas.
Dicionários são coleções do tipo chave/valor.
São representados por chaves {}.
print(type({}))

# Chave e valor são separados por dois pontos 'chave:valor";
# Tanto chave quanto valor podem ser de qualquer tipo de dado;
#Podemos misturar tipos de dados;

# Criação de dicionários

# Forma 1 (Mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (Menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguay')

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acesando via chave, da mesma forma que lista/tupla (chave definida)
print(paises['br'])
print(paises['py'])

#Forma 2 - Acessando via get (recomendado)
print(paises.get('br'))
print(paises.get('ru'))
#Pela forma dois, ao informar uma chave inexistente, retornará none
Diferente da forma 1, que retornava erro

Tipo none
O tipo de dado none em Python representa tipo sem tipo, também conhecido como vazio
falar que é um tipo sem tipo é mais apropriado
OBS: O tipo None é sempre especivicado com a primeira letra maiúscula.
O tipo none em python é sempre considerado como false.

Quando utilizamos?
- Podemos utilizar Nove para criar uma variável inicial sem definir o tipo.

#Podemos definir um valor padrão caso não encotnremos o objeto com a chave informada.
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}
pais = paises.get('ru', 'Não encontrato')
print(f'Encontrei o país {pais}')

#Podemos usar qualquer tipo de dado. Abaixo um exemple de tupla utilizada como chave:
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}
print(localidades)
print(type(localidades))

# Adicionar elementos em um dicionário
receita = {'jan': 100, 'fev': 120, 'mar': 300}
#Forma 1 (mais comum)
receita['abr'] = 350
print(receita)
#Forma 2
novo_dado = {'mai' : 500}
receita.update(novo_dado)
print(receita)

#Atualizando dados em um dicionário
#Forma 1 (é a mesma coisa da insersão)
receita['mai'] = 550
print(receita)

# O mesmo comando utilizado para adicionar, serve para alterar
# Em dicionários, não é possível ter chaves repetidas

#Remover dados de um dicionário
#Forma 1 (mais comum)
receita = {'jan': 100, 'fev': 120, 'mar': 300}
ret = receita.pop('mar')
print(ret)
print(receita)
# Ao removermos um objeto, o valor deste objeto é sempre retornado.
#Forma 2
del receita['fev']
print(receita)
#Neste caso o valor removido não é retornado.

#Limpar dicionário
receita.clear()
print(receita)

#Copiando um dicionário para outro:
#Forma1 - Deep copy (independente)
novo = receita.copy()
#Forma 2 # Shallow Copy (espelhados)
novo = receita

"""
receita = {'jan': 100, 'fev': 120, 'mar': 300}
novo = receita
print(novo)
novo['d'] = 4

print(receita)
print(novo)