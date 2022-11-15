import pandas as pd

data = pd.read_excel(r'C:\Pythoncode\Companies.xlsx')
print(data)
df = pd.DataFrame(data, columns=['CEO','DATA'])
print(df)