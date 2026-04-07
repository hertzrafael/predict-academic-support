from dash import Input, Output, callback
import pandas as pd
import plotly.express as px


@callback(
    Output("distribution-academic-support-race", "figure"), Input("df-store", "data")
)
def update_distribution_academic_support_race(data):
    if not data:
        return px.bar(title="Sem dados")

    df = pd.DataFrame(data)
    df_grouped = (
        df[df["target_media_percentil"] == 1]
        .groupby("raca_declarada")["id_discente"]
        .nunique()
        .reset_index(name="count")
    )

    fig = px.bar(
        df_grouped, x="raca_declarada", y="count", color_discrete_sequence=["#2563eb"]
    )

    fig.update_layout(
        legend_title="Raça",
        font=dict(family="Arial, sans-serif", size=12, color="#7f7f7f"),
    )

    return fig
