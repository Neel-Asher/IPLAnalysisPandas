import pandas as pd

deliveries_df = pd.read_csv("../data/deliveries.csv")
matches_df = pd.read_csv("../data/matches.csv")

print("DELIVERIES DATASET")
print(deliveries_df.shape)
print(deliveries_df.columns)
print(deliveries_df.dtypes)

print("")

print("MATCHES DATASET")
print(matches_df.shape)
print(matches_df.columns)
print(matches_df.dtypes)