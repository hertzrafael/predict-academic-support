from dash import Input, Output, ALL, callback
from config import config

import pandas as pd


def get_kpi_value(df, index):
    return {
        "students": df["id_discente"].nunique(),
        "courses": df["curso_nome"].nunique(),
        "campuses": df["campus"].nunique(),
        "periods": df["periodo"].nunique()
    }[index]


@callback(
    Output({"type": "kpi-value", "index": ALL}, "children"),
    Input("df-store", "data")
)
def update_kpis(data):
    df = pd.DataFrame(data)

    return [ get_kpi_value(df, kpi["index"]) for kpi in config.kpis ]