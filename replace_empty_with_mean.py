import pandas as pd

data = pd.read_csv('health_dataset.csv')

x = data["anxiety_score"].mean()
data.fillna({"anxiety_score" : x}, inplace = True)

print(data.to_string())

