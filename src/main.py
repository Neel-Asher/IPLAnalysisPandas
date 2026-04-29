import pandas as pd

# STAGE 1: Data Loading and Initial Exploration
deliveries_df = pd.read_csv("../data/deliveries.csv")
matches_df = pd.read_csv("../data/matches.csv")

print("Datasets are loaded successfully.")

# STAGE 2: Data Validation and Cleaning
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

# STAGE 3: Data Transformation
print("Starting data transformation: ")

deliveries_df.columns = deliveries_df.columns.str.lower().str.strip()
matches_df.columns = matches_df.columns.str.lower().str.strip()

print("\nColumn names standardized.")

deliveries_df["total_runs"] = (
    deliveries_df["batsman_runs"] +
    deliveries_df["extra_runs"]
)

print("\nNew column 'total_runs' created.")

merged_df = deliveries_df.merge(
    matches_df,
    left_on="match_id",
    right_on="id",
    how="inner"
)

print("\nDatasets merged successfully.")

print("Merged dataset info: ")

print("\nMerged Shape:")
print(merged_df.shape)

print("\nMerged Columns:")
print(merged_df.columns)

print("\nFirst 5 Rows:")
print(merged_df.head())