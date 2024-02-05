# -*- coding: utf-8 -*-
"""
@author: helen

Independent Sample T Test
"""

# Import required packages
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, norm

# Create Sample Data

# norm.rvs creates random variables in a normal distribution
# loc = the mean!  scalse = standard deviation!  size = #datapoints

sample_a = norm.rvs(loc=500, scale=100, size=250,
                    random_state=42).astype(int)

sample_b = norm.rvs(loc=550, scale=150, size=100,
                    random_state=42).astype(int)


plt.hist(sample_a, density=True, alpha=0.5)
plt.hist(sample_b, density=True, alpha=0.5)
plt.show()

sample_a_mean = sample_a.mean()
sample_b_mean = sample_b.mean()

print(sample_a_mean, sample_b_mean)

# State hypothesis & set acceptance criteria

null_hypothesis = "The mean of the sample a is equal to the mean of the sample b"
alternate_hypothesis = "The mean of the sample a is not equal to the mean of the sample b"
acceptance_criteria = 0.05

# Execute the hypothesis test
t_statistic, p_value = ttest_ind(sample_a, sample_b)
print(t_statistic, p_value)

# print the results with p-value probability distribution value?
if p_value <= acceptance_criteria:
    print(
        f"As our p_value probability {p_value} is lower than our acceptance value of {acceptance_criteria} we reject the null hypothesis and conclude that {alternate_hypothesis}.")
else:
    print(
        f"As our p_value probability {p_value} is higher than our acceptance value of {acceptance_criteria} we retain the null hypothesis and conclude that {null_hypothesis}.")

# welches T Test - more reliable when sample sizes are different.  Best practice

# Execute the hypothesis test
t_statistic, p_value = ttest_ind(sample_a, sample_b, equal_var=False)
print(t_statistic, p_value)

# print the results with p-value probability distribution value?
if p_value <= acceptance_criteria:
    print(
        f"As our p_value probability {p_value} is lower than our acceptance value of {acceptance_criteria} we reject the null hypothesis and conclude that {alternate_hypothesis}.")
else:
    print(
        f"As our p_value probability {p_value} is higher than our acceptance value of {acceptance_criteria} we retain the null hypothesis and conclude that {null_hypothesis}.")

# the result is the same but we are less confident in the difference
