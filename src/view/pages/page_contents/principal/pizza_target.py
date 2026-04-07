from dash import html, dcc


def get():
    return html.Div(
        [
            html.H1(
                "Distribuição do Apoio Acadêmico", className="font-semibold text-lg"
            ),
            dcc.Graph(id="distribution-academic-support"),
        ],
        className="bg-white rounded-lg border border-gray-200 p-3 col-span-6 md:col-span-3",
    )
