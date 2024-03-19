# tech report

How many data points are there in total?

- Before cleaning and duplicate removal: 10715 rows, 11 columns
- TODO: finalize

How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)?

- We don't have a classification target variable, rather our target variable (IMDb average movie rating) is normally distributed $[0, 10]$.
- TODO: decide how we clean data for movies, maybe "directiors" or "release year" can be used as a group

Do you think this is enough data to perform your analysis later on?

- Yes, we have enough data to perform an analysis.

What are the identifying attributes?

- `tconst`: the unique identifier for each movie (in IMDb datasets, not in compiled data)
- `title`: the title of the movie

Where is the data from?

- [IMDb](https://developer.imdb.com/non-commercial-datasets/) datasets, `title.basics_movies.tsv` and `title.ratings_movies.tsv`
- [The Numbers](https://www.the-numbers.com/movie/budgets/all) dataset, web scraped

Is the source reputable?

- Yes, both IMDb and The Numbers are reputable sources.

How did you generate the sample?

- TODO 

- We used the pandas library to generate the appropriate sample for us. After we
compiled our data from IMDB and The Numbers, we set the weights to the `averageRating`
column to ensure proper distribution of our sample.

Is it (the sample) comparably small or large?

- TODO Need to consider the size of the db after cleaning

- Given that movies are a very easy source to find, having a sample of 100 entries
is relatively small. 

Is it (the sample) representative or is it (the sample) likely to exhibit some kind of sampling bias?

- TODO consider what else can go wrong with biasing

- We tried to create our sample to best reflect our compiled database. Specifically, 
we payed attention to the `averageRating` column, as it is our main metric of 
movie's "success". 

Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)

- One consideration we took into account is what ratings to use as our target variable. We decided to go with IMDb ratings since they are reputable and widely used.

How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)

- TODO

Summarize any challenges or observations you have made since collecting your data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. (approximately 3-5 sentences)

- TODO
