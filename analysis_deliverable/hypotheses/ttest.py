import pandas as pd
from scipy.stats import ttest_ind
df = pd.read_csv('..\machine_learning\data\preprocessed.csv')
df.dropna(subset=['domesticGross', 'releaseMonth'], inplace=True)

# december_gross = df[df['releaseMonth'] == 12]['domesticGross']
# other_months_gross = df[df['releaseMonth'] != 12]['domesticGross']

# t_stat, p_value = ttest_ind(december_gross, other_months_gross, equal_var=False)

# print(f'T-statistic Dec: {t_stat}')
# print(f'P-value Dec: {p_value}')

# # June
# june_gross = df[df['releaseMonth'] == 6]['domesticGross']
# other_months_gross3 = df[df['releaseMonth'] != 6]['domesticGross']

# t_stat, p_value = ttest_ind(july_gross, other_months_gross3, equal_var=False)

# print(f'T-statistic June: {t_stat}')
# print(f'P-value June: {p_value}')


# # July
# july_gross = df[df['releaseMonth'] == 7]['domesticGross']
# other_months_gross2 = df[df['releaseMonth'] != 7]['domesticGross']

# t_stat, p_value = ttest_ind(july_gross, other_months_gross2, equal_var=False)

# print(f'T-statistic July: {t_stat}')
# print(f'P-value July: {p_value}')

results = {}
for month in range(1, 13):
    current_month_gross = df[df['releaseMonth'] == month]['worldwideGross']
    other_months_gross = df[df['releaseMonth'] != month]['worldwideGross']
    t_stat, p_value = ttest_ind(current_month_gross, other_months_gross, equal_var=False)
    results[month] = {'T-statistic': t_stat, 'P-value': p_value}
for month, values in results.items():
    print(f"Month: {month}, T-statistic: {values['T-statistic']:.2f}, P-value: {values['P-value']:.3f}")
    alpha = 0.05
    if values['P-value'] < alpha:
        print("The result is significant, so we reject the null hypothesis.")
    else:
        print("The result is not significant, so we fail to reject the null hypothesis.")
