# too large to include all imdb data on github, so we prune to only include
# movies, which are the subject of our project

# full datasets: https://datasets.imdbws.com/

import pandas as pd

# Load the data
title_basics = pd.read_csv("../raw_data/imdb/title.basics.tsv", sep="\t")
title_ratings = pd.read_csv("../raw_data/imdb/title.ratings.tsv", sep="\t")
title_crew = pd.read_csv("../raw_data/imdb/title.crew.tsv", sep="\t")
name_basics = pd.read_csv("../raw_data/imdb/name.basics.tsv", sep="\t")

# Prune the data
title_basics = title_basics[title_basics["titleType"] == "movie"]
title_ratings = title_ratings[title_ratings["tconst"].isin(title_basics["tconst"])]
title_crew = title_crew[title_crew["tconst"].isin(title_basics["tconst"])]
name_basics = name_basics[
    name_basics["nconst"].isin(title_crew["directors"])
    | name_basics["nconst"].isin(title_crew["writers"])
]

# Save the data
title_basics.to_csv("../raw_data/imdb/title.basics_movies.tsv", sep="\t", index=False)
title_ratings.to_csv("../raw_data/imdb/title.ratings_movies.tsv", sep="\t", index=False)
title_crew.to_csv("../raw_data/imdb/title.crew_movies.tsv", sep="\t", index=False)
name_basics.to_csv("../raw_data/imdb/name.basics_movies.tsv", sep="\t", index=False)
