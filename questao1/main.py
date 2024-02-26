# Importando as bibliotecas necessárias
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import pandas as pd

# Lista de caminhos para os arquivos CSV contendo dados das escolas e dos alunos
escolas_files = [
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas122019.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Escolas\escolas122020.csv",
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

perfil_educandos_files = [
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez17.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez18.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez19.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez20.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez21.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez22.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeracadez23.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\dicionariopefileducando.csv",
    r"C:\Users\Paulo\OneDrive\Documentos\Projeto\Data\Perfil dos educandos\idadeserieneeraca_r33.csv"
]

# Criando uma engine para conectar ao banco de dados SQLite 'test_analytics.db'
engine = create_engine('sqlite:///test_analytics.db')

# Criando um objeto Metadata para armazenar as informações sobre as tabelas
metadata = MetaData()

# Definindo a estrutura da tabela 'escolas'
escolas_table = Table('escolas', metadata,
    Column('id', Integer, primary_key=True),  # Coluna de identificação única
    Column('nome', String),  # Coluna de nome da escola
)

# Definindo a estrutura da tabela 'alunos'
alunos_table = Table('alunos', metadata,
    Column('id', Integer, primary_key=True),  # Coluna de identificação única
    Column('nome', String),  # Coluna de nome do aluno
)

# Criando as tabelas no banco de dados
metadata.create_all(engine)

# Loop para ler cada arquivo de escolas e inserir os dados na tabela 'escolas'
for file_path in escolas_files:
    try:
        # Lendo o arquivo CSV usando pandas
        df = pd.read_csv(file_path, encoding='latin1')
        # Inserindo os dados na tabela 'escolas' do banco de dados
        df.to_sql('escolas', con=engine, if_exists='append', index=False)
    except pd.errors.ParserError as e:
        # Em caso de erro ao ler o arquivo, imprime uma mensagem de erro
        print(f"Erro ao ler o arquivo {file_path}: {e}")
        continue 

# Loop para ler cada arquivo de alunos e inserir os dados na tabela 'alunos'
for file_path in perfil_educandos_files:
    try:
        # Lendo o arquivo CSV usando pandas
        df = pd.read_csv(file_path, encoding='latin1')
        # Inserindo os dados na tabela 'alunos' do banco de dados
        df.to_sql('alunos', con=engine, if_exists='append', index=False)
    except pd.errors.ParserError as e:
        # Em caso de erro ao ler o arquivo, imprime uma mensagem de erro
        print(f"Erro ao ler o arquivo {file_path}: {e}")
        continue  
