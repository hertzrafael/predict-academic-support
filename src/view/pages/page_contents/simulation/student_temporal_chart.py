from dash import html, dcc

def get():
    return html.Div(
        html.Div(
            [
                html.Div(
                    [
                        html.H3("Evolução da Média Geral", className="font-semibold text-lg"),
                        html.P("Média por ano e período", className="text-sm text-gray-500 mb-2"),
                    ],
                    className="mb-2"
                ),
                dcc.Graph(id="sim-temporal-chart")
            ],
            className="bg-white rounded-lg border border-gray-200 p-4 h-full"
        ),
        className="col-span-12 md:col-span-8 h-full"
    )
