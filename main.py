import pandas as pd

df = pd.read_csv("./pitches.csv")
print(df.describe())

df = df.T