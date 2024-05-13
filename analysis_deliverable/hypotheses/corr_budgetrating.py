import pandas as pd
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import pearsonr
import statsmodels.api as sm

df = pd.read_csv('..\machine_learning\data\preprocessed.csv')
df.dropna(subset=['productionBudget', 'averageRating'], inplace=True)

correlation, p_value = pearsonr(df['productionBudget'], df['averageRating'])
print(f'Pearson correlation coefficient: {correlation}')
print(f'P-value: {p_value}')
alpha = 0.05
if p_value < alpha:
    print("The result is significant, so we reject the null hypothesis.")
else:
    print("The result is not significant, so we fail to reject the null hypothesis.")



plt.scatter(df['productionBudget'], df['averageRating'])
plt.title('Relationship between Production Budget and averageRating')
plt.xlabel('Production Budget')
plt.ylabel('averageRating')
plt.show()

X = df['productionBudget']
y = df['averageRating']

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()
model_summary = model.summary()
print(model_summary)