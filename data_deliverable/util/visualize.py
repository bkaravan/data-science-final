# this is to visualize the data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# import from data_deliverable/compiled_data/compiled.csv
compiled = pd.read_csv("../compiled_data/compiled.csv")

print("shape:", compiled.shape)

VISUALIZE_HISTOGRAMS = False

# visualize data once compiled set is finished
if VISUALIZE_HISTOGRAMS:
    print("Visualizing data...")

    num_cols = [
        "runtimeMinutes",
        "averageRating",
        "numVotes",
        "productionBudget",
        "domesticGross",
        "worldwideGross",
        "releaseYear",
        "releaseMonth",
        "releaseDay",
    ]

    # histograms for numerical columns
    for col in num_cols:
        col_min_max = (compiled[col].min(), compiled[col].max())
        avg = compiled[col][compiled[col] != -1].mean()
        title = f"{col}, range: [{col_min_max[0]}, {col_min_max[1]}], mean: {avg:.2f}"
        plt.hist(compiled[col][compiled[col] != -1], bins=40)
        plt.title(title), print(title)
        plt.show()
