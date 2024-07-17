import pandas as pd

dados = pd.read_csv('./dados_ficticios.csv')

df = pd.DataFrame(data=dados)
print(df[df["idade"] > 40]) 
print(df[df["renda"] > 5000])
print(df[df["renda"] > 15000])
