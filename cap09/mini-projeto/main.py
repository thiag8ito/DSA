import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)

data = {
    'ID_Pedido': range(1001, 1101),
    'Data_Compra': pd.to_datetime(pd.date_range(start = '2026-07-01', periods = 100, freq = 'D')) - pd.to_timedelta(np.random.randint(0, 30, size=100), unit='D'),
    'Cliente_ID': np.random.randint(100, 150, size = 100),
    'Produto': np.random.choice(['Smartphone', 'Notebook', 'Fone de Ouvido', 'Smatwatch', 'Teclado Mecanico'], size=100),
    'Categoria': ['Eletrônicos', 'Eletrônicos', 'Acessórios', 'Acessórios', 'Acessórios'] * 20,
    'Quantidade': np.random.randint(1, 5, size = 100),
    'Preco_Unitario': [5999.90, 8500.00, 799.50, 2100.00, 850.00] * 20,
    'Status_Entrega': np.random.choice(['Entregue', 'Pendente', 'Cancelado'], size=100, p=[0.8, 0.15, 0.05])
}

df_vendas = pd.DataFrame(data)

print("\nIntroduzindo problemas nos dados para a limpeza...\n")

df_vendas.loc[5:10, 'Quantidade'] = np.nan
df_vendas.loc[20:22, 'Status_Entrega'] = np.nan
df_vendas.loc[30, 'Cliente_ID'] = np.nan


df_vendas = pd.concat([df_vendas, df_vendas.head(3)], ignore_index=True)

df_vendas['Preco_Unitario'] = df_vendas['Preco_Unitario'].astype(str)
df_vendas.loc[15, 'Preco_Unitario'] = 'valor_invalido'
df_vendas['Cliente_ID'] = df_vendas['Cliente_ID'].astype(str)

df_vendas.loc[50, 'Quantidade'] = 50

print("Dados gerados com sucesso!\n")

print(df_vendas.isna().sum())

print(f"numero de linhas duplicadas: {df_vendas.duplicated().sum()}")
print(df_vendas.describe()) 

print(df_vendas.describe(include=[object]))

df_limpo = df_vendas.copy()

print("Corrigindo tipos de dados...")

df_limpo['Preco_Unitario'] = pd.to_numeric(df_limpo['Preco_Unitario'], errors='coerce')

df_limpo['Cliente_ID'] = pd.to_numeric(df_limpo['Cliente_ID'], errors='coerce').astype('Int64') # type: ignore

print(df_limpo.dtypes) 

print("Tratando valores ausentes")
mediana_qtd = df_limpo['Quantidade'].mean()
df_limpo.fillna({'Quantidade': mediana_qtd}, inplace = True)

moda_status = df_limpo['Status_Entrega'].mode()[0]
df_limpo['Status_Entrega'] = df_limpo['Status_Entrega'].fillna(moda_status)

df_limpo.dropna(subset=['Preco_Unitario', 'Cliente_ID'], inplace=True)

print("Removendo registros duplicados")
df_limpo.drop_duplicates(inplace=True)

print("Tratando outliers")
sns.boxplot(x=df_limpo['Quantidade'])
plt.title('Boxplot de Quantidade (Antes de tratar outlier)')
plt.show()

limite_superior = df_limpo['Quantidade'].mean() + 3 * df_limpo['Quantidade'].std()
df_limpo = df_limpo[df_limpo['Quantidade'] < limite_superior]

sns.boxplot(x=df_limpo['Quantidade'])
plt.title('Boxplot de Quantidade (Depois de tratar outlier)')
plt.show()

#Verificação final
print("\n--- Verificação Final Pós-Limpeza ---")
print(df_limpo.info())

print(df_limpo.head())

df_limpo['Total_Venda'] = df_limpo['Quantidade'] * df_limpo['Preco_Unitario']

print(df_limpo.head())

#1. Receita total
receita_total = df_limpo['Total_Venda'].sum()
print(f"\nReceita Total: R$ {receita_total:.2f}")

#2. Qual a receita total por categoria de produto?
receita_por_categoria = df_limpo.groupby('Categoria')['Total_Venda'].sum().sort_values(ascending=False)
print("\nReceita Total por Categoria:")
print(receita_por_categoria)

#3. Qual o produto mais vendido em quantidade?
produto_mais_vendido = df_limpo.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)
print("\nProduto mais vendido em quantidade:")
print(produto_mais_vendido)

