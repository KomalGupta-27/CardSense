def assign_segment(row):

    if row["monthly_spend"] > 150000 and row["annual_income"] > 2000000:
        return "High Value Customer"

    elif row["travel_spend"] > 100000:
        return "Frequent Traveller"

    elif row["reward_points"] > 30000:
        return "Reward Maximizer"

    elif row["credit_utilization"] > 80:
        return "High Utilization"

    elif row["inactive_days"] > 90:
        return "Dormant Customer"

    elif row["salary_growth"] > 20:
        return "Premium Candidate"

    elif row["relationship_years"] > 8:
        return "Loyal Customer"

    else:
        return "Regular Customer"



def add_segments(df):

    df["segment"] = df.apply(
        assign_segment,
        axis=1
    )

    return df