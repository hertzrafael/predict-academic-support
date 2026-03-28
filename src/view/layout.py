from dash import html
import dash_bootstrap_components as dbc

from view.sidebar import sidebar
from view.principal import principal


def get():
    return dbc.Container([
        html.Div([
            sidebar.get(),
            principal.get()
        ], className="flex flex-col md:flex-row")
    ])