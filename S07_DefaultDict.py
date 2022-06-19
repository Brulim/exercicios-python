"""
DEFAULT DICT
https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recapitulando dicionário
dicionario = {'nome' : 'Bruno Lima'}
print(dicionario)
print(dicionario['nome'])
print(dicionario['outro']) # ??? KeyError
# A busca de uma chave inexistente retorna KeyError

Default Dict -> Ao criar um dicionário utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Esse valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será
criada e o valor default será atribuído.

OBS: Lambdas são funções sem nome, que podem ou não receber parâmetros de enrada
e retornar valores.

"""

# Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

dicionario['curso'] = 'Programação em Python: Essencial'

print(dicionario)

print(dicionario['outro']) #KeyError no dicionário comum, mas aqui não.

print(dicionario)
