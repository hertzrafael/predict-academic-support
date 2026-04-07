from dash import html, dcc


def get(id, name, options):
    return html.Div([
        dcc.Dropdown(
            id=id,
            options=[
                {"label": name, "value": "None"},
                *[{"label": opt, "value": opt} for opt in options]
            ],
            value="None",
            clearable=False
        )
    ])