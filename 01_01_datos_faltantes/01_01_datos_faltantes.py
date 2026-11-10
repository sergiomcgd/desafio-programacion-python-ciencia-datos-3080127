import pandas as pd
df = pd.read_csv('empleados.csv', delimiter=";")

print(df.head(20),"\n")

print(df.isna().sum())
print(df.notna().sum())
print(df.isna().mean()*100)

