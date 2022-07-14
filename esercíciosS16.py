"""
Observações Pessoais:
Aparentemente esses exercícios não foram criados para python, utilizei apenas a lógica
do que é solicitado no enunciado, sem me apegar aos métodos sugeridos.

1- Crie uma classe para representar uma pessoa, com os atributos privados de nome, idade e altura.
Crie os métodos públicos necessários para sets e gets e também um método para imprimir os dados de uma pessoa.

2- Crie uma classe Agenda que pode armazenar 10 pessoas e seja capaz de realizar as seguintes operações:
- void armazenaPessoa)String nome, int idade, float altura);
- void removePessoa(String nome);
-int buscaPessoa(String nome); // informa em que posição da agenda está a pessoa
-void imprimeAgenda(); // imprime os dados de todas as pessoas da agenda
- void imprimePessoa (int index); // imprime os dados da pessoa que está na posição "i" da agena.

3- Crie uma classe denominada Elevador para armazenar as informações de um elevador dentro de um prédio.
A classe deve armazenar o andar atual (térreo - 0), total de andares do prédio, excluindo o térreo, capacidade
do elevador, e quantas pessoas estão presentes nele.

A classe deve também disponibilizar os seguintes métodos:
- Inicializa: que deve receber como parâmetros a capacidade do elevador e o total de andares do prédio
(os elevadores sempre começam no térro e vazio);
- Entra: para acrescentar uma pessoa no elevador (só deve acrescentar se ainda houver espaço);
- Sai: para remover uma pessoa do elevador (só deve remover se houver alguém dentro dele);
- Sobe: para subir um andar (não deve subir se já estiver no último andar);
- Desce: para descer um antar (não deve descer se já estiver no térreo);
- Encapsular todos os atributos da classe (criar métodos set e get);

4 - Crie uma classe Televisão e uma classe Controle Remoto que pode controlar o volume e trocar os canais da televisão.

- O controle de volume permite aumentar ou diminuir a potência do volume de som em uma unidade de cada vez;
- O controle de canal também permite aumentar e diminuir o número do canal em uma unidade, porém, também possibilita
trocar para um canal indicado;
- Também devem existir métodos para consultar o valor do volume de som e o canal selecionado.

"""