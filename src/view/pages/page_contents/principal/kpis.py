from dash import html
from pages.page_contents.principal.components import kpi as kpi_component
from config import config


def get():
    return html.Div(
        html.Div(
            [
                kpi_component.get(kpi["index"], kpi["name"], kpi["icon"]) for kpi in config.kpis
            ],
            className="grid grid-cols-2 gap-3 md:grid-cols-4"
        ),
        className="mt-3 p-3 w-full"
    )