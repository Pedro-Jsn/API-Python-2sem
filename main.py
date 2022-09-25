import mysql.connector

def main():
    bdsql = mysql.connector.connect(host="localhost", user="root", password="TheKingBox751", database="appPython")

    mycursor = bdsql.cursor()

    mycursor.execute("SELECT * from parametro WHERE fkServidor = 1")

    resposta = mycursor.fetchall()

    arquivo = open('app.txt', 'w')
    
    arquivo.write("\nimport threading")

    i=1;
    for row in resposta :
        arquivo.write(f"\n\ndef executar{i}(servidor, componente, metrica):")
        arquivo.write("\n  import psutil")
        arquivo.write("\n  import mysql.connector")
        arquivo.write('\n  bdsql = mysql.connector.connect(host="localhost", user="root", password="TheKingBox751", database="appPython")')
        arquivo.write("\n  cursores = bdsql.cursor()")

        arquivo.write(f'\n  sql = ("SELECT comando FROM metrica WHERE idMetrica = %s")')
        arquivo.write(f"\n  val = (metrica, )")    
        arquivo.write(f"\n  cursores.execute(sql, val)")    

        arquivo.write(f"\n  comando = cursores.fetchall()")    
        arquivo.write(f"\n  leitura = eval(comando[0][0])")    

        arquivo.write(f'\n  sql = ("INSERT INTO leitura(fkServidor, fkComponente, fkMetrica, horario, valorLido) VALUES(%s, %s, %s, now(), %s)")')    
        arquivo.write(f'\n  val = (servidor, componente, metrica, leitura, )')    

        arquivo.write(f"\n  cursores.execute(sql, val)")
        arquivo.write(f"\n  bdsql.commit()")

        arquivo.write(f"\n\n\nthreading.Thread(target=executar{i}, args={row[0], row[1], row[2],}).start()")    

        i = i + 1
    arquivo.close()

    executavel = open('app.txt').read()

    exec(executavel)
    
if __name__ == '__main__':
    main()