CREATE DATABASE appPython;
USE appPython;

# DROP DATABASE appPython;

CREATE TABLE servidor(
	id CHAR(17) PRIMARY KEY
);

SELECT * FROM servidor;

INSERT INTO servidor VALUES();

CREATE TABLE componente(
	idComponente INT PRIMARY KEY AUTO_INCREMENT
    ,fkServidor CHAR(17)
    ,tipoComponente VARCHAR(25)
    ,FOREIGN KEY (fkServidor) REFERENCES servidor(id)
);

INSERT INTO componente(fkServidor, tipoComponente)
	VALUES('0c:9d:92:00:02:b5', "CPU")
    ,('0c:9d:92:00:02:b5', "DISCO")
    ,('0c:9d:92:00:02:b5', "RAM");

CREATE TABLE metrica(
	idMetrica INT PRIMARY KEY AUTO_INCREMENT
    ,nomeMetrica VARCHAR(50)
    ,comando VARCHAR(75)
    ,unidadeMedida VARCHAR(50)
    ,tipoComponente VARCHAR(50)
    ,isTupla INT
);

INSERT INTO metrica(nomeMetrica, comando, unidadeMedida, tipoComponente, isTupla)
	VALUES("CPU Percent", "psutil.cpu_percent()", "%", "CPU", 0)
    ,("CPU Percent por core", "psutil.cpu_percent(interval=1, percpu=True)", "%", "CPU", 1)
    ,("Disco percent", "psutil.disk_usage('/').percent", "%", "DISCO", 0)
    ,("RAM Percent", "psutil.virtual_memory().percent", "%", "RAM", 0);

CREATE TABLE parametro(
	fkServidor CHAR(17)
    ,fkComponente INT
    ,fkMetrica INT
    ,FOREIGN KEY (fkServidor) REFERENCES servidor(id)
    ,FOREIGN KEY (fkComponente) REFERENCES componente(idComponente)
    ,FOREIGN KEY (fkMetrica) REFERENCES metrica(idMetrica)
);

INSERT INTO parametro(fkServidor, fkComponente, fkMetrica)
	VALUES('0c:9d:92:00:02:b5', 1, 1)
    ,('0c:9d:92:00:02:b5', 1, 2)
    ,('0c:9d:92:00:02:b5', 2, 3)
    ,('0c:9d:92:00:02:b5', 3, 4);

CREATE TABLE leitura(
	idLeitura INT AUTO_INCREMENT
    ,fkServidor CHAR(17)
    ,fkComponente INT
    ,fkMetrica INT
    ,horario DATETIME
    ,valorLido DECIMAL(8,2)
    ,FOREIGN KEY (fkServidor) REFERENCES servidor(id)
    ,FOREIGN KEY (fkComponente) REFERENCES componente(idComponente)
    ,FOREIGN KEY (fkMetrica) REFERENCES metrica(idMetrica)
    ,PRIMARY KEY(idLeitura, fkServidor, fkComponente, fkMetrica, horario)
);

SELECT * FROM leitura;

CREATE VIEW medicoes AS
	SELECT fkComponente, tipoComponente, valorLido, horario FROM leitura
    INNER JOIN componente ON fkComponente = idComponente
    ORDER BY fkComponente;
    
SELECT * FROM medicoes;