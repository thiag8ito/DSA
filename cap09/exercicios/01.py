import pandas as pd
import numpy as np

#__________EXERCICIO 1__________________________________
# Dados de exemplo
dados = {'Nome': ['Ana', 'Bruno', 'Carla', 'Matias', 'Eliana', 'Fabiano'],
         'Departamento': ['RH', 'Vendas', 'TI', 'Vendas', 'RH', 'Vendas'],
         'Salário': [4000, 5000, 6200, 4400, 4300, 5500]}

df_funcionarios = pd.DataFrame(dados)

condicao_depto = df_funcionarios['Departamento'] == 'Vendas'
condicao_salario = df_funcionarios['Salário'] > 4500

funcionarios_condicao = df_funcionarios[condicao_depto & condicao_salario]
print(f"Resposta ex 1.: \n{funcionarios_condicao}")


#_________EXERCICIO 2__________________________________
print("\n--- Exercício 2 ---\n")
# Dados de exemplo
dados_vendas = {'Categoria': ['Eletrônicos', 'Vestuário', 'Eletrônicos', 'Casa', 'Vestuário', 'Eletrônicos'],
                'Produto': ['TV', 'Camiseta', 'Notebook', 'Sofá', 'Calça', 'Celular'],
                'Valor': [2500, 80, 4500, 1500, 120, 3000]}

df_vendas = pd.DataFrame(dados_vendas)

vendas_por_categoria = df_vendas.groupby('Categoria')['Valor'].sum()
print(f"Resposta ex 2.: \n{vendas_por_categoria}")


#__________EXERCICIO 3__________________________________
print("\n--- Exercício 3 ---\n")

# Dados de exemplo
dados_produtos = {'Produto': ['Monitor', 'Teclado', 'Mouse', 'Webcam'],
                  'Preco': [800, 120, 70, 250]}

df_produtos = pd.DataFrame(dados_produtos)

df_produtos['Preco_com_Desconto'] = df_produtos['Preco'] * 0.9
print(f"Resposta ex 3.: \n{df_produtos}")


#__________EXERCICIO 4__________________________________
print("\n--- Exercício 4 ---\n")

# Dados de exemplo
dados_alunos = {'Aluno': ['Alice', 'Bernardo', 'Clara', 'Marcelo'],
                'Nota': [8.5, 7.0, np.nan, 9.0]}

df_alunos = pd.DataFrame(dados_alunos)

media_alunos = df_alunos['Nota'].mean()
df_alunos['Nota'] = df_alunos['Nota'].fillna(media_alunos)
print(f"Resposta ex 4.: \n{df_alunos}")


#__________EXERCICIO 5__________________________________
print("\n--- Exercício 5 ---\n")

# Dados de exemplo
dados_pontuacao = {'Jogador': ['J1', 'J2', 'J3', 'J4', 'J5'],
                   'Pontos': [88, 95, 74, 102, 95]}

df_pontuacao = pd.DataFrame(dados_pontuacao)

df_ordenado = df_pontuacao.sort_values(by=['Pontos'], ascending=False)
print(f"Resposta ex 5.: \n{df_ordenado}")


#__________EXERCICIO 6__________________________________
print("\n--- Exercício 6 ---\n")

# Dados de exemplo
df_clientes = pd.DataFrame({'ID_Cliente': [1, 2, 3],
                            'Nome': ['Carlos', 'Mariana', 'Lucas']})

# Dados de exemplo
df_pedidos = pd.DataFrame({'ID_Pedido': [101, 102, 103],
                           'ID_Cliente': [2, 1, 2],
                           'Produto': ['Livro', 'Caneta', 'Caderno']})

df_merged = pd.merge(df_clientes, df_pedidos, on='ID_Cliente')

print(f"Resposta ex 6.: \n{df_merged}")


#__________EXERCICIO 7__________________________________
print("\n--- Exercício 7 ---\n")

# Dados de exemplo
dados_eventos = {'Evento': ['Conferência A', 'Workshop B', 'Feira C'],
                 'Data': ['2025-10-25', '2026-03-12', '2026-09-01']}

df_eventos = pd.DataFrame(dados_eventos)

df_eventos['Ano'] = pd.to_datetime(df_eventos['Data']).dt.year

print(f"Resposta ex 7.: \n{df_eventos}")


#__________EXERCICIO 8__________________________________
print("\n--- Exercício 8 ---\n")

df_notas = pd.DataFrame({'Aluno': ['Maria', 'Jeremias', 'Paulo', 'Roberto'],
                         'Nota': [9.5, 6.0, 5.5, 8.0]})

df_notas['Status'] = df_notas['Nota'].apply(lambda nota: 'Aprovado' if nota >= 7 else 'Reprovado')

print(f"Resposta ex 8.: \n{df_notas}")


#__________EXERCICIO 9__________________________________
print("\n--- Exercício 9 ---\n")

df_regional = pd.DataFrame({'Regiao': ['Norte', 'Sul', 'Norte', 'Sul', 'Norte', 'Sul'],
                            'Vendedor': ['Ana', 'Bruno', 'Ana', 'Carlos', 'Carlos', 'Bruno'],
                            'Vendas': [1000, 1500, 1200, 1800, 800, 1300]})

tabela_dinamica = df_regional.pivot_table(index='Regiao',
                                          columns='Vendedor',
                                          values='Vendas',
                                          aggfunc='sum',
                                          fill_value=0)

print(f"Resposta ex 9.: \n{tabela_dinamica}")


#__________EXERCICIO 10__________________________________
print("\n--- Exercício 10 ---\n")

# Dados de exemplo
datas = pd.to_datetime(pd.date_range(start = '2026-07-25', periods = 15, freq = 'D'))
dados_visitas = {'Visitas': [150, 165, 178, 199, 205, 210, 225, 230, 215, 240, 255, 260, 245, 250, 270]}
df_visitas = pd.DataFrame(data = dados_visitas, index = datas)
df_visitas.index.name = 'Data'

#print(df_visitas)

visitas_agosto = df_visitas.loc['2026-08']
print(f"Visitas em agosto de 2026:\n{visitas_agosto}")