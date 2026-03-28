from dash import html, dcc
from dash_iconify import DashIconify


def get(name, icon_name, route, active=False):
    return dcc.Link([
        html.Div(
            DashIconify(icon=f"lucide:{icon_name}", width=20)
        ),
        html.Div([
            html.P(name, className="text-sm font-semibold"),
        ])
    ], 
    className=f"""
        flex flex-row items-center text-white gap-2 p-2 mt-2 cursor-pointer 
        {'bg-teal-500 rounded-lg' if active else ''}
    """,
    id=f"nav-{route}", 
    href=route)
