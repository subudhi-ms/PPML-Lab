import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
student_data = pd.DataFrame({
    'School code': ['S001', 'S002', 'S003', 'S001', 'S002', 'S004'],
    'Class': ['V', 'V', 'VI', 'VI', 'V', 'VI'],
    'Name': ['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton', 'Gino Mcneill', 'David Parkes'],
    "date_of_birth": ['15/05/2002', '17/05/2003', '15/05/2002', '14/05/2002', '17/05/2003', '16/05/2002'],
    'age': [12, 12, 13, 12, 12, 13],
    'height': [173, 192, 186, 167, 151, 159],
    'weight': [30, 32, 33, 30, 31, 32],
    'address': ['Street 1', 'Street 2', 'Street 3', 'Street 1', 'Street 2', 'Street 4']
}, index=['S1', 'S2', 'S3', 'S4', 'S5', 'S6'])

print("Original DataFrame:\n", student_data)

print("\nSplit the said data on school_code wise:\n")
result = student_data.groupby('School code')

for name, group in result:
    print("\nGroup Name:", name)
    print(group)

print("\nType of the object:\n", type(result))