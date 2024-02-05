# -*- coding: utf-8 -*-
"""
@author: helen

One Sample T Test
"""

# Import required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_1samp, norm

# Create Sample Data

# norm.rvs creates random variables in a normal distribution
# loc = the mean!  scalse = standard deviation!  size = #datapoints
# random state kind of seeds the random algorithm

population = norm.rvs(loc=500, scale=100, size=1000,
                      random_state=42).astype(int)

# again seeding our random data for the sample
np.random.seed(42)
sample = np.random.choice(population, 250)

plt.hist(population, density=True, alpha=0.5)
plt.hist(sample, density=True, alpha=0.5)
plt.show()

population_mean = population.mean()
sample_mean = sample.mean()

print(population_mean, sample_mean)

# State hypothesis & set acceptance criteria

null_hypothesis = "The mean of the sample is equal to the mean of the population"
alternate_hypothesis = "The mean of the sample is not equal to the mean of the population"
acceptance_criteria = 0.05

# Execute the hypothesis test
t_statistic, p_value = ttest_1samp(sample, population_mean)
print(t_statistic, p_value)

# print the results with p-value probability distribution value?
if p_value <= acceptance_criteria:
    print(
        f"As our p_value probability {p_value} is lower than our acceptance value of {acceptance_criteria} we reject the null hypothesis and conclude that {alternate_hypothesis}.")
else:
    print(
        f"As our p_value probability {p_value} is higher than our acceptance value of {acceptance_criteria} we retain the null hypothesis and conclude that {null_hypothesis}.")
