import pandas as pd
df = pd.DataFrame ({"Name" : ["Rajesh", "Subha", 'Rabi'],
                    "Age" : [21, 20, 21],
                    "Marks" : [85, 90, 99]})
print("Original DataFrame:\n", df)
print("\nTransposed DataFrame:\n", df.T) #df.transpose() 