import pandas as pd
data = [10,20,30]
label=['a','b','c']
series = pd.Series(data,index=label)
print("Pandas series :")
print(series)
print("Value at label'b :",series['b'])