import streamlit as st
import plotly.express as px

from utils.data_loader import load_customers
from services.segmentation import add_segments
from services.recommendation_engine import add_recommendations


st.set_page_config(
    page_title="CardSense",
    page_icon="💳",
    layout="wide"
)


@st.cache_data
def get_data():

    df = load_customers()
    df = add_segments(df)
    df = add_recommendations(df)

    return df


df = get_data()


st.title("CardSense")
st.subheader(
    "Customer Intelligence & Next Best Action Platform"
)


st.markdown(
"""
CardSense helps product teams analyze customer behaviour,
identify segments, and generate explainable business actions.
"""
)


# KPI Section

col1, col2, col3, col4 = st.columns(4)


with col1:
    st.metric(
        "Total Customers",
        len(df)
    )


with col2:
    st.metric(
        "Average Spend",
        f"₹{int(df.monthly_spend.mean()):,}"
    )


with col3:
    st.metric(
        "Premium Customers",
        len(
            df[
                df.segment=="Premium Candidate"
            ]
        )
    )


with col4:
    st.metric(
        "Campaign Eligible",
        len(
            df[
                df.priority=="High"
            ]
        )
    )


st.divider()


# Charts

col1, col2 = st.columns(2)


with col1:

    segment_count = (
        df.segment
        .value_counts()
        .reset_index()
    )

    segment_count.columns=[
        "Segment",
        "Count"
    ]

    fig = px.pie(
        segment_count,
        names="Segment",
        values="Count",
        title="Customer Segments"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


with col2:

    fig = px.histogram(
        df,
        x="monthly_spend",
        title="Monthly Spending Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


st.divider()


st.subheader("Latest Recommendations")

st.dataframe(
    df[
        [
            "name",
            "segment",
            "recommendation",
            "priority",
            "reason"
        ]
    ].head(10),
    use_container_width=True
)