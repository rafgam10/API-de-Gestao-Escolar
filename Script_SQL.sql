CREATE TABLE IF NOT EXISTS alunos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    matricula TEXT NOT NULL UNIQUE,
    data_nascimento DATE NOT NULL,
    status INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS professor(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    cpf TEXT NOT NULL UNIQUE,
    especialidade TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS disciplina(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    carga_horaria INTEGER NOT NULL,
    professor_id INTEGER NOT NULL,
    FOREIGN KEY (professor_id) REFERENCES professor(id)
);

CREATE TABLE IF NOT EXISTS matricula(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    aluno_id INTEGER NOT NULL,
    disciplina_id INTEGER NOT NULL,
    ano_letivo INTEGER NOT NULL,
    status INTEGER NOT NULL,
    FOREIGN KEY (aluno_id) REFERENCES alunos(id),
    FOREIGN KEY (disciplina_id) REFERENCES disciplina(id)
);

CREATE TABLE IF NOT EXISTS nota(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula_id INTEGER NOT NULL,
    bimestre INTEGER NOT NULL CHECK (bimestre BETWEEN 1 AND 4),
    nota REAL NOT NULL CHECK (nota BETWEEN 0 AND 10),
    FOREIGN KEY (matricula_id) REFERENCES matricula(id)
);

CREATE TABLE IF NOT EXISTS frequencia(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matricula_id INTEGER NOT NULL,
    data DATE NOT NULL,
    presente INTEGER NOT NULL CHECK (presente IN (0,1)),
    FOREIGN KEY (matricula_id) REFERENCES matricula(id),
    UNIQUE (matricula_id, data)
);
