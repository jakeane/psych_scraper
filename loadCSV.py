import pandas as pd

csv = pd.read_csv("/Users/jackkeane/Downloads/medTerms.csv", header=None)
print(csv.iloc[:, 0].tolist())
