import pandas as pd

data = pd.read_csv('health_dataset.csv')

data.fillna(130, inplace = True) # Replace the value to empty cell instead of removing entire row.

print(data.to_string())

# To replace specific columns
import pandas as pd

data = pd.read_csv('health_dataset.csv')

data.fillna({"anxiety_score": 130}, inplace = True) # Replace the specific column value to empty cell.

print(data.to_string())