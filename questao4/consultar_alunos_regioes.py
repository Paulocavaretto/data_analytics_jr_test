# Importando a biblioteca necessária
import sqlite3  # Biblioteca para trabalhar com bancos de dados SQLite

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('projeto.db')  # Conecta ao banco de dados 'projeto.db'

# Criando um cursor para executar consultas SQL
cur = conn.cursor()  # Cria um cursor para interagir com o banco de dados

# Consulta SQL para selecionar informações dos alunos e suas respectivas escolas
consulta_sql = """
SELECT alunos.nome AS nome_aluno, escolas.nome AS nome_escola, escolas.cep, escolas.latitude, escolas.longitude
FROM alunos
INNER JOIN escolas ON alunos.escola_id = escolas.id
WHERE escolas.cep LIKE '010%'  -- Filtra escolas pelo CEP iniciado com '010'
"""

# Executando a consulta SQL
cur.execute(consulta_sql)

# Obtendo todos os resultados da consulta
resultados = cur.fetchall()

# Iterando sobre os resultados e imprimindo cada linha
for linha in resultados:
    print(linha)

# Fechando o cursor e a conexão com o banco de dados
cur.close()  # Fecha o cursor
conn.close()  # Fecha a conexão com o banco de dados
