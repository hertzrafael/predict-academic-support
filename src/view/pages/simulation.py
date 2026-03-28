from dash import html, register_page

register_page(__name__, path="/simulation")

layout = html.Div([
    html.H1("Simulação")
])
