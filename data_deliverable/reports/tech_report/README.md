# tech report

How many data points are there in total?

- Before cleaning and duplicate removal: 10715 rows, 11 columns
- After the cleaning: 1312 rows, 15 columns

How many are there in each group you care about (e.g. if you are dividing your data into positive/negative examples, are they split evenly)?

- We don't have a classification target variable, rather our target variable (IMDb average movie rating) is normally distributed $[0, 10]$.
- When cleaning our data, we decided to group it by year released and title, by the nature of our data.
- As of now, we could group them by director, release year, worldwide gross. We don't have positive/negative examples but we do have specifications of -1 when data is not available.

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

- We used the pandas library to generate the appropriate sample for us. After we
  compiled our data from IMDB and The Numbers, we set the weights to the `averageRating`
  column to ensure proper distribution of our sample.

Is it (the sample) comparably small or large?

- Given that movies are a very easy source to find, having a sample of 100 entries is relatively small.
- Our cleaned dataset consists of 1312 entires, so the sample is about 7%.

Is it (the sample) representative or is it (the sample) likely to exhibit some kind of sampling bias?

- We tried to create our sample to best reflect our compiled database. Specifically,
  we payed attention to the `averageRating` column, as it is our main metric of
  movie's "success".
- While focusing on a single metric, like averageRating in our case, is useful, other variables can also impact the success of a movie, such as budget, box office earnings, or the crew.

Are there any other considerations you took into account when collecting your data? This is open-ended based on your data; feel free to leave this blank. (Example: If it's user data, is it public/are they consenting to have their data used? Is the data potentially skewed in any direction?)

- One consideration we took into account is what ratings to use as our target variable. We decided to go with IMDb ratings since they are reputable and widely used.

How clean is the data? Does this data contain what you need in order to complete the project you proposed to do? (Each team will have to go about answering this question differently but use the following questions as a guide. Graphs and tables are highly encouraged if they allow you to answer these questions more succinctly.)

- To check how clean our data is, we decided to use describe() in pandas to get a summary of statistics for numerical columns. You can see the code and things we checked for at the bottom of `compile.py`.

- As a result of our summary, we found that none of the entries are missing, there are no duplicates, data types match the expected ones

- The only challenge/issue we have is there are movies with the same exact title, that were released in the same year. But we only have the information on budgets and box offices about one of them. The problem is that our scraping data doesn't indicate each one since the only in common elements are title and release date, that match. So we are not sure whether we should keep both entries, one entry, or get rid of both entires. It's just 12 movies which is not a significat percentage of our cleaned data by any means, but we would love feedback on this!

Here is the result of our descriptions of data that proves the points stated above:

### Missing Values

| Column           | Missing Values |
| ---------------- | -------------- |
| title            | 0              |
| isAdult          | 0              |
| runtimeMinutes   | 0              |
| genres           | 0              |
| averageRating    | 0              |
| numVotes         | 0              |
| director         | 0              |
| writer           | 0              |
| Release Date     | 0              |
| productionBudget | 0              |
| domesticGross    | 0              |
| worldwideGross   | 0              |
| releaseYear      | 0              |
| releaseMonth     | 0              |
| releaseDay       | 0              |

### Data Types

| Column           | Data Type |
| ---------------- | --------- |
| title            | object    |
| isAdult          | int64     |
| runtimeMinutes   | object    |
| genres           | object    |
| averageRating    | float64   |
| numVotes         | int64     |
| director         | object    |
| writer           | object    |
| Release Date     | object    |
| productionBudget | int64     |
| domesticGross    | int64     |
| worldwideGross   | int64     |
| releaseYear      | object    |
| releaseMonth     | int64     |
| releaseDay       | int64     |

### Number of Duplicates

| Description | Count |
| ----------- | ----- |
| Duplicates  | 0     |

| Statistic | isAdult  | averageRating | numVotes  | worldwideGross | releaseMonth | releaseDay |
| --------- | -------- | ------------- | --------- | -------------- | ------------ | ---------- |
| count     | 1311.0   | 1311.0        | 1.311e+03 | 1.311e+03      | 1311.0       | 1311.0     |
| mean      | 0.000763 | 6.370404      | 1.086e+05 | 6.543e+07      | 7.491228     | 16.146453  |
| std       | 0.027618 | 1.071302      | 1.926e+05 | 1.487e+08      | 3.306673     | 8.441622   |
| min       | 0.0      | 1.8           | 5.0       | 0.0            | 1.0          | 1.0        |
| 25%       | 0.0      | 5.8           | 1.206e+04 | 4.305e+06      | 5.0          | 9.0        |
| 50%       | 0.0      | 6.5           | 4.549e+04 | 2.134e+07      | 8.0          | 16.0       |
| 75%       | 0.0      | 7.1           | 1.205e+05 | 6.788e+07      | 10.0         | 23.0       |
| max       | 1.0      | 9.0           | 2.528e+06 | 2.923e+09      | 12.0         | 31.0       |

- The isAdult column has a very low mean close to zero, suggesting that almost all movies in the dataset are non-adult. After closer examination, we found only one entry that is True for the isAdult parameter out of 1312 entries, so we decided to drop this parameter as it will not provide any statistical significance to our analysis and project.
- The dataset appears to be complete with no missing values across all the columns, which is excellent as it suggests that the data is well-maintained and ready for analysis without the need for imputation.
- There are no duplicate entries, indicating that the data is likely to be unique and well-curated.

- The averageRating has a mean of approximately 6.37, with a standard deviation of about 1.07, indicating a moderate average rating for movies with some variation. But this is not something we can use or judge by as we haven't grouped our data.

- The numVotes column shows a large standard deviation, which suggests that some movies have many more votes than others, possibly indicating a wide range in the popularity of the movies.

- The releaseMonth and releaseDay columns suggest a uniform distribution of movie releases throughout the year.

Summarize any challenges or observations you have made since collecting your data. Then, discuss your next steps and how your data collection has impacted the type of analysis you will perform. (approximately 3-5 sentences)

- Because movies are very accessible, finding data was not very difficult. The most challenging part was properly merging different tables from both IMDb database sources and our own web-scraping results. 
- Some minor challenges also included merging on different datatypes from different tables -- we fixed it with typecasting. 
- We are only performing analysis on the movies with the most complete set of data (director, box office, release dates, ratings, etc). So our database shrank a lot, since our scraped data had much less entries than the IMDb one. Additionally, not all of them matched. So our analysis might not be representative of whole movie industry but rather of those movies for which the data got successfully scraped.
