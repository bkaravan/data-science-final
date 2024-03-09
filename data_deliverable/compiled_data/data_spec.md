# data spec

## `compiled.csv` & `sample.csv`

### simple

- `title` (string) - the title of the movie
- `originalTitle` (string) - the original title of the movie
- `releaseYear` (int, YYYY) - the release year of the movie
- `releaseMonth` (int, MM) - the release month of the movie
- `releaseDay` (int, DD) - the release day of the movie
- `runtimeMinutes` (int) - primary runtime of the movie, in minutes
- `genres` (string array) - the genres associated with the movie
- `averageRating` (float of form $a.b$) - the weighted average of all the individual user ratings
- `numVotes` (int) - the number of votes the movie has received
- `productionBudget` (string in format $\$x,xxx,...$) - the production budget of the movie
- `domesticGross` (string in format $\$x,xxx,...$) - the domestic gross of the movie
- `worldwideGross` (string in format $\$x,xxx,...$) - the worldwide gross of the movie

### detailed

- `title`

  - type: string
  - description: the title of the movie
  - default value: ``
  - range of value: any string
  - distribution: ???
  - unique: no
  - required: yes
  - use in analysis: probably not
  - sensitive: no

- `releaseYear`

  - type: int (YYYY)
  - description: the release year of the movie
  - default value: ``
  - range of value: any year, $[-1, 2024]$
  - mean value: $2004.96$
  - distribution: skew left
  - unique: no
  - required: yes
  - use in analysis: yes
  - sensitive: no

- `releaseMonth`

  - type: int (MM)
  - description: the release year of the movie
  - default value: ``
  - range of value: any year, $[-1, 12]$
  - mean value: $6.92$
  - distribution: uniform
  - unique: no
  - required: yes
  - use in analysis: yes
  - sensitive: no

- `releaseDay`

  - type: int (DD)
  - description: the release year of the movie
  - default value: ``
  - range of value: any year, $[-1, 31]$
  - mean value: $15.92$
  - distribution: uniform
  - unique: no
  - required: yes
  - use in analysis: yes
  - sensitive: no

- `runtimeMinutes`

  - type: int
  - description: primary runtime of the movie, in minutes
  - default value: `-1`
  - range of value: any positive integer, $[-1, 700]$
  - mean value: $102.93$
  - distribution: normal
  - unique: no
  - required: yes
  - use in analysis: yes
  - sensitive: no

- `genres`

  - type: string array
  - description: the genres associated with the movie
  - default value: `[]`
  - range of value: any string
  - distribution: ???
  - unique: no
  - required: yes
  - use in analysis: yes
  - sensitive: no

- `averageRating`

  - type: float of form $a.b$
  - description: the weighted average of all the individual user ratings
  - default value: `-1`
  - range of value: any positive float, $[1.2, 9.9]$
  - mean value: $6.23$
  - distribution: normal
  - unique: no
  - required: yes
  - use in analysis: yes
  - sensitive: no

- `numVotes`

  - type: int
  - description: the number of votes the movie has received
  - default value: `-1`
  - range of value: any positive integer, $[5, 2865377]$
  - mean value: $68326.08$
  - distribution: skew right
  - unique: no
  - required: yes
  - use in analysis: yes
  - sensitive: no

- `productionBudget`

  - type: string in format $\$x,xxx,...$
  - description: the production budget of the movie
  - default value: `-1`
  - range of value: $[1400, 460000000]$
  - mean value: $32496736.58$
  - distribution: skew right
  - unique: no
  - required: yes
  - use in analysis: yes
  - sensitive: no

- `domesticGross`

  - type: string in format $\$x,xxx,...$
  - description: the domestic gross of the movie
  - default value: `-1`
  - range of value: $[0, 858373000]$
  - mean value: $41294874.98$
  - distribution: skew right
  - unique: no
  - required: yes
  - use in analysis: yes
  - sensitive: no

- `worldwideGross`
  - type: string in format $\$x,xxx,...$
  - description: the worldwide gross of the movie
  - default value: `-1`
  - range of value: $[0, 2923706026]$
  - mean value: $91190738.17$
  - distribution: skew right
  - unique: no
  - required: yes
  - use in analysis: yes
  - sensitive: no
