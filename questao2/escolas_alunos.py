import sqlite3

# Função para criar a tabela 'escolas_alunos' no banco de dados 'escolas_alunos.db'
def criar_tabela_escolas_alunos():
    conn = sqlite3.connect('escolas_alunos.db')  # Conecta ao banco de dados 'escolas_alunos.db'
    cur = conn.cursor()  # Cria um cursor para interagir com o banco de dados
    cur.execute('''CREATE TABLE IF NOT EXISTS escolas_alunos (
                    id INTEGER PRIMARY KEY,
                    escola_id INTEGER,
                    aluno_id INTEGER,
                    FOREIGN KEY (escola_id) REFERENCES escolas(id),
                    FOREIGN KEY (aluno_id) REFERENCES alunos(id)
                )''')  # Cria a tabela 'escolas_alunos' se ela não existir
    conn.commit()  # Confirma as alterações no banco de dados
    conn.close()  # Fecha a conexão com o banco de dados

# Função para relacionar uma escola a um aluno na tabela 'escolas_alunos'
def relacionar_escola_aluno(escola_id, aluno_id):
    conn = sqlite3.connect('escolas_alunos.db')  # Conecta ao banco de dados 'escolas_alunos.db'
    cur = conn.cursor()  # Cria um cursor para interagir com o banco de dados
    cur.execute("INSERT INTO escolas_alunos (escola_id, aluno_id) VALUES (?, ?)", (escola_id, aluno_id))  # Insere os dados na tabela 'escolas_alunos'
    conn.commit()  # Confirma as alterações no banco de dados
    conn.close()  # Fecha a conexão com o banco de dados

# Chamando a função para criar a tabela 'escolas_alunos'
criar_tabela_escolas_alunos()

# Chamando a função para relacionar uma escola a um aluno
relacionar_escola_aluno(1, 1)

print("Dados inseridos na tabela 'escolas_alunos' com sucesso.")

# Conectando ao banco de dados 'escolas_alunos.db' para imprimir os dados da tabela 'escolas_alunos'
conn = sqlite3.connect('escolas_alunos.db')  # Conecta ao banco de dados 'escolas_alunos.db'
cur = conn.cursor()  # Cria um cursor para interagir com o banco de dados
cur.execute("SELECT * FROM escolas_alunos")  # Executa a consulta SQL para selecionar todos os dados da tabela 'escolas_alunos'
rows = cur.fetchall()  # Obtém todos os resultados da consulta
print("Dados na tabela 'escolas_alunos':")
for row in rows:
    print(row)
conn.close()  # Fecha a conexão com o banco de dados
