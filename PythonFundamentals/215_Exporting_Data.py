# -*- coding: utf-8 -*-
"""
 Pandas - exporting data
"""

import pandas as pd
import numpy as np

my_df = pd.DataFrame({"A": [1, 2, 3],
                      "B": ["one", np.nan, "three"]})

my_df.to_csv("testcsv_export.csv", index=False)

my_df.to_csv("testcsv_export.csv", index=False, columns=["B"])

my_df.to_csv("testcsv_export.csv", index=False, header=False)

my_df.to_csv("testcsv_export.csv", index=False, na_rep="Missing")

my_df.to_csv("testcsv_export.txt", index=False, na_rep="Missing")

my_df.to_csv("testcsv_export.txt", index=False, sep="\t")

my_df.to_excel("test_export.xlsx", sheet_name="helen")

# write 2 dataframes to different sheets
my_other_df = my_df * 3

with pd.ExcelWriter("test_export2.xlsx") as excel_writer:
    my_df.to_excel(excel_writer, sheet_name="helen1")
    my_other_df.to_excel(excel_writer, sheet_name="helen2")

# weird unicode escape error! because of the \U
my_df.to_csv("C:\Users\helen\OneDrive\Desktop\test_export.csv", index=False)

# fix 1
my_df.to_csv(
    "C:\\Users\\helen\\OneDrive\\Desktop\\test_export.csv", index=False)

# fix 2 - raw string
my_df.to_csv(r"C:\Users\helen\OneDrive\Desktop\test_export.csv", index=False)
