from utils.data_loader import load_customers
from services.segmentation import add_segments
from services.recommendation_engine import add_recommendations


df = load_customers()

df = add_segments(df)

df = add_recommendations(df)


print(
    df[
        [
            "name",
            "segment",
            "recommendation",
            "priority"
        ]
    ].head()
)