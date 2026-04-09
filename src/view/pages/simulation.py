from dash import html, register_page
from pages.page_contents.simulation import student_selector, student_stats, student_temporal_chart, student_active_enrollments

register_page(__name__, path="/simulation")

layout = html.Div([
    html.Div([
        student_selector.get(),
        html.Div([
            html.H1("Insight IA", className="text-xl font-semibold text-gray-800"),
            html.P(id="sim-ia-insight", className="mt-2 text-gray-600")
        ], className="md:col-span-3 p-3 bg-white rounded-lg border border-gray-200")
    ], className="p-3 mt-8 grid md:grid-cols-5 gap-3"),
    student_stats.get(),
    html.Div([
        student_active_enrollments.get(),
        student_temporal_chart.get()
    ], className="grid grid-cols-6 p-3 gap-3 md:grid-cols-12")
])
