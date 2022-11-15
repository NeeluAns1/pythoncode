import pandas as pd

#making data frame from csv file

data = pd.read_csv("filetest.csv", index_col ="CustomerID")
 
# retrieving coluns by indexing operator

#first = data["Age"]

print(data)