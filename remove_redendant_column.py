import pandas as pd

data = pd.read_csv('health_dataset.csv')

data.drop('social_support_score', axis=1, inplace=True)

print(data.to_string())

