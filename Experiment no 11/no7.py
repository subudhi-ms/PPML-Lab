import pandas as pd
data = {
    'Name':['Alice','Bob','Charlie'],
    'Age' :[25,30,35],
    'City':['New york','San francisco','Los angles']
}
df=pd.DataFrame(data)
print("DataFrame :")
print(df)
print("\nAge column :")
print(df['Age'])
print("\nRow at index 1 :")
print(df.iloc[1])