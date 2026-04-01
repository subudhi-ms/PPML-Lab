import pandas as pd
import matplotlib.pyplot as plt
data = {
    'year': [2018, 2019, 2020, 2021, 2022, 2023],
    'sales': [100, 120, 110, 150, 170, 190]
}
df = pd.DataFrame(data)
print("Sample DataFrame:")
print(df)
plt.plot(df['year'], df['sales'], marker='o', linestyle='-', color='b')
plt.xlabel('Year')
plt.ylabel('Sales')
plt.title('Year vs Sales Trend')
plt.show()