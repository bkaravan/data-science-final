# Sample data_deliverable/compiled_data/compiled.csv

import pandas as pd

compiled = pd.read_csv("../compiled_data/compiled.csv")

compiles_sample = compiled.sample(100)  # TODO: proportionally sample by rating

compiled_sample_with_avg = compiled.sample(
    100, replace=True, weights=compiled["averageRating"]
)

compiles_sample.to_csv("../compiled_data/sample.csv", index=False)
compiled_sample_with_avg.to_csv("../compiled_data/sample_avg.csv", index=False)