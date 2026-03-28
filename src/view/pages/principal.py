from dash import html, register_page


register_page(__name__, path="/")

layout = html.Div([
    html.Div(html.P("Principal")),
    html.Div(html.P("Principal 2"))
], className="flex flex-row justify-between")
