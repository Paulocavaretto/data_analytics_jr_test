# Importando a biblioteca necessária
import sqlite3  # Biblioteca para trabalhar com bancos de dados SQLite

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('projeto.db')  # Conecta ao banco de dados 'projeto.db'
cursor = conn.cursor()  # Cria um cursor para interagir com o banco de dados

# Criando a tabela perfil_educandos, se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS perfil_educandos (
        id INTEGER PRIMARY KEY,
        matricula_aluno TEXT,
        nome_aluno TEXT
    )
''')

# Criando a tabela escolas, se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS escolas (
        id INTEGER PRIMARY KEY,
        codigo_escola TEXT,
        nome_escola TEXT
    )
''')

# Confirmando as alterações no banco de dados
conn.commit()

# Fechando a conexão com o banco de dados
conn.close()  # Fecha a conexão com o banco de dados
