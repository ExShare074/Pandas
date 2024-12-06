#определяем средню зарплату по городу, перед эти пустые значения заменяем на 1
import pandas as pd

df = pd.read_csv('dz.csv')
df['Salary'] = df['Salary'].fillna(1)

print(df.groupby('City')['Salary'].mean())
