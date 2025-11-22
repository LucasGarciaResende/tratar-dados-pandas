import pandas as pd
import numpy as np

df = pd.read_csv('data.csv', sep = ';', engine='python', encoding='utf-8') # Importando Arquivo

print(df.info()) # Informações Gerais
print(df[-3:]) # Exibindo últimos 3 registros

df_copy = df # Copiando o Dataframe para uma nova variável
df_copy['Calories'].fillna('0', inplace=True) # Trocando os valores nulos na coluna 'Calories' por 0
print(df_copy) # Exibindo o Dataframe com as mudanças na coluna Calories

df_copy['Date'].fillna('1900/01/01', inplace=True) # Trocando os valores nulos na coluna 'Date' por 1900/01/01
print(df_copy) # Exibindo o Dataframe com as mudanças na coluna Date

df_copy['Date'].replace('1900/01/01', np.nan, inplace=True) # Revertendo os valores 1900/01/01 por NaN para evitar erro
df_copy['Date'].replace('20201226', pd.to_datetime('20201226'), inplace=True) # Transformando o valor 20201226 no formato Datetime
df_copy['Date'] = pd.to_datetime(df_copy['Date']) # Formatando a coluna 'Date' inteira para Datetime
df_copy['Date'].fillna(pd.to_datetime('1900/01/01'), inplace=True) # Trocando o valor NaN restante para 1900/01/01 no formato Datetime
print(df_copy) # Exibindo o resultado final
