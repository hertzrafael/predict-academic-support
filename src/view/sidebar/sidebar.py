from dash import html, dcc

from view.sidebar.components import title
from view.sidebar.components import nav_icon
from view.config import config


def get():
    return html.Div([
        title.get(),
        html.Div([
            html.Div(html.P("Navegação", className="text-gray-400 font-bold uppercase text-sm")),
            html.Div([nav_icon.get(icon["name"], icon["icon"]) for icon in config.nav_icons], className="mt-3")
        ], className="mt-10")
    ], className="bg-[#151C28] w-screen p-3 md:h-screen md:max-w-2xs md:min-w-3xs")
