from dash import Input, Output, callback
import pandas as pd
import plotly.express as px


@callback(
    Output("distribution-academic-support", "figure"),
    Input("df-store", "data")
)
def update_distribution_academic_support(data):
    if not data:
        return px.pie(title="Sem dados")

    df = pd.DataFrame(data)

    df_grouped = df["target_media_percentil"].value_counts().reset_index()
    df_grouped.columns = ["target_media_percentil", "count"]

    fig = px.pie(
        df_grouped,
        names="target_media_percentil",
        values="count"
    )

    fig.update_layout(
        legend_title="Apoio Acadêmico",
        font=dict(
            family="Arial, sans-serif",
            size=12,
            color="#7f7f7f"
        )
    )

    return fig