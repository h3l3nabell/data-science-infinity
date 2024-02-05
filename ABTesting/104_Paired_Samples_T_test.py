# -*- coding: utf-8 -*-
"""
@author: helen

Paired Sample T Test
"""

# Import required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_rel, norm

# Create Sample Data

# norm.rvs creates random variables in a normal distribution
# loc = the mean!  scalse = standard deviation!  size = #datapoints

before = norm.rvs(loc=500, scale=100, size=100,
                  random_state=42).astype(int)

np.random.seed(42)
after = before + np.random.randint(-50, 75, size=100)

plt.hist(before, density=True, alpha=0.5, label="before")
plt.hist(after, density=True, alpha=0.5, label="after")
plt.legend()
plt.show()

before_mean = before.mean()
after_mean = after.mean()

print(before_mean, after_mean)

# State hypothesis & set acceptance criteria

null_hypothesis = "The mean of the before is equal to the mean of the after"
alternate_hypothesis = "The mean of the before is not equal to the mean of the after"
acceptance_criteria = 0.05

# Execute the hypothesis test
t_statistic, p_value = ttest_rel(before, after)
print(t_statistic, p_value)

# print the results with p-value probability distribution value?
if p_value <= acceptance_criteria:
    print(
        f"As our p_value probability {p_value} is lower than our acceptance value of {acceptance_criteria} we reject the null hypothesis and conclude that {alternate_hypothesis}.")
else:
    print(
        f"As our p_value probability {p_value} is higher than our acceptance value of {acceptance_criteria} we retain the null hypothesis and conclude that {null_hypothesis}.")
