import pandas as pd
df_csv=pd.read_csv("C:\\Users\\student\\Desktop\\24CSEAIML014\\Experiment no 11\\sample.csv")
print("DataFrame from csv :")
print(df_csv)
df_json=pd.read_json("C:\\Users\\student\\Desktop\\24CSEAIML014\\Experiment no 11\\sample.json")
print(df_json)