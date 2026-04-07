from dash import html
from dash_iconify import DashIconify

def get():
    return html.Div(
        html.Div(
            [
                html.Div(
                    [
                        html.H3("Matrículas Ativas", className="font-semibold text-lg"),
                        html.P("No último semestre registrado", className="text-sm text-gray-500"),
                    ],
                    className="mb-4"
                ),
                html.Div(
                    [
                        html.Div(
                            [
                                DashIconify(icon="lucide:book-open", width=48, className="text-green-600"),
                            ],
                            className="bg-green-100 p-4 rounded-full mr-4 flex-shrink-0"
                        ),
                        html.Div(
                            [
                                html.P("Disciplinas", className="text-sm font-semibold text-gray-500 mb-1"),
                                html.P("...", id="sim-active-enrollments", className="text-4xl font-bold text-gray-800")
                            ],
                            className="flex-1"
                        )
                    ],
                    className="flex justify-center items-center h-full"
                )
            ],
            className="bg-white rounded-lg border border-gray-200 p-4 h-full flex flex-col"
        ),
        className="col-span-12 md:col-span-4 h-full"
    )
