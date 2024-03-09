# data spec

Both the data specs below are derived from [IMDb](https://developer.imdb.com/non-commercial-datasets/).

## `title.basics_movies.tsv`

- `tconst` (string) - alphanumeric unique identifier of the title
- `titleType` (string) – the type/format of the title (e.g. movie, short, tvseries, tvepisode, video, etc). _For our project, we have filtered to just `movie`_.
- `primaryTitle` (string) – the more popular title / the title used by the filmmakers on promotional materials at the point of release
- `originalTitle` (string) - original title, in the original language
- `isAdult` (boolean) - 0: non-adult title; 1: adult title
- `startYear` (YYYY) – represents the release year of a title. In the case of TV Series, it is the series start year
- `endYear` (YYYY) – TV Series end year. ‘\N’ for all other title types. _For our project, because we only have movies, this will always be `\N`_.
- `runtimeMinutes` (int) – primary runtime of the title, in minutes
- `genres` (string array) – includes up to three genres associated with the title

## `title.ratings_movies.tsv`

- `tconst` (string) - alphanumeric unique identifier of the title
- `averageRating` (float of form $a.b$) – weighted average of all the individual user ratings
- `numVotes` (int) - number of votes the title has received
