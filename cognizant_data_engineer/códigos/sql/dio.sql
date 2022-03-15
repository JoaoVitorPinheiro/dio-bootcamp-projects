CREATE TABLE pessoas (
    id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    nascimento DATE
)

INSERT INTO pessoas (nome, nascimento) VALUES ('Mbappe', '2000-09-15')
INSERT INTO pessoas (nome, nascimento) VALUES ('Neymar', '1993-05-22')
INSERT INTO pessoas (nome, nascimento) VALUES ('Messi', '1985-01-10')

UPDATE pessoas SET nome = 'Ney JR' WHERE id = 2;

DELETE FROM pessoas WHERE id = 3;

INSERT INTO pessoas (nome, nascimento) VALUES ('João Vitor', '1998-09-15');

SELECT * FROM pessoas ORDER BY nome;

SELECT * FROM pessoas ORDER BY nascimento DESC;

ALTER TABLE pessoas ADD posicao VARCHAR(15) NOT NULL BEFORE nascimento;

UPDATE pessoas SET posicao = 'ATACANTE' WHERE id = 1;
UPDATE pessoas SET posicao = 'ATACANTE' WHERE id = 2;

SELECT COUNT(id), posicao FROM pessoa GROUP BY posicao;