#4. analise de venda ao longo do tempo
vendas_por_dia = df_limpo.set_index('Data_Compra').resample('D')['Total_Venda']
print("\nResumo de VEndas por dia (5 primeiros dias):")
print(vendas_por_dia.head())

#VISUALIZAÇÃO DOS DADOS PARA ANALISE    
receita_por_categoria.plot(kind='bar', color='skyblue')
plt.title('Receita Total por Categoria de Produto')
plt.xlabel('Categoria')
plt.ylabel('Receita Total')
plt.xticks(rotation=0)
plt.show()

#Grafico 2. Quantidade vendida por produto
produto_mais_vendido.plot(kind='barh', color='salmon')
plt.title('Produto mais vendido em quantidade')
plt.xlabel('Quantidade Vendida')
plt.ylabel('Produto')
plt.gca().invert_yaxis()
plt.show()

# Gráfico 3: Tendência de Vendas ao Longo do Tempo
vendas_por_dia.plot(kind = 'line', marker = '.', linestyle = '-')
plt.title('Tendência de Vendas Diárias')
plt.xlabel('Data da Compra')
plt.ylabel('Receita (R$)')
plt.grid(True)
plt.show()

# Gráfico 4: Distribuição do Status de Entrega

# Conta quantas vezes aparece cada status de entrega
status_counts = df_limpo['Status_Entrega'].value_counts()

plt.pie(
    status_counts,                 # Valores numéricos para cada fatia (quantidade de cada status)
    labels = status_counts.index,  # Rótulos de cada fatia (labels dos status)
    autopct = '%1.1f%%',           # Mostra o percentual em cada fatia com 1 casa decimal 
    startangle = 180,              # Ângulo inicial para "girar" o gráfico e escolher onde começa a primeira fatia
    colors = ['lightgreen',        # Cor da primeira fatia
              'orange',            # Cor da segunda fatia
              'lightcoral']        # Cor da terceira fatia
)

plt.title('\nDistribuição do Status de Entrega')  # Título do gráfico
plt.show()                                         # Exibe o gráfico na tela

# Gráfico 4: Distribuição do Status de Entrega no formato 3D

# Conta quantas vezes aparece cada status de entrega
status_counts = df_limpo['Status_Entrega'].value_counts()

# Descobre a posição (índice) da fatia com maior valor para destacá-la
maior_idx = status_counts.argmax()

# Cria a lista explode: desloca 0.1 para a maior fatia e 0 para as outras
explode = [0.1 if i == maior_idx else 0 for i in range(len(status_counts))]

# Define o tamanho da figura (6x6 polegadas)
plt.figure(figsize = (6,6))

plt.pie(
    status_counts,                 # Valores numéricos para cada fatia (quantidade de cada status)
    labels = status_counts.index,  # Rótulos de cada fatia (nomes dos status)
    autopct = '%1.1f%%',           # Mostra o percentual em cada fatia com 1 casa decimal 
    startangle = 180,              # Ângulo inicial para "girar" o gráfico e definir onde começa a primeira fatia
    colors = ['lightgreen',        # Cor da primeira fatia
              'orange',            # Cor da segunda fatia
              'lightcoral'],       # Cor da terceira fatia
    explode = explode,             # Desloca a maior fatia para destacá-la visualmente
    shadow = True                  # Adiciona sombra para criar um efeito 3D simples
)

plt.title('\nDistribuição do Status de Entrega\n')  # Define o título do gráfico
plt.axis('equal')                                   # Mantém o formato circular (sem deformações)
plt.show()                                          # Exibe o gráfico

# Gráfico 4: Distribuição dos Status de Entrega com gráfico interativo usando o Plotly

# Importa o pacote Plotly Express para gráficos interativos
import plotly.express as px  

# Cria o gráfico de pizza interativo
dsa_fig = px.pie(
    values = status_counts,        # Valores numéricos para cada fatia (quantidade de cada status)
    names = status_counts.index,   # Rótulos de cada fatia (nomes dos status)
    hole = 0,                      # Define o tamanho do "furo" no centro (0 = pizza completa, >0 cria gráfico do tipo donut)
    title = 'Distribuição do Status de Entrega'  # Título exibido no gráfico
)

# Ajusta o destaque das fatias (pull desloca as fatias para fora)
dsa_fig.update_traces(
    pull = [0.05 if i == maior_idx else 0 for i in range(len(status_counts))]
    # Cria uma lista onde a maior fatia é deslocada 0.05 e as outras ficam sem deslocamento
)

# Mostra o gráfico interativo na tela
dsa_fig.show()