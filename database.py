import sqlite3

conn = sqlite3.connect("CEP.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS CEP(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cep VARCHAR(20) NOT NULL,
    logradouro VARCHAR(50),
    complemento VARCHAR(50),
    bairro VARCHAR(50),
    cidade VARCHAR(20),
    uf VARCHAR(5),
    estado VARCHAR(20),
    regiao VARCHAR(20),
    ibge VARCHAR(20),
    gia VARCHAR(20),
    ddd VARCHAR(5),
    siafi VARCHAR(20),
    UNIQUE(cep)
)
''')

conn.commit()

