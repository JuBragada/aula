import pandas as pd

dados = {
    "Nome": ["Julia","André","Giovanna","Raphael"],
    "Idade": [23,30,23,26]
}

df = pd.DataFrame(data=dados)

print(df)