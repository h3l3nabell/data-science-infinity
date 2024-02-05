# -*- coding: utf-8 -*-
"""
@author: helen

Linear Regression ABC Grocery Task
"""
###############################################################
# import required packages
###############################################################
import pandas as pd
import pickle
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.utils import shuffle
from sklearn.preprocessing import OneHotEncoder
from sklearn.feature_selection import RFECV
from sklearn.model_selection import cross_val_score, KFold, StratifiedKFold

pd.__version__

###############################################################
# read in data
###############################################################
data_for_model_0_loaded = pickle.load(
    open("data/regression_modelling.p", "rb"))

# test_pickle = pickle.load(
#    open("data/abc_classification_modelling.p", "rb"))

###############################################################
# drop unnecessary columns
###############################################################
data_for_model_1_cd = data_for_model_0_loaded.drop(
    "customer_id", axis=1)


# shuffle data
data_for_model_2_shuffled = shuffle(
    data_for_model_1_cd, random_state=42)

# check for missing values

data_for_model_2_shuffled.isna().sum()
data_for_model_3_mvr = data_for_model_2_shuffled.dropna(
    how="any")

###############################################################
# deal with outliers
###############################################################

outlier_investigation = data_for_model_3_mvr.describe()

# from outliers in data prep
outlier_columns = ["distance_from_store",
                   "total_sales_cost", "total_num_items"]

data_for_model_4_or = data_for_model_3_mvr

# remove outliers
for column in outlier_columns:
    lower_quartile = data_for_model_4_or[column].quantile(
        0.25)
    upper_quartile = data_for_model_4_or[column].quantile(
        0.75)
    interquartilerange = upper_quartile - lower_quartile
    iqr_extended = interquartilerange * 2
    min_border = lower_quartile - iqr_extended
    max_border = upper_quartile + iqr_extended
    print(f"lower quartile={lower_quartile} and min border={min_border}")
    print(f"upper quartile={upper_quartile} and max border={max_border}")
    outliers = data_for_model_4_or[(data_for_model_4_or[column] < min_border) | (
        data_for_model_4_or[column] > max_border)].index
    print(f"{len(outliers)} outliers detected in column {column}")
    data_for_model_4_or = data_for_model_4_or.drop(
        outliers)

###############################################################
# separate input and output data
###############################################################
X = data_for_model_4_or.drop(["customer_loyalty_score"], axis=1)
y = data_for_model_4_or["customer_loyalty_score"]

# split out test set and training set
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

###############################################################
# deal with categorical variables
###############################################################

categorical_vars = ["gender"]

# Here sparse=False means we return an array rather than a  sparse object
# the drop = first will tell it to drop the first of the encoded values
# this avoids the dummy variable trap - and you dont lose any info for ML - the
# dropped value would have been 1 whenever the others were all zero.
one_hot_encoder = OneHotEncoder(sparse=False, drop="first")

x_train_encoded = one_hot_encoder.fit_transform(x_train[categorical_vars])
x_test_encoded = one_hot_encoder.transform(x_test[categorical_vars])

encoder_feature_names = one_hot_encoder.get_feature_names_out(categorical_vars)

x_train_encoded = pd.DataFrame(
    x_train_encoded, columns=encoder_feature_names)

# the reset index ensures that no rows are not aligned.
x_train = pd.concat(
    [x_train.reset_index(drop=True), x_train_encoded.reset_index(drop=True)], axis=1)

x_train = x_train.drop(categorical_vars, axis=1)


x_test_encoded = pd.DataFrame(
    x_test_encoded, columns=encoder_feature_names)

# the reset index ensures that no rows are not aligned.
x_test = pd.concat(
    [x_test.reset_index(drop=True), x_test_encoded.reset_index(drop=True)], axis=1)

x_test = x_test.drop(categorical_vars, axis=1)

###############################################################
# Feature Selection
###############################################################

regressor = LinearRegression()
feature_selector = RFECV(regressor, cv=5)

# Train model using 5 chunks
fit = feature_selector.fit(x_train, y_train)

# Once model trained we can find out what the optimal number of variables are,
# and which variables they are

optimal_feature_count = feature_selector.n_features_
print(f"The optimal number of features is: {optimal_feature_count}")

# create some dataframes so we can investigate
# f_scores_df = pd.DataFrame(fit.get_feature_names_out())
# input_variable_names = pd.DataFrame(x_test.columns)

x_train = x_train.loc[:, feature_selector.get_support()]
x_test = x_test.loc[:, feature_selector.get_support()]

plt.plot(range(1, len(fit.cv_results_["mean_test_score"]) + 1),
         fit.cv_results_["mean_test_score"], marker="o")
plt.ylabel = "Model Scores"
plt.xlabel = "Number of Features"
plt.title(
    f"Feature Selection using RFE \n Optimal number of features is {optimal_feature_count} (at score of : {round(max(fit.cv_results_['mean_test_score']),4)})")
plt.tight_layout()
plt.show()

###############################################################
# create regression object
###############################################################
regressor = LinearRegression()

# train model
regressor.fit(x_train, y_train)


###############################################################
# Assess Model Accuracy
###############################################################

# predict on the test set
y_pred = regressor.predict(x_test)

# calculate r-squared
r_squared = r2_score(y_test, y_pred)
print(r_squared)

# cross validation
cv = KFold(n_splits=4, shuffle=True, random_state=42)
cv_scores = cross_val_score(regressor, x_train, y_train, cv=cv, scoring="r2")
print(cv_scores.mean())

# caculate adjusted R-squared
num_data_points, num_input_vars = x_test.shape
adjusted_r_squared = 1 - \
    (1 - r_squared) * (num_data_points - 1) / \
    (num_data_points - num_input_vars - 1)
print(adjusted_r_squared)

# extract model coefficents
# the wieighting of each parameter
coefficients = pd.DataFrame(regressor.coef_)
input_variable_names = pd.DataFrame(x_train.columns)
summary_stats = pd.concat([input_variable_names, coefficients], axis=1)
summary_stats.columns = ["input_variable", "coefficient"]

# extract model intercept
model_intercept = regressor.intercept_
