# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:04:50 2023

@author: helen

chi square test
"""

# Import required packages
import pandas as pd
from scipy.stats import chi2_contingency, chi2

# Import Data
campaign_data = pd.read_excel(
    "grocery_database.xlsx", sheet_name="campaign_data")

# Filter data - remove the control rows we dont need for this test

campaign_data = campaign_data.loc[campaign_data["mailer_type"] != "Control"]

# Summarise to get observed frequencies

observed_values = pd.crosstab(
    campaign_data["mailer_type"], campaign_data["signup_flag"]).values

mailer1_signup_rate = 123 / (252 + 123)
mailer2_signup_rate = 127 / (209 + 127)
print(mailer1_signup_rate, mailer2_signup_rate)

# State hypothesis & set acceptance criteria

null_hypothesis = "There is no relationship between mailer type and signup rate.  They are independent"
alternate_hypothesis = "There is a relationship between mailer type and signup rate.  They are not independent"
acceptance_criteria = 0.05

# calculate the expected frequencies and chi square statistic
chi2_statistic, p_value, dof, expected_values = chi2_contingency(
    observed_values, correction=False)

# find the critical value for the test
critical_value = chi2.ppf(1 - acceptance_criteria, dof)

print(critical_value)

# print the result with chi square statistic

if chi2_statistic >= critical_value:
    print(
        f"As our chi-square statistic {chi2_statistic} is higher than our critical value of {critical_value} we reject the null hypothesis and conclude that {alternate_hypothesis}.")
else:
    print(
        f"As our chi-square statistic {chi2_statistic} is lower than our critical value of {critical_value} we retain the null hypothesis and conclude that {null_hypothesis}.")

# print the results with p-value probability distribution value?
if p_value <= acceptance_criteria:
    print(
        f"As our p_value probability {p_value} is lower than our acceptance value of {acceptance_criteria} we reject the null hypothesis and conclude that {alternate_hypothesis}.")
else:
    print(
        f"As our p_value probability {p_value} is higher than our acceptance value of {acceptance_criteria} we retain the null hypothesis and conclude that {null_hypothesis}.")
