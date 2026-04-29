import pandas as pd

deliveries_df = pd.read_csv("../data/deliveries.csv")
matches_df = pd.read_csv("../data/matches.csv")

print("Datasets are loaded successfully.")

print("Checking for missing values: ")

print("Deliveries missing values:")
print(deliveries_df.isnull().sum())

print("Matches missing values:")
print(matches_df.isnull().sum())

print("Validating match id alignment: ")

deliveries_match_ids = set(deliveries_df["match_id"].unique())
matches_ids = set(matches_df["id"].unique())

missing_in_matches = deliveries_match_ids - matches_ids
missing_in_deliveries = matches_ids - deliveries_match_ids

print(f"\nMatch IDs in deliveries but not in matches: {len(missing_in_matches)}")
print(f"Match IDs in matches but not in deliveries: {len(missing_in_deliveries)}")

print("Validating data tyoes: ")

print("\nDeliveries Data Types:\n")
print(deliveries_df.dtypes)

print("\nMatches Data Types:\n")
print(matches_df.dtypes)

print("Performing basic cleaning: ")

matches_df["winner"] = matches_df["winner"].fillna("No Result")
matches_df["player_of_match"] = matches_df["player_of_match"].fillna("Not Awarded")

print("\nBasic cleaning completed.")

print("Final dataframe shapes: ")

print(f"\nDeliveries Shape: {deliveries_df.shape}")
print(f"Matches Shape: {matches_df.shape}")