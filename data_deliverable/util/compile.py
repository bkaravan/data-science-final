# we have three datasets:
#   data_deliverable/raw_data/imdb/title.basics_movies.tsv
#   data_deliverable/raw_data/imdb/title.ratings_movies.tsv
#   data_deliverable/raw_data/the_numbers/movie_budgets.csv

import pandas as pd

# Load data
print("Loading data...")
title_basics = pd.read_csv(
    "../raw_data/imdb/title.basics_movies.tsv", low_memory=False, sep="\t"
)
title_ratings = pd.read_csv("../raw_data/imdb/title.ratings_movies.tsv", sep="\t")
title_crew = pd.read_csv("../raw_data/imdb/title.crew_movies.tsv", sep="\t")
name_basics = pd.read_csv("../raw_data/imdb/name.basics_movies.tsv", sep="\t")
movie_budgets = pd.read_csv("../raw_data/the_numbers/movie_budgets.csv")

# Merge data
print("Merging IMDb data...")
imdb = title_basics.merge(title_ratings, on="tconst")
title_crew = title_crew.merge(name_basics, left_on="directors", right_on="nconst")
title_crew.rename(columns={"primaryName": "director"}, inplace=True)
title_crew = title_crew[["tconst", "director", "writers"]] #select
title_crew = title_crew.merge(name_basics, left_on="writers", right_on="nconst")
title_crew.rename(columns={"primaryName": "writer"}, inplace=True)
title_crew = title_crew[["tconst", "director", "writer"]]
imdb = imdb.merge(title_crew, on="tconst")
imdb.drop(columns=["tconst", "titleType", "endYear"], inplace=True)

# Merge with movie_budgets
print("Merging with movie budgets...")

months = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}


def convertDay(x):
    if len(x) != 2:
        return -1
    if x[1] == ",":
        return int(x[0])
    return int(x)


def convertMonth(x):
    if len(x) != 3:
        return -1
    return months[x]


# compiled = imdb.merge(movie_budgets, left_on="primaryTitle", right_on="Movie")
# compiled.drop(columns=["Movie", "Rank", "startYear", "originalTitle"], inplace=True)

# Split the date "Dec 25, 1996" into 12 25 1996
print("Splitting release date...")
movie_budgets["releaseYear"] = movie_budgets["Release Date"].apply(
    lambda x: (
        x[-4:]
        if x != "Unknown"
        and (len(x) == len("Dec 25, 1996") or len(x) == len("Dec 2, 1996"))
        else -1
    )
)
movie_budgets["releaseMonth"] = movie_budgets["Release Date"].apply(
    lambda x: (
        convertMonth(x[:3])
        if x != "Unknown"
        and (len(x) == len("Dec 25, 1996") or len(x) == len("Dec 2, 1996"))
        else -1
    )
)
movie_budgets["releaseDay"] = movie_budgets["Release Date"].apply(
    lambda x: (
        convertDay(x[4:6])
        if x != "Unknown"
        and (len(x) == len("Dec 25, 1996") or len(x) == len("Dec 2, 1996"))
        else -1
    )
)
# compiled.drop(columns=["Release Date"], inplace=True)

# Convert money to integers
# print("Converting money to integers...")
# compiled["Production Budget"] = compiled["Production Budget"].apply(
#     lambda x: int(x[1:].replace(",", "")) if x != "Unknown" else -1
# )
# compiled["Domestic Gross"] = compiled["Domestic Gross"].apply(
#     lambda x: int(x[1:].replace(",", "")) if x != "Unknown" else -1
# )
# compiled["Worldwide Gross"] = compiled["Worldwide Gross"].apply(
#     lambda x: int(x[1:].replace(",", "")) if x != "Unknown" else -1
# )

# # Convert runtime to integers
# print("Converting runtime to integers...")
# compiled["runtimeMinutes"] = compiled["runtimeMinutes"].apply(
#     lambda x: int(x) if x != "\\N" else -1
# )

# # Convert genres to lists
# print("Converting genres to lists...")
# compiled["genres"] = compiled["genres"].apply(
#     lambda x: x.split(",") if x != "\\N" else []
# )
print("Converting money to integers in movie_budgets...")
movie_budgets['Production Budget'] = movie_budgets['Production Budget'].apply(lambda x: int(x[1:].replace(",", "")) if x != "Unknown" else -1)
movie_budgets['Domestic Gross'] = movie_budgets['Domestic Gross'].apply(lambda x: int(x[1:].replace(",", "")) if x != "Unknown" else -1)
movie_budgets['Worldwide Gross'] = movie_budgets['Worldwide Gross'].apply(lambda x: int(x[1:].replace(",", "")) if x != "Unknown" else -1)
print("MOVIE BUDGETS COMING")
print(movie_budgets)
print(movie_budgets.columns)
print("IMDB BELOWWWWWWWWWWWWWWWWWWWWWWWWWW")
print(imdb)
print(imdb.columns)
compiled = imdb.merge(movie_budgets, left_on=["startYear", "primaryTitle"], right_on=["releaseYear", "Movie"])
compiled.drop(columns=["Movie", "Rank", "originalTitle", "startYear", "isAdult"], inplace=True)

# Rename columns
compiled.rename(
    columns={
        "primaryTitle": "title",
        "Production Budget": "productionBudget",
        "Domestic Gross": "domesticGross",
        "Worldwide Gross": "worldwideGross",
        "Release Date": "releaseDate"
    },
    inplace=True,
)
print(compiled.columns)


# Save the data
compiled.to_csv("../compiled_data/compiled.csv", index=False)



# Load your dataset
# df = pd.read_csv('data_deliverable\compiled_data\compiled.csv')

# Check for missing values
missing_values = compiled.isnull().sum()

# Check data types
data_types = compiled.dtypes

# Check for duplicates
duplicates = compiled.duplicated().sum()

# Summary statistics
summary_stats = compiled.describe()

# Output the findings
print("Missing Values:\n", missing_values)
print("\nData Types:\n", data_types)
print("\nNumber of Duplicates:", duplicates)
print("\nSummary Statistics:\n", summary_stats)
