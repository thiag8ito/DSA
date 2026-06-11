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

print("\nIntroduzindo problemas nos dados para a limpeza...")

df_vendas.loc[5:10, 'Quantidade'] = np.nan
df_vendas.loc[20:22, 'Status_Entrega'] = np.nan
df_vendas.loc[30, 'Cliente_ID'] = np.nan

df_vendas = pd.concat([df_vendas, df_vendas.head(3)], ignore_index=True)

df_vendas['Preco_Unitario'] = df_vendas['Preco_Unitario'].astype(str)
df_vendas.loc[15, 'Preco_Unitario'] = 'valor_invalido'
df_vendas['Cliente_ID'] = df_vendas['Cliente_ID'].astype(str)

df_vendas.loc[50, 'Quantidade'] = 50

print("Dados gerados com sucesso!\n")

print(df_vendas.info())
print(df_vendas.isna().sum())
print(f"Numero de linhas duplicadas: {df_vendas.duplicated().sum()}")
print(df_vendas.describe())
print(df_vendas.describe(include=[object]))

df_limpo = df_vendas.copy()

print("Corrigindo tipos de dados...")

df_limpo['Preco_Unitario'] = pd.to_numeric(df_limpo['Preco_Unitario'], errors='coerce')
df_limpo['Cliente_ID'] = pd.to_numeric(df_limpo['Cliente_ID'], errors='coerce')
