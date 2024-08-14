-- CRIAÇÃO DAS TABELAS 'REGIAO', 'VINICOLA' E 'VINHO'
CREATE TABLE mydb.Regiao (
codRegiao BIGINT PRIMARY KEY, 
nomeRegiao VARCHAR(100) NOT NULL,
descricaoRegiao TEXT
);

CREATE TABLE mydb.Vinicola (
codVinicola BIGINT PRIMARY KEY,
nomeVinicola VARCHAR(100) NOT NULL,
descricaoVinicola TEXT,
foneVinicola VARCHAR(15),
emailVinicola VARCHAR(15),
codRegiao BIGINT NOT NULL, 
FOREIGN KEY (codRegiao) REFERENCES mydb.Regiao(codRegiao)
);

CREATE TABLE mydb.Vinho (
codVinho BIGINT PRIMARY KEY,
nomeVinho VARCHAR(50) NOT NULL,
tipoVinho VARCHAR(30) NOT NULL,
anoVinho INT NOT NULL,
descricaoVinho TEXT, 
codVinicola BIGINT NOT NULL,
FOREIGN KEY (codVinicola) REFERENCES mydb.Vinicola(codVinicola)
);

-- CRIAÇÃO DOS INSERTS NAS TABELAS
INSERT INTO mydb.Regiao (codRegiao, nomeRegiao, descricaoRegiao)
VALUES
(1, 'Região Norte', 'Descrição da Região Norte'),
(2, 'Região Nordeste', 'Descrição da Região Nordeste'),
(3, 'Região Centro-Oeste', 'Descrição da Região Centro-Oeste'),
(4, 'Região Sudeste', 'Descrição da Região Sudeste'),
(5, 'Região Sul', 'Descrição da Região Sul');

INSERT INTO mydb.Vinicola (codVinicola, nomeVinicola, descricaoVinicola, foneVinicola, emailVinicola, codRegiao)
VALUES
(200, 'Vinícola A', 'Descrição da Vinícola A', '(00) 1234-5678', 'vinA@mail.com', 1),
(201, 'Vinícola B', 'Descrição da Vinícola B', '(00) 9876-5432', 'vinB@mail.com', 2),
(202, 'Vinícola C', 'Descrição da Vinícola C', '(00) 5555-4444', 'vinC@mail.com', 3),
(203, 'Vinícola D', 'Descrição da Vinícola D', '(00) 9999-8888', 'vinD@mail.com', 4),
(204, 'Vinícola E', 'Descrição da Vinícola E', '(00) 7777-6666', 'vinE@mail.com', 5);

INSERT mydb.Vinho (codVinho, nomeVinho, tipoVinho, anoVinho, descricaoVinho, codVinicola)
VALUES
('1', 'Vinho Tinto', 'Tinto', '2019', 'Feito de uvas Malbec, com teor alcóolico de 13%.', '200'),
('2', 'Vinho Branco', 'Branco', '2019', 'Branco refrescante com acidez marcante', '201'),
('3', 'Vinho Rosé', 'Rosé', '2021', 'Frutado e refrescante com notas de frutas vermelhas frescas', '202'),
('4', 'Vinho Espumante', 'Espumante Branco', '2018', 'Vinho com notas de frutas cítricas, frutas secas, flores brancas e pães', '203'),
('5', 'Vinho Fortificado', 'Fortificado', '2015', 'Vinho marcante, com teor alcóolico de 16%', '204');

-- CONSULTA DOS DADOS PEDIDOS NO ITEM 2 E 3
SELECT nomeVinho AS 'Vinho', anoVinho AS 'Ano', nomeVinicola AS 'Vinícola', nomeRegiao AS 'Região'
FROM mydb.Vinho 
INNER JOIN mydb.Vinicola ON Vinho.codVinicola = Vinicola.codVinicola
INNER JOIN mydb.Regiao ON Vinicola.codRegiao = Regiao.codRegiao;

-- CRIAÇÃO DO USUÁRIO 'SOMMELIER'
CREATE USER 'sommelier' IDENTIFIED BY '123456'
	WITH MAX_QUERIES_PER_HOUR 40
		 MAX_CONNECTIONS_PER_HOUR 60;
GRANT SELECT ON mydb.Vinho TO 'sommelier';
GRANT SELECT (codVinicola, nomeVinicola) ON mydb.Vinicola TO 'sommelier';