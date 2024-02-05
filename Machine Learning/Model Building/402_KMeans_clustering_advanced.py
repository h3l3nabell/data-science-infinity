# -*- coding: utf-8 -*-
"""
@author: helen

K Means Clustering Advanced - Customer Profiling for ABC Grocery
"""
######################################
# import required packages
######################################
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import matplotlib.pyplot as plt


######################################
# create the data
######################################


# import tables

transactions = pd.read_excel(
    "data/grocery_database.xlsx", sheet_name="transactions")

product_areas = pd.read_excel(
    "data/grocery_database.xlsx", sheet_name="product_areas")

# merge on product area name

model_data_0 = pd.merge(
    transactions, product_areas, how="inner", on="product_area_id")

# drop the non-food category

model_data_1 = model_data_0.drop(
    model_data_0[model_data_0["product_area_name"] == "Non-Food"].index)

# aggregate sales at customer level by product area

transactions_summary = model_data_1.groupby(
    ["customer_id", "product_area_name"])["sales_cost"].sum().reset_index()

# pivot data to place product areas as columns

transaction_summary_pivot = model_data_1.pivot_table(index="customer_id",
                                                     columns="product_area_name",
                                                     values="sales_cost",
                                                     aggfunc="sum",
                                                     fill_value=0,
                                                     margins=True,
                                                     margins_name="Total").rename_axis(None, axis=1)

# turn sales = % sales

transaction_summary_pivot_1 = transaction_summary_pivot.div(
    transaction_summary_pivot["Total"], axis=0)


# drop the total column

data_for_clustering = transaction_summary_pivot_1.drop(["Total"], axis=1)

######################################
# data preparation and cleaning
######################################

# check for missing values
data_for_clustering.isna().sum()

# feature scaling - normalise data

scale_normaliser = MinMaxScaler()
data_for_clustering_scaled = pd.DataFrame(scale_normaliser.fit_transform(
    data_for_clustering), columns=data_for_clustering.columns)

######################################
# use WCSS to find a good value for k
######################################

k_values = list(range(1, 10))
wcss_list = []

for k in k_values:
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(data_for_clustering_scaled)
    wcss_list.append(kmeans.inertia_)

# plot the k values to find the elbow

plt.plot(k_values, wcss_list)
plt.title = "Within Cluster Sum of Squares by K"
plt.xlabel("K")
plt.ylabel("WCSS Score")
plt.tight_layout()
plt.show()

######################################
# instantiate and fit the model
######################################

kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(data_for_clustering_scaled)

######################################
# Add the cluster labels to our df
######################################
data_for_clustering["cluster"] = kmeans.labels_
data_for_clustering["cluster"].value_counts()

######################################
# profile our clusters
######################################
cluster_summary = data_for_clustering.groupby(
    "cluster")[["Dairy", "Fruit", "Meat", "Vegetables"]].mean().reset_index()
