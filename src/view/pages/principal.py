from dash import html, register_page
from pages.page_contents.principal import filters, kpis, target_by_course_and_year, pizza_target, students_table, race_target


register_page(__name__, path="/")

layout = html.Div([
    filters.get(),
    kpis.get(),
    html.Div([
        target_by_course_and_year.get(),
        pizza_target.get()
    ], className="grid grid-cols-6 p-3 gap-3"),
    race_target.get(),
    students_table.get()
])
