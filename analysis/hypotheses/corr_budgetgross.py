import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import statsmodels.api as sm

df = pd.read_csv('..\machine_learning\data\preprocessed.csv')
df.dropna(subset=['productionBudget', 'worldwideGross'], inplace=True)
correlation, p_value = pearsonr(df['productionBudget'], df['worldwideGross'])

print(f'Pearson correlation coefficient: {correlation}')
print(f'P-value: {p_value}')
alpha = 0.05
if p_value < alpha:
    print("The result is significant, so we reject the null hypothesis.")
else:
    print("The result is not significant, so we fail to reject the null hypothesis.")

plt.scatter(df['productionBudget'], df['worldwideGross'])
plt.title('Relationship between Production Budget and Worldwide Gross')
plt.xlabel('Production Budget')
plt.ylabel('Worldwide Gross')
plt.show()

X = df['productionBudget']
y = df['worldwideGross']
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
model_summary = model.summary()
print(model_summary)