from data_loader import load_data
from cleaning import clean_data
from transformation import transform_data
from analysis import *
from insights import generate_insights

# STAGE 1: Data Ingestion
deliveries_df, matches_df = load_data()

# STAGE 2: Data Cleaning and Validation
deliveries_df, matches_df = clean_data(
    deliveries_df,
    matches_df
)

# STAGE 3: Data Transformation
merged_df = transform_data(
    deliveries_df,
    matches_df
)

print("\nPipeline execution completed successfully. Starting analysis...\n")

# Stage 4: Core Analysis
total_runs_per_match(merged_df)
runs_per_team_per_match(merged_df)
top_10_batters(merged_df)
strike_rate(merged_df)
top_bowlers_by_economy(merged_df)
most_consistent_batters(merged_df)
highest_individual_score(merged_df)
boundary_analysis(merged_df)
boundary_percentage(merged_df)
dot_ball_analysis(merged_df)
runs_per_over(merged_df)
powerplay_performance(merged_df)
death_overs_performance(merged_df)
run_distribution_per_inning(merged_df)
toss_impact_analysis(merged_df)
toss_match_win_analysis(merged_df)
player_of_match_contribution(merged_df)
venue_wise_analysis(merged_df)
city_wise_scoring(merged_df)
season_wise_run_trends(merged_df)
winning_team_analysis(merged_df)

# Stage 5: Derived Insights
generate_insights(merged_df)