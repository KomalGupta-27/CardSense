import pandas as pd
def generate_recommendation(row):

    recommendation = "Lifestyle Benefits Campaign"
    priority = "Low"
    reason = "Customer profile suitable for engagement offers"
    

    if row["travel_spend"] > 150000:

        recommendation = "Premium Travel Card Upgrade"
        priority = "High"
        reason = (
            "High travel spending indicates interest "
            "in travel benefits"
        )


    elif (
        row["credit_utilization"] > 80
        and row["late_payments"] == 0
    ):

        recommendation = "Credit Limit Increase"
        priority = "High"
        reason = (
            "High utilization with strong repayment behaviour"
        )


    elif row["reward_points"] > 25000:

        recommendation = "Reward Redemption Campaign"
        priority = "Medium"
        reason = (
            "Large unused reward balance detected"
        )


    elif row["inactive_days"] > 90:

        recommendation = "Customer Retention Offer"
        priority = "High"
        reason = (
            "Customer inactive for extended period"
        )


    elif row["current_balance"] > 200000:

        recommendation = "EMI Conversion Offer"
        priority = "Medium"
        reason = (
            "High outstanding balance detected"
        )


    return pd.Series(
        [
            recommendation,
            priority,
            reason
        ]
    )



def add_recommendations(df):

    import pandas as pd

    results = df.apply(
        generate_recommendation,
        axis=1
    )

    results.columns = [
        "recommendation",
        "priority",
        "reason"
    ]

    df = pd.concat(
        [
            df,
            results
        ],
        axis=1
    )

    return df