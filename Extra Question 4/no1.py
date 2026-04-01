import pandas as pd
s = pd.Series(['10', '20', 'abc','30'])
#converts to numeric, imvalid parsing will be set as NaN
numeric_s = pd.to_numeric(s, errors='coerce')
print(numeric_s)

'''
to_numeric()
converts values to int or float
Tries to interpret each string as a number

Note: errors='corece'
This is the key concept
If conversion is possible -> conerts normally
if conversion fails -> replaces with NaN (Not a Number)
'''