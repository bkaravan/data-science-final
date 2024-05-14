## Notes on Permutation Importance Visualization

- Why did you pick this representation?

  - The stacked boxplots provide a great visual comparison of feature permutation importance. To determine feature permutation importance, the model is re-evaluated over a series of shuffled perturbed features. To create a robust representation of permutation feature importance, we re-evaluate over many randomstates, giving us a distribution of feature importance. The box plot provides a great visualization of the distribution. The box plot is also robust against outliers, while a mean representation would be skewed by outliers.

- What alternative ways might you communicate the result?

  - A bar plot could have also been used to represent the mean permutation importance of each feature, but doesn't account for the distribution of importance.

- Were there any challenges visualizing the results, if so, what were they?

  - The only challenge faced was limiting the number of features. We didn't want to display all the features and their importances, only the top ones, and also sort them. This was achieved by some result array manipulation to get a sorted top 10 features and their values.

- Will your visualization require text to provide context or is it standalone (either is fine, but it’s recognized which type your visualization is)?

  - This visualization does not require text, and could be used standalone. It may be helpful to provide a brief explanation of permutation importance, if unfamiliar, as well as the model being evaluated (in this case Random Forest).
