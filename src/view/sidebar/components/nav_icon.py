from dash import html
from dash_iconify import DashIconify


def get(name, icon_name, active=False):
    return html.Div([
        html.Div(
            DashIconify(icon=f"lucide:{icon_name}", width=20)
        ),
        html.Div([
            html.P(name, className="text-sm font-semibold"),
        ])
    ], className="flex flex-row items-center text-white gap-2 p-2 mt-2 cursor-pointer")