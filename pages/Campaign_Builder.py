import streamlit as st

from utils.data_loader import load_customers
from services.segmentation import add_segments
from services.recommendation_engine import add_recommendations


st.title("Campaign Builder")


st.markdown(
"""
Create targeted customer campaigns using
customer insights and recommendation rules.
"""
)


df = load_customers()

df = add_segments(df)

df = add_recommendations(df)



campaigns = {

    "Premium Upgrade Campaign":
        "Premium Card Upgrade",

    "Travel Rewards Campaign":
        "Premium Travel Card Upgrade",

    "Retention Campaign":
        "Customer Retention Offer",

    "EMI Conversion Campaign":
        "EMI Conversion Offer",

    "Rewards Campaign":
        "Reward Redemption Campaign"

}



campaign = st.selectbox(
    "Select Campaign",
    list(campaigns.keys())
)



target_action = campaigns[campaign]



eligible = df[
    df["recommendation"] == target_action
]



st.subheader(
    "Campaign Audience"
)


st.metric(
    "Eligible Customers",
    len(eligible)
)



st.dataframe(
    eligible[
        [
            "customer_id",
            "name",
            "city",
            "card_type",
            "monthly_spend",
            "recommendation",
            "reason"
        ]
    ],
    use_container_width=True
)



st.download_button(
    "Export Campaign List",
    eligible.to_csv(index=False),
    "campaign_audience.csv",
    "text/csv"
)