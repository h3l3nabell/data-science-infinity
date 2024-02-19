# -*- coding: utf-8 -*-
"""
@author: helen

Association Rule Learning using Apriori - Advanced Template
"""
######################################
# import required packages
######################################
import pandas as pd
from apyori import apriori


######################################
# import data
######################################
data_for_model_0_loaded = pd.read_csv("data/sample_data_apriori.csv")

# drop unnecessary columns
data_for_model_1_cd = data_for_model_0_loaded.drop(
    "transaction_id", axis=1)


# prepare data as a list of lists for apriori algorithm

transactions_list = []
for index, row in data_for_model_1_cd.iterrows():
    transaction = list(row.dropna())
    transactions_list.append(transaction)

transactions_list


######################################
# apply the apriori algorithm
######################################
apriori_rules = apriori(transactions_list,
                        min_support=0.003,
                        min_confidence=0.2,
                        min_lift=3,
                        min_length=2,
                        max_length=2)

apriori_rules_list = list(apriori_rules)

######################################
# Convert the resulting mess to a dataframe
######################################
apriori_rules_list[0][2][0][0]

product1 = [list(rule[2][0][0])[0] for rule in apriori_rules_list]
product2 = [list(rule[2][0][1])[0] for rule in apriori_rules_list]

support = [rule[1] for rule in apriori_rules_list]
confidence = [rule[2][0][2] for rule in apriori_rules_list]
lift = [rule[2][0][3] for rule in apriori_rules_list]

apriori_rules_df = pd.DataFrame({"product1": product1,
                                 "product2": product2,
                                 "support": support,
                                 "confidence": confidence,
                                 "lift": lift})

######################################
# Sort rules by descending lift
######################################
apriori_rules_df_sorted = apriori_rules_df.sort_values(by="lift",
                                                       ascending=False)

######################################
# search rules
######################################

apriori_rules_df_sorted[apriori_rules_df_sorted["product1"].str.contains("Bar")]
