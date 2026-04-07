from dash import html, dcc, Input, Output, callback

from sidebar.components import title
from sidebar.components import nav_icon
from config import config


def get():
    return html.Div(
        [
            dcc.Store(id="side-navigating", data={"isNavigating": False}),
            dcc.Location(id="url", refresh=False),
            title.get(),
            html.Div(
                [
                    html.Div(
                        html.P(
                            "Navegação",
                            className="text-gray-400 font-bold uppercase text-xs",
                        )
                    ),
                    html.Div(id="sidebar-nav-items", className="mt-3"),
                ],
                id="sidebar-nav-container",
            ),
        ],
        className="bg-[#151C28] w-screen p-3 md:min-h-screen md:max-w-2xs md:min-w-3xs",
    )


@callback(Output("sidebar-nav-items", "children"), Input("url", "pathname"))
def update_nav(pathname):
    pathname = pathname or "/"

    return [
        nav_icon.get(
            icon["name"],
            icon["icon"],
            icon["route"],
            active=(pathname == icon["route"]),
        )
        for icon in config.nav_icons
    ]

# FAZENDO RESPONSIVIDADE, QUANDO FOR NO CELULAR E isNavigating = False, NÃO APARECER O CONTAINER DE NAVEGAÇÃO.
@callback(
    Output("sidebar-nav-container", "className"),
    Input("side-navigating", "data"),
)
def toggle_sidebar(data):
    normal = "mt-10"
    if data["isNavigating"]:
        return normal

    return f"{normal} hidden md:block"