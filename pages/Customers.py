import streamlit as st

from utils.data_loader import load_customers
from services.segmentation import add_segments
from services.recommendation_engine import add_recommendations


st.title("Customer Database")


df = load_customers()

df = add_segments(df)

df = add_recommendations(df)



search = st.text_input(
    "Search Customer"
)


if search:

    df = df[
        df.name
        .str.contains(
            search,
            case=False
        )
    ]



segment = st.selectbox(
    "Filter Segment",
    ["All"] + list(df.segment.unique())
)



if segment!="All":

    df=df[
        df.segment==segment
    ]



st.dataframe(
    df,
    use_container_width=True
)