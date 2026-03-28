from dash import html, dash
import dash_bootstrap_components as dbc

from sidebar import sidebar


def get():
    return dbc.Container([
        html.Div([
            sidebar.get(),
            dash.page_container
        ], className="flex flex-col md:flex-row")
    ])