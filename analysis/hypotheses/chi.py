import pandas as pd
from scipy.stats import ttest_ind
df = pd.read_csv('..\machine_learning\data\preprocessed.csv')
df.dropna(subset=['domesticGross', 'releaseMonth'], inplace=True)


# do we need to do it or can we use Pearson corr