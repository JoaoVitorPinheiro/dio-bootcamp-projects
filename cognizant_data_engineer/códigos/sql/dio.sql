CREATE TABLE pessoas (
    id INT NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(255) NOT NULL,
    nascimento DATE
)

INSERT INTO pessoas (nome, nascimento) VALUES ('Mbappe', '2000-09-15')
INSERT INTO pessoas (nome, nascimento) VALUES ('Neymar', '1993-05-22')
INSERT INTO pessoas (nome, nascimento) VALUES ('Messi', '1985-01-10')
