from dash_iconify import DashIconify
from dash import html, callback, Output, Input, State


def get():
    return html.Div(
        [
            html.Div(
                [
                    html.Div(
                        DashIconify(
                            icon="lucide:graduation-cap", width=20, color="white"
                        ),
                        className="bg-teal-500 p-2 rounded-lg flex items-center justify-center",
                    ),
                    html.Div(
                        [
                            html.P("Apoio Acadêmico", className="font-bold text-white"),
                            html.P(
                                "Previsão e Análise", className="text-sm text-gray-300"
                            ),
                        ],
                        className="flex flex-col",
                    ),
                ],
                className="flex flex-row items-center gap-2",
            ),
            html.Div(
                DashIconify(icon="lucide:menu", width=20, color="white"),
                className="bg-teal-500 p-2 rounded-lg flex items-center justify-center cursor-pointer md:hidden",
                id="side-nav-button",
                n_clicks=0
            ),
        ],
        className="w-full md:mt-10 flex flex-row justify-between items-center",
    )


@callback(
    Output("side-navigating", "data"),
    Input("side-nav-button", "n_clicks"),
    State("side-navigating", "data"),
    prevent_initial_call=True
)
def toggle_navigation(n, data):
    data["isNavigating"] = not data["isNavigating"]
    return data

