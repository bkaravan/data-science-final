import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('..\machine_learning\data\preprocessed.csv')

df['worldwideGross'] = pd.to_numeric(df['worldwideGross'], errors='coerce')
df['releaseMonth'] = pd.to_numeric(df['releaseMonth'], errors='coerce')

df.dropna(subset=['worldwideGross', 'releaseMonth'], inplace=True)
monthly_gross_average = df.groupby('releaseMonth')['worldwideGross'].mean()
plt.figure(figsize=(10, 6))
plt.bar(monthly_gross_average.index, monthly_gross_average.values, color='skyblue')

plt.title('Average Worldwide Gross Income by Month of Release')
plt.xlabel('Month of Release')
plt.ylabel('Average Worldwide Gross Income')
plt.xticks(range(1, 13), ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])

plt.show()