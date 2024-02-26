# Importando a biblioteca necessária
import pandas as pd  # Biblioteca para trabalhar com estruturas de dados e análise de dados

# Definindo os caminhos para os arquivos CSV
caminho_perfil_educandos = "caminho_completo_para_o_arquivo_perfil_educandos.csv"
caminho_escolas = "caminho_completo_para_o_arquivo_escolas.csv"
caminho_alunos = "caminho_completo_para_o_arquivo_alunos.csv"

# Lendo os arquivos CSV e armazenando os dados em DataFrames do Pandas
perfil_educandos = pd.read_csv(caminho_perfil_educandos)  # DataFrame com os dados do perfil dos educandos
escolas = pd.read_csv(caminho_escolas)  # DataFrame com os dados das escolas
alunos = pd.read_csv(caminho_alunos)  # DataFrame com os dados dos alunos
