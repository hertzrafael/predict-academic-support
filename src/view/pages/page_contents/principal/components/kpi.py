from dash_iconify import DashIconify
from dash import html


def get(index, name, icon):
    return html.Div([
        html.Div([
            html.Span(name, className="text-gray-500 text-sm font-semibold uppercase"),
            html.H1(
                id={"type": "kpi-value", "index": index}, 
                children=0, 
                className="font-bold text-xl"
            )
        ]),
        html.Div(DashIconify(icon=f"lucide:{icon}", width=20, color="white"), className="bg-teal-400 p-2 rounded-lg self-start")
    ],
    className="bg-white rounded-lg border border-gray-200 p-2 flex flex-row justify-between hover:shadow-lg transition-shadow"
    )