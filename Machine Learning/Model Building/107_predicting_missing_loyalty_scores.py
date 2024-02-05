# -*- coding: utf-8 -*-
"""
@author: helen

Predicting missing loyalty scores using prepared model
"""

# import required packages
import pandas as pd
import pickle

# import customers for scoring
to_be_scored_0_loaded = pickle.load(
    open("data/regression_scoring.p", "rb"))

regressor = pickle.load(
    open("data/random_forest_regressor.p", "rb"))

one_hot_encoder = pickle.load(
    open("data/random_forest_regressor_ohe.p", "rb"))

# drop unused data
to_be_scored_1_unused_dropped = to_be_scored_0_loaded.drop(
    ["customer_id"], axis=1)

# drop missing data

to_be_scored_2_missing_dropped = to_be_scored_1_unused_dropped.dropna(
    how="any")

# encode categorical variables

categorical_vars = ["gender"]
encoder_vars_array = one_hot_encoder.transform(
    to_be_scored_2_missing_dropped[categorical_vars])
encoder_feature_names = one_hot_encoder.get_feature_names_out(categorical_vars)
encoder_vars_df = pd.DataFrame(
    encoder_vars_array, columns=encoder_feature_names)
to_be_scored_3_encoded = pd.concat(
    [to_be_scored_2_missing_dropped.reset_index(drop=True), encoder_vars_df.reset_index(drop=True)], axis=1)

to_be_scored_4_old_cat_dropped = to_be_scored_3_encoded.drop(
    categorical_vars, axis=1)

# make the predictions
loyalty_predictions = regressor.predict(to_be_scored_4_old_cat_dropped)
