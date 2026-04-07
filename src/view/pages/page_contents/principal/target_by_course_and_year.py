from dash import html, dcc


def get():
    return html.Div([
        html.H1("Apoio Acadêmico por Curso e Ano", className="font-semibold text-lg"),
        dcc.Graph(id="target-by-course-and-year-graph")
    ],
        className="bg-white rounded-lg border border-gray-200 p-3 col-span-6 md:col-span-3"
    )