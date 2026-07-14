import streamlit as st

from utils.data_loader import load_customers
from services.segmentation import add_segments
from services.recommendation_engine import add_recommendations


st.title("Next Best Action Recommendations")

st.markdown(
"""
This module provides explainable recommendations generated
using business rules based on customer behaviour.
"""
)


df = load_customers()

df = add_segments(df)

df = add_recommendations(df)


priority = st.selectbox(
    "Filter Priority",
    ["All", "High", "Medium", "Low"]
)


if priority != "All":
    df = df[df["priority"] == priority]


recommendation = st.selectbox(
    "Filter Recommendation",
    ["All"] + list(df["recommendation"].unique())
)


if recommendation != "All":
    df = df[
        df["recommendation"] == recommendation
    ]


st.subheader(
    f"{len(df)} Customers Identified"
)


st.dataframe(
    df[
        [
            "customer_id",
            "name",
            "segment",
            "recommendation",
            "priority",
            "reason"
        ]
    ],
    use_container_width=True
)


st.download_button(
    "Export Recommendations",
    df.to_csv(index=False),
    "customer_recommendations.csv",
    "text/csv"
)