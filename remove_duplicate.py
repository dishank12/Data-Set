import pandas as pd

data = pd.read_csv('health_dataset.csv')

data.drop_duplicates(inplace=True) # Removes the duplicate values

print(data.duplicated().to_string()) # Checks the Duplicate value 

