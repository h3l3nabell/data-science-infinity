# -*- coding: utf-8 -*-
"""
 MatPlotLib - highlighting data
"""

import matplotlib.pyplot as plt
import pandas as pd

body_data = pd.read_csv("weights_and_heights.csv")
male = body_data[body_data["Gender"] == "Male"]
female = body_data[body_data["Gender"] == "Female"]

male_sample = male.sample(200, random_state=42)
patient = male_sample.loc[[705]]

plt.style.available
plt.style.use("seaborn-v0_8-poster")

plt.scatter(male_sample["Weight"], male_sample["Height"],
            color="blue", s=500, alpha=0.5)
plt.scatter(patient["Weight"], patient["Height"],
            color="magenta", s=500, alpha=1.0, edgecolor="red", linewidth=2)

plt.scatter(patient["Weight"], patient["Height"],
            color="black", marker="x",  s=250, alpha=1.0, linewidth=5)

plt.title("Weight vs Height for Males")
plt.xlabel("Weight (lbs)")
plt.ylabel("Height (in)")

plt.axvline(x=male_sample["Weight"].median(), color="black", linestyle="--")
plt.axhline(y=male_sample["Height"].median(), color="black", linestyle="--")

# plt.legend()
plt.tight_layout()
plt.show()
