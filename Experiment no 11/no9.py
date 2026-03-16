import pandas as pd
data = {
    'Math' : [90,85,80,90],
    'Science':[88,82,85,90],
    "English":[78,75,80,85]
}
df=pd.DataFrame(data)
print("DataFrame :")
print(df)
correlation = df.corr()
print("\ncorrelation matrix\n",correlation)