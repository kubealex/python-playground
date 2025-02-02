import pandas as pd

df = pd.read_csv("ade2.csv")
df = df.groupby('ID').sum().divide(2).reset_index()
df = df.sort_values('Score', ascending=False)

print(df.head(25))



