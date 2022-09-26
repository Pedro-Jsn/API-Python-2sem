import os
from time import sleep

def main():
    print("Iniciando o monitoramento...")

    sleep(1)

    while True:
        bdsql, mycursor = conectar()

        mycursor.execute("SELECT * from parametro WHERE fkServidor = 1")

        resposta = mycursor.fetchall()

        arquivo = open('app.txt', 'w')
        
        arquivo.write("import threading")

        i=1;
        for row in resposta :
            isTupla = row[3]

            if isTupla == 0:
                criando_funcao = f"""
def executar{i}(servidor, componente, metrica):
    import psutil
    bdsql, cursores = conectar()

    sql = ("SELECT comando FROM metrica WHERE idMetrica = %s")
    val = (metrica, )    
    cursores.execute(sql, val)    

    comando = cursores.fetchall()    
    leitura = eval(comando[0][0])    

    sql = ("INSERT INTO leitura(fkServidor, fkComponente, fkMetrica, horario, valorLido) VALUES(%s, %s, %s, now(), %s)")    
    val = (servidor, componente, metrica, leitura, )    

    cursores.execute(sql, val)
    bdsql.commit()

"""

            else:
                criando_funcao = f"""
def executar{i}(servidor, componente, metrica):
    import psutil
    bdsql, cursores = conectar()

    sql = ("SELECT comando FROM metrica WHERE idMetrica = %s")
    val = (metrica, )    
    cursores.execute(sql, val)    

    comando = cursores.fetchall()    
    leitura = eval(comando[0][0])    

    for row in leitura:
        sql = ("INSERT INTO leitura(fkServidor, fkComponente, fkMetrica, horario, valorLido) VALUES(%s, %s, %s, now(), %s)")    
        val = (servidor, componente, metrica, row, )  

        cursores.execute(sql, val)
        bdsql.commit()

    
"""
    
            arquivo.write(criando_funcao)
            arquivo.write(f"threading.Thread(target=executar{i}, args=({row[0]}, {row[1]}, {row[2]},)).start()")

            i = i + 1
        arquivo.close()

        exec(open('app.txt').read())

        os.remove('app.txt')

def conectar():
  import mysql.connector
  bdsql = mysql.connector.connect(host="localhost", user="nomeUsuario", password="SuaSenha", database="nomeBanco")
  cursor = bdsql.cursor()

  return (bdsql, cursor)

if __name__ == '__main__':
    main()