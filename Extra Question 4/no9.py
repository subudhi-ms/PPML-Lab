import pandas as pd
df = pd.DataFrame({"C_ID": [1, 2, 3], "S_ID":[4,9,8], "Amount":[100, 200, 300]})
print("Original DataFrame:\n", df)
result = df.groupby(['C_ID', 'S_ID']).size().reset_index(name='Count')
print("\nGrouped count:\n", result)