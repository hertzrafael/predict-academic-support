from dash import html, register_page
from pages.page_contents.simulation import student_selector, student_stats, student_temporal_chart, student_active_enrollments

register_page(__name__, path="/simulation")

layout = html.Div([
    student_selector.get(),
    student_stats.get(),
    html.Div([
        student_active_enrollments.get(),
        student_temporal_chart.get()
    ], className="grid grid-cols-6 p-3 gap-3 md:grid-cols-12")
])
