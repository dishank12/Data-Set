import pandas as pd
import openpyxl

data = pd.read_excel('heartexcel.xlsx')

print(data.to_string()) 