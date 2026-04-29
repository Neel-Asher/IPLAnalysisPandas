def clean_data(deliveries_df, matches_df):

    matches_df["winner"] = matches_df["winner"].fillna("No Result")
    matches_df["player_of_match"] = matches_df["player_of_match"].fillna("Not Awarded")

    deliveries_df.columns = deliveries_df.columns.str.lower().str.strip()
    matches_df.columns = matches_df.columns.str.lower().str.strip()

    return deliveries_df, matches_df