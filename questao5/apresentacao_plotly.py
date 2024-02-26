# Importando as bibliotecas necessárias
import plotly.graph_objects as go  # Biblioteca para criar gráficos personalizados
import plotly.express as px  # Biblioteca para criar gráficos expressivos com menos código

# Definindo os dados
escolas = ['Escola A', 'Escola B', 'Escola C']  # Nomes das escolas
alunos_por_escola = [250, 300, 200]  # Número de alunos por escola
generos = ['Masculino', 'Feminino']  # Gêneros dos alunos
distribuicao_genero = [400, 350]  # Número de alunos por gênero

# Criando o gráfico de barras
fig1 = go.Figure([go.Bar(x=escolas, y=alunos_por_escola)])  # Cria um gráfico de barras com os dados das escolas e quantidade de alunos
fig1.update_layout(title='Quantidade de Alunos por Escola',  # Adiciona título ao gráfico
                   xaxis_title='Escola',  # Adiciona rótulo ao eixo x
                   yaxis_title='Quantidade de Alunos')  # Adiciona rótulo ao eixo y

# Criando o gráfico de pizza
fig2 = px.pie(values=distribuicao_genero, names=generos, title='Distribuição de Gênero dos Alunos')  # Cria um gráfico de pizza com os dados de distribuição de gênero

# Mostrando os gráficos
fig1.show()  # Mostra o gráfico de barras
fig2.show()  # Mostra o gráfico de pizza
