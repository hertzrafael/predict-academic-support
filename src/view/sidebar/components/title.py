from dash_iconify import DashIconify
from dash import html


def get():
    return html.Div([
        html.Div(
            DashIconify(icon="lucide:graduation-cap", width=20, color="white"),
            className="bg-teal-500 p-2 rounded-lg flex items-center justify-center"
        ),
        html.Div([
            html.P('Apoio Acadêmico', className="font-bold text-white"),
            html.P('Previsão e Análise', className="text-sm text-gray-300")
        ], className="flex flex-col")
    ], className="flex flex-row items-center gap-2 mt-10")