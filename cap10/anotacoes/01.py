import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf
from statsmodels.stats.weightstats import ttest_ind
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 6)

np.random.seed(42)

grupo_a = np.random.normal(loc=175, scale=5, size=100)
grupo_b = np.random.normal(loc=180, scale=6, size=100)

df_alturas = pd.DataFrame({'Grupo A': grupo_a, 'Grupo B': grupo_b})

print(df_alturas.head())

print('\n--- Estatísticas Descritivas com Pandas ---')
print(df_alturas.describe())

print('\n--- Estatísticas Descritivas com Statsmodels ---')
descr_a = sm.stats.DescrStatsW(grupo_a)

descr_b = sm.stats.DescrStatsW(grupo_b)

print("\n--- Estatísticas Descritivas do Grupo A (com StatsModels) ---")
print(f"Média : {descr_a.mean:.2f}")
print(f"Desvio Padrão: {descr_a.std:.2f}")
print(f"Mínimo: {np.min(grupo_a):.2f}")
print(f"Máximo: {np.max(grupo_a):.2f}")

print("\n--- Estatística Descritivas do Grupo B (com StatsModels) ---")
print(f"Média: {descr_b.mean:.2f}")
print(f"Desvio Padrão: {descr_b.std:.2f}")
print(f"Mínimo: {np.min(grupo_b):.2f}")
print(f"Máximo: {np.max(grupo_b):.2f}")

#Visualização

sns.kdeplot(data=df_alturas, fill=True)
plt.title('Distribuição de Alturas dos Grupos')
plt.xlabel('Altura (cm)')
plt.ylabel('Densidade')
plt.show()


np.random.seed(101)

anos_experiencia = np.arange(1, 11) + np.random.randn(10) * 0.5
salario = 5000 + anos_experiencia * 1500 + np.random.randn(10) * 800

df_salario = pd.DataFrame({'Anos de Experiencia': anos_experiencia, 'Salario': salario})

print(df_salario.head())

correlacao = df_salario['Anos de Experiencia'].corr(df_salario['Salario'])

print(f"\n--- Coeficiente de Correlação ---\n")
print(f"A correlação entrer Anos de Experiencia e Salario é: {correlacao:.4f}\n")

sns.regplot(x='Anos de Experiencia', y='Salario', data=df_salario)
plt.title('Relação entre Anos de Experiencia e Salário')
plt.xlabel('Anos de Experiencia')
plt.ylabel('Salário (R$)')
plt.show()

correlacoes = df_alturas.corr()

plt.figure(figsize=(6, 4))
sns.heatmap(correlacoes, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Heatmap de Correlação entre Grupos de Altura')
plt.show()