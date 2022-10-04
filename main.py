import threading
from time import sleep

def main():
    from getmac import get_mac_address as macaddress

    enderecoMac = macaddress()
    bdsql, mycursor = conectar()
    
    query = ('SELECT * FROM servidor WHERE id = %s')
    params = (enderecoMac, )
    mycursor.execute(query, params)

    resposta = mycursor.fetchall()

    if(len(resposta) > 0):
        selecionarParametro(mycursor, enderecoMac)
    else :
        cadastrarServidor(bdsql, mycursor, enderecoMac)

def cadastrarServidor(bdsql, cursor, mac):
    query = ("INSERT INTO servidor(id) VALUES (%s)")
    params = (mac,)
    cursor.execute(query, params)

    bdsql.commit()

def selecionarParametro(cursor, mac):

    query = ("SELECT * from parametro WHERE fkServidor = %s")
    params = (mac, )
    cursor.execute(query, params)

    resposta = cursor.fetchall()

    if(len(resposta) > 0):
        executarMonitoramento(resposta)
    else:
        print("Nenhuma componente cadastrado para monitoramento, cadastre na sua dashboard!")
        sleep(3)

def executarMonitoramento(resposta):
    while True:
        script = """
import threading   
        """

        i=1
        for row in resposta:
            script += f"""
def executar_{i}(servidor, componente, metrica):
    import psutil
    bdsql, cursores = conectar()

    query = ("SELECT comando, isTupla FROM metrica WHERE idMetrica = %s")
    val = (metrica, )    
    cursores.execute(query, val)    

    resposta = cursores.fetchall() # resposta retorna isto [(comando, isTupla)]
    isTupla = resposta[0][1]

    comando = resposta[0][0]    
    leitura = eval(comando)    

    if isTupla == 0:
        query = ("INSERT INTO leitura(fkServidor, fkComponente, fkMetrica, horario, valorLido) VALUES(%s, %s, %s, now(), %s)")    
        val = (servidor, componente, metrica, leitura, )
            
        cursores.execute(query, val)
        bdsql.commit()
    else: 
        for row in leitura:
            query = ("INSERT INTO leitura(fkServidor, fkComponente, fkMetrica, horario, valorLido) VALUES(%s, %s, %s, now(), %s)")    
            val = (servidor, componente, metrica, row, )  

            cursores.execute(query, val)
            bdsql.commit()

threading.Thread(target=executar_{i}, args=('{row[0]}', {row[1]}, {row[2]},)).start()
    """
        i += 1
        if script != None:
            exec(script)

        sleep(10)
        print("Executando...")


def conectar():
    import mysql.connector

    bdsql = mysql.connector.connect(host="localhost", user="root", password="TheKingBox751", database="appPython")
    mycursor = bdsql.cursor()

    return (bdsql, mycursor)

if __name__ == '__main__':
    main()