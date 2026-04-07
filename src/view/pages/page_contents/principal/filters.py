from dash import html
from config import config
from pages.page_contents.principal.components import filter as filter_component

from global_df import df


def get():
    return html.Div(
        html.Div(
            [filter_component.get(
                filter["id"], 
                filter["name"],
                sorted(df[filter["column_name"]].dropna().unique())
            ) for filter in config.filters],
            className="bg-white rounded-lg border border-gray-200 p-2 grid grid-cols-3 gap-2 md:grid-cols-4 md:p-4"
        ), 
        className="mt-8 p-3 w-full"
    )