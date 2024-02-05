# -*- coding: utf-8 -*-
"""
 MatPlotLib - saving plots
"""

import matplotlib.pyplot as plt
import pandas as pd

body_data = pd.read_csv("weights_and_heights.csv")
male = body_data[body_data["Gender"] == "Male"]
female = body_data[body_data["Gender"] == "Female"]

male_sample = male.sample(200, random_state=42)
patient = male_sample.loc[[705]]

median_weight = male_sample["Weight"].median()
median_height = male_sample["Height"].median()

min_weight = male_sample["Weight"].min()
min_height = male_sample["Height"].min()

plt.style.available
plt.style.use("seaborn-v0_8-poster")

plt.scatter(male_sample["Weight"], male_sample["Height"],
            color="blue", s=500, alpha=0.5)
plt.scatter(patient["Weight"], patient["Height"],
            color="salmon", s=500, alpha=1.0, edgecolor="magenta", linewidth=2)

# plt.scatter(patient["Weight"], patient["Height"],
#            color="black", marker="x",  s=250, alpha=1.0, linewidth=5)

plt.title("Weight vs Height for Males")
plt.xlabel("Weight (lbs)")
plt.ylabel("Height (in)")

plt.axvline(x=median_weight, color="black", linestyle="--")
plt.axhline(y=median_height, color="black", linestyle="--")

# plt.annotate(text="Median Weight", xy=(190, 60), fontsize=16)
plt.annotate(text=f"Median Weight ({round(median_weight)} lbs)",
             xy=(median_weight, min_height),
             xytext=(10, -10), textcoords="offset pixels", fontsize=16)

plt.annotate(text=f"Median Height ({round(median_height)} ins)",
             xy=(min_weight, median_height),
             xytext=(-10, 10), textcoords="offset pixels", fontsize=16)

plt.annotate(text="Patient 705",
             xy=(patient["Weight"], patient["Height"]),
             xytext=(140, 74),
             fontsize=25,
             bbox=dict(boxstyle="round",
                       fc="salmon",
                       ec="red"),
             arrowprops=dict(arrowstyle="wedge,tail_width=1.",
                             fc="salmon",
                             ec="red",
                             patchA=None,
                             connectionstyle="arc3,rad=-0.1"))

plt.tight_layout()
plt.savefig(fname="exported_plot.png")
plt.show()
