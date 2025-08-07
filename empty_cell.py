import pandas as pd

data = pd.read_csv('Data_Entry_2017.csv')

new_data = data.dropna(inplace = True) # Removes the empty cell rows

print(new_data)

