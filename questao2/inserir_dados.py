import pandas as pd
import sqlite3

# Função para criar a tabela perfil_educandos no banco de dados projeto.db
def criar_tabela_perfil_educandos():
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS perfil_educandos (
        coluna1 INTEGER,
        coluna2 TEXT,
        coluna3 TEXT
    )
    """
    try:
        conn = sqlite3.connect('projeto.db')  # Conecta ao banco de dados projeto.db
        cursor = conn.cursor()  # Cria um cursor para interagir com o banco de dados
        cursor.execute(sql_create_table)  # Executa o comando SQL para criar a tabela perfil_educandos
        conn.commit()  # Confirma as alterações no banco de dados
        print("Tabela perfil_educandos criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela perfil_educandos: {e}")
    finally:
        if conn:
            conn.close()  # Fecha a conexão com o banco de dados

# Função para criar a tabela escolas no banco de dados projeto.db
def criar_tabela_escolas():
    sql_create_table = """
    CREATE TABLE IF NOT EXISTS escolas (
        coluna1 INTEGER,
        coluna2 TEXT,
        coluna3 TEXT
    )
    """
    try:
        conn = sqlite3.connect('projeto.db')  # Conecta ao banco de dados projeto.db
        cursor = conn.cursor()  # Cria um cursor para interagir com o banco de dados
        cursor.execute(sql_create_table)  # Executa o comando SQL para criar a tabela escolas
        conn.commit()  # Confirma as alterações no banco de dados
        print("Tabela escolas criada com sucesso.")
    except sqlite3.Error as e:
        print(f"Erro ao criar a tabela escolas: {e}")
    finally:
        if conn:
            conn.close()  # Fecha a conexão com o banco de dados

# Função para carregar os dados de um arquivo CSV para uma tabela do banco de dados SQLite
def carregar_csv_para_sqlite(caminho, tabela):
    conn = None
    try:
        df = pd.read_csv(caminho, sep=';', encoding='latin1')  # Lê o arquivo CSV usando pandas
        conn = sqlite3.connect('projeto.db')  # Conecta ao banco de dados projeto.db
        df.to_sql(tabela, conn, if_exists='append', index=False)  # Insere os dados do DataFrame na tabela do banco de dados SQLite
        print(f"Dados do arquivo {caminho} inseridos na tabela {tabela}.")
    except FileNotFoundError:
        print(f"Erro: Arquivo não encontrado - {caminho}")
    except pd.errors.ParserError as e:
        print(f"Erro ao processar o arquivo {caminho}: {e}")
    except Exception as e:
        print(f"Erro inesperado ao processar o arquivo {caminho}: {e}")
    finally:
        if conn:
            conn.close()  # Fecha a conexão com o banco de dados

# Lista de caminhos para os arquivos CSV contendo os dados de perfil de educandos
perfil_educandos_files = [
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez17.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez18.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez19.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez20.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez21.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez22.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeraca-r33.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\dicionariopefileducando.xlsx",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeraca_r33.csv"
]

# Lista de caminhos para os arquivos CSV contendo os dados das escolas
escolas_files = [
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas122019.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas122020.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas122021.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas122021.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas122023.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas-dez-2010.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas-dez-2011.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas-dez-2012.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas-dez-2013.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas-dez-2014.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas-dez-2015.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolasr34.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolasr34dez2017.csv"
]

# Chamando as funções para criar as tabelas no banco de dados e carregar os dados dos arquivos CSV
criar_tabela_perfil_educandos()
criar_tabela_escolas()

for arquivo in perfil_educandos_files:
    carregar_csv_para_sqlite(arquivo, "perfil_educandos")

for arquivo in escolas_files:
    carregar_csv_para_sqlite(arquivo, "escolas")
