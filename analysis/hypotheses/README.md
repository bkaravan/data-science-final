## Hypothesis testing component: 
The group must formulate a minimum of three distinct research hypotheses and test them using a statistical testing method.

1) First, we wanted to check the hypothesis that a movie's release date within a month's window can affect its worldwide gross. For that, we used an independent ttest for every month, comparing that month's worldwide gross to every other month gross combined. 

2) Second, we thought that it would be valuable to check if there is any correlation between a movie's budget and its worldwide gross or its average rating. For that, we used Pearson's correlation coefficient.

3) Lastly, we wanted to explore the idea of directors affecting the average rating of the movie. Given that our data was mostly from the top charts of IMDB, we thought that if a director has at least 3 movies in our dataset, we can consider that director as a "top director". Then, we created a "ranking category" column for the movies, where a movie would be considered "high" if its rating is above the mean, and low otherwise. We used a chi-squared test to see if there is a statistically significant contingency of top directors and high rated movies. 

## Description of the result
We will answer the following question throughout the next section: Why did you use this statistical test? Which other tests did you consider or evaluate? What metric(s) did you use to measure success or failure, and why did you use it? What challenges did you face evaluating the model? Did you have to clean or restructure your data?


## What is your interpretation of the results? 
Do you accept or deny the hypothesis, or are you satisfied with your prediction accuracy? For prediction projects, we expect you to argue why you got the accuracy/success metric you have. Intuitively, how do you react to the results? Are you confident in the results?

`Hypothesis 1: Release Date's Effect on Worldwide Gross
`

For our first hypothesis, we decided to visualize the mean worldwide gross profit for all the movies based on which month it has been released in. The graph can be found here :analysis\hypotheses\gross_months.png. We noticed that the top profits occured in June/July and December. It made sense -- summer and Christmas holidays are peak times for movie visits. So we decided to focus on these two months, even though we did run our tests for every month. 

#### Test Used: Independent t-tests.

* Reason: The independent t-test is ideal for comparing the means of two independent groups. In this case, it was used to compare the mean worldwide gross of movies released in a specific month to those released in all other months.

* Alternatives Considered: ANOVA could have been considered if comparing more than two groups (e.g., all months separately), but the t-test was sufficient for a focused comparison involving just one month against others.

#### Results

June:
T-statistic: 2.65, P-value: 0.009
The result is significant, so we reject the null hypothesis.

December:
T-statistic: 1.84, P-value: 0.067
The result is not significant, so we fail to reject the null hypothesis.
#### Interpretation
Movies released in June tend to have a higher worldwide gross compared to other months.

`Hypothesis 2: Correlation Between Budget and Worldwide Gross/Average Rating`


#### Test Used: Pearson's correlation coefficient and OLS regression.

* Reason: From some additional research, Pearson's correlation coefficient measures the strength and direction of the linear relationship between two continuous variables. It was chosen to assess the linear correlation between movie budgets and their gross earnings. OLS regression was used to quantify the relationship and determine how much of the variance in worldwide gross could be explained by the production budget.

* Alternatives Considered: Spearman's rank correlation could have been used if the data were not normally distributed or had outliers, as it does not assume normality and is less sensitive to outliers.

#### Results for Budget and Worldwide Gross Correlation

Pearson correlation coefficient: 0.6047184293264617
P-value: 3.683001512771247e-131
The result is significant, so we reject the null hypothesis.


| Term              | Coefficient | Std Error | t-stat  | P-value | 95% Conf. Interval |
|-------------------|-------------|-----------|---------|---------|--------------------|
| **const**         | -4.399e+06  | 4.15e+06  | -1.060  | 0.289   | -1.25e+07, 3.74e+06|
| **productionBudget** | 2.8982      | 0.106     | 27.429  | 0.000   | 2.691, 3.105       |

**Regression Statistics**

| Statistic        | Value         |
|------------------|---------------|
| **R-squared**    | 0.366         |
| **Adj. R-squared** | 0.365         |
| **F-statistic**  | 752.3         |
| **Prob (F-statistic)** | 3.68e-131   |
| **Log-Likelihood** | -26153.      |
| **AIC**          | 5.231e+04     |
| **BIC**          | 5.232e+04     |
| **No. Observations** | 1307        |
| **Df Residuals** | 1305          |
| **Df Model**     | 1             |

**Additional Statistics**

| Statistic        | Value         |
|------------------|---------------|
| **Omnibus**      | 1874.508      |
| **Prob(Omnibus)** | 0.000         |
| **Skew**         | 7.919         |
| **Kurtosis**     | 132.282       |
| **Durbin-Watson** | 1.932         |
| **Cond. No.**    | 4.97e+07      |
#### Interpretation
A moderate positive correlation exists between production budget and worldwide gross, suggesting that higher budgets are generally associated with higher gross earnings.

#### Results for Budget and Average Rating Correlation

Pearson correlation coefficient: 0.0337167681630076
P-value: 0.22317686277530505
The result is not significant, so we fail to reject the null hypothesis.

#### Interpretation
It appears that there is no significant correlation between movie's budget and its average rating on IMBD. This is an interesting finding since, even though our data supports that movies with bigger budget has a more statistically significant chance of grossing more, they might not be rated as proportionally high.


`Hypothesis 3: Directors' Influence on Average Rating
`

