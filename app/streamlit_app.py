import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Tokenomics Health Engine", layout="centered")

from pathlib import Path

@st.cache_data
def load_data():
    # Resolve project root (one level above /app)
    root = Path(__file__).resolve().parents[1]
    csv_path = root / "data" / "processed" / "tokenomics_health_engine_output.csv"
    return pd.read_csv(csv_path)

df = load_data()

st.title("Tokenomics Health Scoring Engine")
st.caption("Multi-pillar evaluation of crypto token sustainability")

token = st.selectbox(
    "Select a token",
    sorted(df["coingecko_id"].unique())
)

row = df[df["coingecko_id"] == token].iloc[0]

st.subheader(f"{token.upper()} — Health Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Final Score", round(row["tokenomics_health_score"], 1))
col2.metric("Grade", row["health_grade"])
col3.metric("Market Health", round(row["market_health_score"], 1))

st.markdown("### Pillar Breakdown")

fig = go.Figure(
    data=[
        go.Bar(
            x=["Market", "Distribution", "Supply"],
            y=[
                row["market_health_score"],
                row["distribution_health_score"],
                row["supply_sustainability_score"]
            ]
        )
    ]
)

fig.update_layout(
    yaxis_title="Score",
    yaxis_range=[0, 100]
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("### Interpretation")
st.write(
    "This score reflects structural tokenomics health based on liquidity, "
    "on-chain participation, and supply sustainability. "
    "It is not a price prediction."
)
