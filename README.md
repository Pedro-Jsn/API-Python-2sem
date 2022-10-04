# API Python 2 semestre CCO

**Essa aplicação foi feita no intuito de capturar os dados da máquina de uma maneira flexível sem que os comandos ficassem blocados no código.**
**Este projeto foi feito como uma tentativa de ajudar colegas e alunos da SPTech.**


#### Como funciona?
**Conexão banco:**
```python
import mysql.connector

bdsql = mysql.connector.connect(host="localhost", user="seuUser", 
password="senhaUser", database="nomeBanco")

mycursor = bdsql.cursor()
```
**Instale a biblioteca no terminal:**
```
pip install mysql-connector-python 
```
**Explicação:**

Ao importar a biblioteca do mysql connector, criamos uma variável para receber a conexão com o banco, onde **```mysql.connector```** é o módulo que estamos importando e **```.connect```** é uma função para criar a conexão com o banco de dados e nela passamos os argumentos para a conexão com aquele banco.
Após isso criamos um cursor, ou seja, algo que nos permite executar um código dentro do nosso banco de dados, então criamos uma variável para receber esse cursor onde **```bdsql.cursor()```** bdsql é a variável criada para me conectar ao banco e a função **```cursor()```** é o responsável por executar algum código dentro dessa conexão com o banco.

**Pegar endereço mac da maquina:**
```python
from getmac import get_mac_address as mac

print(mac())
```
**Instale a biblioteca antes:**
```
pip install getmac
```
**Explicação:**
Da biblioteca **```getmac```** queremos pegar o endereço mac da máquina, então importamos a função **```get_mac_address```** e damos um apelido para essa função de **```mac```** e como o **```get_mac_address```** é uma função para executar basta colocar o **()** no apelido **```mac```** para o Python entender que você está "chamando" a função.

#### Uso de Thread:
**Caso você queira um programa fazendo multitarefas, você pode utilizar o conceito de Thread, thread basicamente é você executar determinadas partes do código sem que tenha que esperar outras partes serem executadas, você pode criar várias Threads para assim trabalhar com várias tarefas simultaneamente.** 

**Exemplo:**
```python
import threading

def exemplo(nome):
  for i in range(5):
    print(f"{nome} contou até {i+1}")

def exemplo2(nome):
  for i in range(7):
    print(f"{nome} contou até {i+1}")


threading.Thread(target=exemplo, args=('Pedro',)).start()
threading.Thread(target=exemplo2, args=('Gustavo',)).start()
```

**Explicação:**
Aqui estamos importando o modulo de threading, para podermos usar a Thread, estamos criando duas funções que vão ser as funções a serem executadas simultaneamente, **```threading.Thread(target=exemplo, args=('Pedro',)).start()```** onde **```threading```** é o modulo que estamos importando **```Thread```** é a classe que estamos executando no módulo **```threading```** que recebe os parametros **```target```** que é a função que queremos executar e **```args```** que são os argumentos(parametros) que queremos passar para aquela função **```start()```** é uma função utilizada para iniciar as Threads.

**Observação:**
Se o seu computador não tiver mais cores do que a quantidade de Thread que você criou, as Threads trabalharam em escalonamento, ou seja, uma será executada e após um tempo executa a próxima, depois volta para a primeira e assim sucessivamente.

#### Documentação das bibliotecas utilizadas: 

 - [Psutil](https://psutil.readthedocs.io/en/latest/)
 - [Threading](https://docs.python.org/3/library/threading.html)
 - [Mysql.connector](https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html)
 - [Getmac](https://pypi.org/project/getmac/)
 

#### Feito por: 

- [@Pedro Henrique Jesuino Varela](https://github.com/Pedro-Jsn)
- [@Vinícius Da Silva Sousa](https://github.com/VS-Sousa)
- [@Gustavo Antonio](https://github.com/GustavoAntonio12)