#### Test Used: Chi-squared test of independence.

* Reason: The chi-squared test is used to determine whether there is a significant association between two categorical variables. It was the appropriate choice to explore the relationship between the categorical variable of 'top director' status and the categorical classification of movie ratings (High/Low).

* Alternatives Considered: A logistic regression could have been used if the outcome was binary (e.g., high rating vs. low rating) and we wanted to control for other variables, but the chi-squared test was sufficient for the initial exploration of association.

#### Results

Chi-squared: 18.426203587056754

P-value: 1.7661254414638942e-05

The result is significant, so we reject the null hypothesis.

#### Interpretation
The result suggests that there is a significant relationship between whether a movie's director is on the top directors list and the movie's average rating category (High/Low).

There is evidence to suggest that the director being in the top list is not independent of the movie's average rating.

This could mean that movies directed by the most frequent directors in our dataset tend to have different average ratings compared to movies directed by others.

A significant contingency exists between movies directed by top directors and high ratings, indicating that top directors are more likely to direct highly-rated movies.

#### Methodology
The choice of tests was driven by the nature of our data and the specific hypotheses. We were very curious about the existence of these relationships between variables so we tried to find the most suitable tests. T-tests were used for comparing means, Pearson's correlation for linear relationships, and chi-squared tests for categorical associations.

#### Metrics
 We used P-values to assess statistical significance, with a standard alpha level of 0.05, as we did in class, labs, and assignments. 

 #### Challenges
 Evaluating the model required careful data cleaning, including handling missing values, duplicates, outliers, etc. Ensuring the assumptions of each statistical test were met also posed challenges.

 #### Data preparation
 Our biggest challenge in terms of data was having all the values filled for every row for tests we were running. Our hypotheses used differernt variables and we needed full rows for every variable. So to prepare our data and clean it, we dropped rows with missing critical information and filtered out anomalies that could skew the results such as directors that did not occur in our data at least 3 times as they cannot be assesed as 'top directors'.

 We also created new columns to categorize data effectively, such as the "ranking category" and "is_top_director".

#### Conclusion
The statistical analysis provided valuable insights into the movie industry, confirming that release dates, production budgets, and directorial influence *can* play significant roles in a movie's financial success and critical reception.


### Did you find the results corresponded with your initial belief in the data? If yes/no, why do you think this was the case?


#### Hypothesis 1: Release Date's Effect on Worldwide Gross
* Expectation: We anticipated that movies released during certain times of the year, specifically summer and Christmas holidays, would perform better due to higher audience turnout.

* Outcome: The significant result for June supported this belief, confirming the idea that release timing can impact box office performance. The non-significant result for December could be due to a variety of factors, such as increased competition during the holiday season or a smaller sample size of high-grossing movies.

#### Hypothesis 2: Correlation Between Budget and Worldwide Gross/Average Rating
* Expectation: It was presumed that movies with larger budgets would have higher gross earnings, potentially due to more substantial marketing efforts and production quality. Additionally, we expected that movies with higher budget would also score higher on the average ratings. 

* Outcome: The significant positive correlation confirmed this hypothesis, indicating that, as expected, there is a tendency for movies with higher budgets to earn more worldwide. However, earning more worldwide did not mean that movies were rated higher. We found no correlation between a movie's budget and its average rating. 

#### Hypothesis 3: Directors' Influence on Average Rating
* Expectation: We hypothesized that directors with a track record of success, as indicated by having multiple movies in top charts, would be more likely to produce highly-rated movies.

* Outcome: The significant result from the chi-squared test validated this hypothesis, suggesting that 'top directors' are indeed more likely to direct movies that receive higher average ratings.

Overall, the results were quite consistent with our initial beliefs, reinforcing the notion that certain factors such as release timing, budget, and directorial influence are pivotal in the success of a movie. 

The statistical significance of the findings provides a level of confidence in these results, although it's important to remember that correlation does not imply causation, and further research could be beneficial to explore these relationships in depth. 

The process of hypothesis testing also highlighted the importance of data preparation and the need to ensure that the data used in statistical tests is complete and clean to avoid skewed results.

#### Do you believe the tools for analysis that you chose were appropriate? If yes/no, why or what method could have been used?

Yes! The chosen tools for analysis were appropriate. The statistical tests used are standard methods for the types of data and hypotheses being investigated. They are widely recognized for their reliability in determining significance, correlation, and association in research data. 

Alternative methods could include regression analysis for more detailed relationships or non-parametric tests if the data did not meet certain assumptions, but the chosen methods were well-suited for the initial exploration of the hypotheses.

#### Was the data adequate for your analysis? If not, what aspects of the data were problematic and how could you have remedied that?
The data was largely adequate for our analysis, as it allowed us to test our hypotheses with statistical methods. However, there were challenges and things that could have made our project's results more reliable as well as could have made our work a bit easier:

* Completeness: Any missing values, especially in key variables like budget or worldwide gross, could skew results. Remedying this would involve sourcing missing data or employing imputation techniques where appropriate.

* Outliers: Extreme values can affect the results of statistical tests. We could mitigate this by using robust statistical methods or by carefully filtering outliers.

* Sample Size: A larger dataset might provide more reliable insights, particularly for less common release dates or for directors with fewer movies.

However, despite all the challanges, we are quite happy with our finding and results!