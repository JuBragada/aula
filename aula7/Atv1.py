import pandas as pd

dados = {
    "Nome": ["Julia","André","Giovanna","Raphael","Vanda","Rosendo","Keli"],
    "Idade": [23,30,23,26,56,69,50],
    "Cidade": ["Recife","Recife","Recife","Salvador","Salvador","São Paulo","Manaus"]
}

df = pd.DataFrame(data=dados)

#print(df)
filtrocid_df = df[df["Cidade"] == "Recife"]
print(filtrocid_df)