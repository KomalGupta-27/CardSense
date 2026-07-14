import streamlit as st

from utils.data_loader import load_customers
from services.segmentation import add_segments
from services.recommendation_engine import add_recommendations



st.title("Customer Profile")


df=load_customers()

df=add_segments(df)

df=add_recommendations(df)



customer = st.selectbox(
    "Select Customer",
    df.name
)



row=df[
    df.name==customer
].iloc[0]



st.subheader(row["name"])


col1,col2,col3=st.columns(3)


with col1:
    st.metric(
        "Income",
        f"₹{row.annual_income:,}"
    )

with col2:
    st.metric(
        "Credit Limit",
        f"₹{row.credit_limit:,}"
    )


with col3:
    st.metric(
        "Monthly Spend",
        f"₹{row.monthly_spend:,}"
    )


st.divider()


st.write(
    "### Customer Segment"
)

st.info(row.segment)



st.write(
    "### Next Best Action"
)


st.success(
    row.recommendation
)


st.write(
    "Reason:"
)

st.write(
    row.reason
)