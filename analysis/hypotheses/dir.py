import pandas as pd
from scipy.stats import chi2_contingency
df = pd.read_csv('..\machine_learning\data\preprocessed.csv')
df.dropna(subset=['director', 'writer'], inplace=True)
# counted = df.groupby('director').filter(lambda x: len(x)>3)['director']
# counted.to_csv("directors.csv")
# print(counted.head)


import csv
from collections import Counter
csv_file_path = '..\machine_learning\data\preprocessed.csv'

def count_movies_by_director(csv_file_path):
    with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        director_counter = Counter()
        for row in reader:
            director = row['director']
            if director:  # Check if the director field is not empty
                director_counter[director] += 1
        sorted_directors = director_counter.most_common()
        print("Number of movies by each director:")
        dict = {}
        for director, count in sorted_directors:
            if count >= 3:
                dict[director] = count
                print(f"{director}: {count}")
        return dict
counted = count_movies_by_director(csv_file_path)
# counted.to_csv("directors2.csv")

top_directors = counted
rating = df['averageRating'].mean()
df['is_top_director'] = df['director'].apply(lambda x: 'Yes' if x in top_directors else 'No')
df['rating_category'] = df['averageRating'].apply(lambda x: 'High' if x >= rating else 'Low')

contingency_table = pd.crosstab(df['is_top_director'], df['rating_category'])
chi2, p, dof, expected = chi2_contingency(contingency_table)

print(f"Chi-squared: {chi2}")
print(f"P-value: {p}")
# print(f"Degrees of freedom: {dof}")
# print(f"Expected frequencies:\n{expected}")

alpha = 0.05
if p < alpha:
    print("The result is significant, so we reject the null hypothesis.")
else:
    print("The result is not significant, so we fail to reject the null hypothesis.")

