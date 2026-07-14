import streamlit as st
import plotly.express as px

from utils.data_loader import load_customers
from services.segmentation import add_segments
from services.recommendation_engine import add_recommendations



st.title("Portfolio Analytics")


df = load_customers()

df = add_segments(df)

df = add_recommendations(df)



# KPI


col1,col2,col3,col4 = st.columns(4)


with col1:
    st.metric(
        "Customers",
        len(df)
    )


with col2:
    st.metric(
        "Avg Income",
        f"₹{int(df.annual_income.mean()):,}"
    )


with col3:
    st.metric(
        "Avg Utilization",
        f"{round(df.credit_utilization.mean(),2)}%"
    )


with col4:
    st.metric(
        "High Priority Actions",
        len(df[df.priority=="High"])
    )



st.divider()



# Segment chart


segment = (
    df.segment
    .value_counts()
    .reset_index()
)


segment.columns=[
    "Segment",
    "Count"
]


fig = px.bar(
    segment,
    x="Segment",
    y="Count",
    title="Customer Segment Distribution"
)


st.plotly_chart(
    fig,
    use_container_width=True
)



# Recommendation chart


rec = (
    df.recommendation
    .value_counts()
    .reset_index()
)


rec.columns=[
    "Recommendation",
    "Customers"
]


fig2 = px.pie(
    rec,
    names="Recommendation",
    values="Customers",
    title="Recommendation Distribution"
)


st.plotly_chart(
    fig2,
    use_container_width=True
)



# Spending analysis


fig3 = px.scatter(
    df,
    x="monthly_spend",
    y="credit_utilization",
    color="segment",
    title="Spend vs Credit Utilization"
)


st.plotly_chart(
    fig3,
    use_container_width=True
)