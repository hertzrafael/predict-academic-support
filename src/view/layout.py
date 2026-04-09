from dash import html, dash, dcc, callback, Output, Input
from sidebar import sidebar
from config import config
from global_df import df


# IMPORTANDO CALLBACKS
from pages.page_contents.principal.callbacks import kpi_callback
from pages.page_contents.principal.callbacks import filter_callback
from pages.page_contents.principal.callbacks import pizza_target_callback
from pages.page_contents.principal.callbacks import target_by_course_and_year_callback
from pages.page_contents.principal.callbacks import race_target_callback

from pages.page_contents.simulation.callbacks import simulation_callback
from pages.page_contents.simulation.callbacks import selector_callback
from pages.page_contents.simulation.callbacks import insight_callback

import dash_bootstrap_components as dbc


def get():
    return dbc.Container([
        dcc.Store(id="df-store"),
        html.Div([
            sidebar.get(),
            html.Div(
                dash.page_container,
                className="w-full bg-gray-100 min-w-0"
            )
        ], className="flex flex-col md:flex-row")
    ])

@callback(
    Output("df-store", "data"),
    Input("df-store", "id"),  # 🔥 dispara ao iniciar
    [Input(f["id"], "value") for f in config.filters]
)
def load_data(_, *values):
    print("🔥 carregando dados")
    print(df.shape)
    
    df_filtered = df.copy()

    for i, value in enumerate(values):
        column = config.filters[i]["column_name"]

        if value != "None":
            df_filtered = df_filtered[df_filtered[column] == value]

    return df_filtered.to_dict("records")