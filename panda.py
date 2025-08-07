import pandas as pd

data = pd.read_csv('health_dataset.csv')

print(data.head(5)) # Display Top 5 rows 
print(data.tail(5)) # Display Bottom 5 rows
print(data.info()) # Information about data set columns , Non-Null Values, Data Type
print(data.describe()) # Describe the details of data set min value max value.