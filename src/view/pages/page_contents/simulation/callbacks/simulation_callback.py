from dash import Input, Output, callback
import plotly.express as px
from global_df import df


@callback(
    Output("sim-stat-target_media_percentil", "children"),
    Output("sim-stat-curso", "children"),
    Output("sim-stat-ano-periodo", "children"),
    Output("sim-stat-renda", "children"),
    Output("sim-stat-media", "children"),
    Output("sim-stat-ch-integralizada", "children"),
    Output("sim-stat-situacao", "children"),
    Output("sim-temporal-chart", "figure"),
    Output("sim-active-enrollments", "children"),
    Input("sim-student-dropdown", "value")
)
def update_simulation_page(student_id):
    if not student_id:
        empty_fig = px.bar()
        empty_fig.update_layout(template="plotly_white")
        return "-", "-", "-", "-", "-", "-", empty_fig, "0"

    # Filter for the selected student
    student_data = df[df["id_discente"] == student_id]
    
    if student_data.empty:
        empty_fig = px.bar()
        empty_fig.update_layout(template="plotly_white")
        return "-", "-", "-", "-", "-", "-", empty_fig, "0"

    # Sorting to get chronological data and identifying latest record
    student_data = student_data.sort_values(by=["ano", "periodo"])
    latest_record = student_data.iloc[-1]

    # Descriptive Stats
    target_media_percentil = "Sim" if latest_record.get("target_media_percentil", 0) == 1 else "Não"
    curso = str(latest_record.get("curso_nome", "N/A"))
    ano_periodo = f"{latest_record.get('ano', '')}.{latest_record.get('periodo', '')}"
    renda = str(latest_record.get("faixa_renda_familiar", "N/A"))
    media = f"{latest_record.get('media_geral', 0):.2f}" if "media_geral" in latest_record else "N/A"
    ch_int = str(latest_record.get("ch_integralizada", "N/A"))
    situacao = str(latest_record.get("situacao", "N/A"))

    # Temporal chart for general average
    # Creating a combined X axis label for year and period
    student_data["ano_periodo"] = student_data["ano"].astype(str) + "." + student_data["periodo"].astype(str)
    
    fig = px.bar(
        student_data, 
        x="ano_periodo", 
        y="media_geral",
        labels={"ano_periodo": "Ano.Período", "media_geral": "Média Geral"},
        text="media_geral",
        color_discrete_sequence=["#2563eb"]
    )
    fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    fig.update_layout(
        template="plotly_white", 
        margin=dict(l=20, r=20, t=20, b=20),
        xaxis_title=None,
        yaxis_title=None,
    )

    # Active enrollments in the highest year and period
    max_ano = student_data["ano"].max()
    max_periodo = student_data[student_data["ano"] == max_ano]["periodo"].max()
    
    # Check how many are "MATRICULADO" or just calculate rows for max term
    # If the df is at the student-semester level, it will just be 1. 
    # But as the user implicitly expects "disciplinas", maybe there are multiple discipline rows per student in `df`.
    # Let's count records for the max_ano just in case they are class enrollments:
    active_rows = student_data[(student_data["ano"] == max_ano)]
    
    # We will just show the number of rows as active enrollments since user said "pega o maior ano no registro daquele aluno para calcular isso - quantidade de matriculas"
    active_enrollments_count = len(active_rows)

    return target_media_percentil, \
           curso, \
           ano_periodo, \
           renda, \
           media, \
           ch_int, \
           situacao, \
           fig, \
           str(active_enrollments_count)
