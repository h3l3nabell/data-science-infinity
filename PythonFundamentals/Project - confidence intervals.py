# -*- coding: utf-8 -*-
"""
  We have a single sample of data
  Based on this, we want to calculate the confidence interval
  around the sample mean


   CI = mean x +/- Z * s/sqrt(n)

   Z - we want a confidence interval of 95%
   s = standard deviation of our sample of heights
   x = mean of our sample of heights
   n = our sample size
"""


import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

body_data = pd.read_csv("weights_and_heights.csv")
female = body_data[body_data["Gender"] == "Female"]
female_sample = female.sample(200)

mean_height = female_sample["Height"].mean()
std_height = female_sample["Height"].std()
min_height = female_sample["Height"].min()
max_height = female_sample["Height"].max()

# lets see if we can get a frequency distribution to plot!

heights = female_sample["Height"]

# splits height data into bins of size 1 inch
# start, stop, step defaults to 1
height_bins = np.arange(0, max_height, 1)

cut = pd.cut(heights, bins=height_bins,
             labels=height_bins[:-1], right=False).reset_index()


grouped = cut.groupby()

# sort out this scribbly plot!
plt.style.available
plt.style.use("seaborn-v0_8-dark")

plt.plot(counts,
         color="darkmagenta", alpha=0.5)


plt.title("Height for sample of 200 Females")
#plt.xlabel("Weight (lbs)")
plt.ylabel("Height (in)")

plt.axhline(y=mean_height, color="black", linestyle="--")

plt.annotate(text=f"Mean Height ({round(mean_height)} ins)",
             xy=(0, mean_height),
             xytext=(-10, 10), textcoords="offset pixels", fontsize=16)

plt.tight_layout()
plt.savefig(fname="confidence_intervals_plot.png")
plt.show()
