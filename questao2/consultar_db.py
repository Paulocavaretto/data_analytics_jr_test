# Importando a biblioteca necessária
import sqlite3  # Biblioteca para trabalhar com bancos de dados SQLite

# Conectando ao banco de dados SQLite
conn = sqlite3.connect('projeto.db')  # Conecta ao banco de dados 'projeto.db'
cursor = conn.cursor()  # Cria um cursor para interagir com o banco de dados

# Executando a consulta SQL para obter dados da tabela perfil_educandos
cursor.execute('SELECT * FROM perfil_educandos')  # Executa a consulta SQL
dados_perfil_educandos = cursor.fetchall()  # Obtém todos os resultados da consulta

# Imprimindo os dados da tabela perfil_educandos
print("Dados da tabela perfil_educandos:")
for linha in dados_perfil_educandos:
    print(linha)

# Executando a consulta SQL para obter dados da tabela escolas
cursor.execute('SELECT * FROM escolas')  # Executa a consulta SQL
dados_escolas = cursor.fetchall()  # Obtém todos os resultados da consulta

# Imprimindo os dados da tabela escolas
print("\nDados da tabela escolas:")
for linha in dados_escolas:
    print(linha)

# Fechando a conexão com o banco de dados
conn.close()  # Fecha a conexão com o banco de dados
