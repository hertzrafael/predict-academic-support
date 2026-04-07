from dash import html
import dash_bootstrap_components as dbc
from dash_iconify import DashIconify


def stat_card(id_suffix, title, icon_name="info"):
    return html.Div(
        [
            html.Div(
                [
                    DashIconify(icon=f"lucide:{icon_name}", width=24, className="text-blue-600"),
                ],
                className="bg-blue-100 p-3 rounded-full mr-4 flex-shrink-0"
            ),
            html.Div(
                [
                    html.P(title, className="text-sm font-semibold text-gray-500 mb-1"),
                    html.P("...", id=f"sim-stat-{id_suffix}", className="text-xl font-bold text-gray-800 break-words")
                ],
                className="flex-1 min-w-0"
            )
        ],
        className="bg-white rounded-lg border border-gray-200 p-4 flex items-center shadow-sm min-w-0 w-full"
    )

def get():
    return html.Div(
        [
            html.H3("Perfil do Estudante", className="font-semibold text-lg mb-3 ml-1"),
            html.Div(
                [
                    stat_card("target_media_percentil", "Necessitando Apoio Acadêmico", "target"),
                    stat_card("curso", "Curso", "graduation-cap"),
                    stat_card("ano-periodo", "Último Ano/Período", "calendar"),
                    stat_card("renda", "Faixa de Renda Familiar", "wallet"),
                    stat_card("media", "Média Geral Atual", "bar-chart"),
                    stat_card("ch-integralizada", "CH Integralizada", "check-circle"),
                    stat_card("situacao", "Situação Atual", "activity")
                ],
                className="grid grid-cols-1 md:grid-cols-3 gap-4"
            )
        ],
        className="px-3 w-full"
    )
