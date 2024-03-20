# Sample data_deliverable/compiled_data/compiled.csv

import matplotlib.pyplot as plt
import pandas as pd

compiled = pd.read_csv("../compiled_data/compiled.csv")

compiled_sample_with_avg = compiled.sample(
    100, weights=compiled["averageRating"], random_state=3
)
compiled_sample_with_avg.to_csv("../compiled_data/sample.csv", index=False)

# check distribution of "averageRating"
compiled["averageRating"].hist()
plt.xlabel("Average Rating")
plt.ylabel("Frequency")
plt.title("Complete dataset average rating distribution")
plt.show()

compiled_sample_with_avg["averageRating"].hist()
plt.xlabel("Average Rating")
plt.ylabel("Frequency")
plt.title("Sample data average rating distribution")
plt.show()
