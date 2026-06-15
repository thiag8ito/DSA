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
print(descr_a)
