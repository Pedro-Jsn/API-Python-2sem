CREATE DATABASE appPython;
USE appPython;

CREATE TABLE servidor(
	id INT PRIMARY KEY AUTO_INCREMENT
);

INSERT INTO servidor VALUES();

CREATE TABLE componente(
	idComponente INT PRIMARY KEY AUTO_INCREMENT
    ,fkServidor INT
    ,tipoComponente VARCHAR(25)
    ,FOREIGN KEY (fkServidor) REFERENCES servidor(id)
);

INSERT INTO componente(fkServidor, tipoComponente)
	VALUES(1, "CPU")
    ,(1, "CPU")
    ,(1, "RAM");

CREATE TABLE metrica(
	idMetrica INT PRIMARY KEY AUTO_INCREMENT
    ,nomeMetrica VARCHAR(50)
    ,comando VARCHAR(75)
    ,unidadeMedida VARCHAR(50)
    ,tipoComponente VARCHAR(50)
);

INSERT INTO metrica(nomeMetrica, comando, unidadeMedida, tipoComponente)
	VALUES("CPU Percent", "psutil.cpu_percent()", "%", "CPU")
    ,("CPU Percent por core", "psutil.cpu_percent(interval=1, percpu=True)", "%", "CPU")
    ,("RAM Percent", "psutil.virtual_memory().percent", "%", "RAM");

CREATE TABLE parametro(
	fkServidor INT
    ,fkComponente INT
    ,fkMetrica INT
    ,isTupla INT
    ,FOREIGN KEY (fkServidor) REFERENCES servidor(id)
    ,FOREIGN KEY (fkComponente) REFERENCES componente(idComponente)
    ,FOREIGN KEY (fkMetrica) REFERENCES metrica(idMetrica)
);

INSERT INTO parametro(fkServidor, fkComponente, fkMetrica, isTupla)
	VALUES(1, 1, 1, 0)
    ,(1, 2, 2, 1)
    ,(1, 3, 3, 0);

CREATE TABLE leitura(
	idLeitura INT AUTO_INCREMENT
    ,fkServidor INT
    ,fkComponente INT
    ,fkMetrica INT
    ,horario DATETIME
    ,valorLido DECIMAL(8,2)
    ,FOREIGN KEY (fkServidor) REFERENCES servidor(id)
    ,FOREIGN KEY (fkComponente) REFERENCES componente(idComponente)
    ,FOREIGN KEY (fkMetrica) REFERENCES metrica(idMetrica)
    ,PRIMARY KEY(idLeitura, fkServidor, fkComponente, fkMetrica, horario)
);