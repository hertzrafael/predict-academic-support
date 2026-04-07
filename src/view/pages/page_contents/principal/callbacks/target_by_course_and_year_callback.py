from dash import Input, Output, callback
import pandas as pd
import plotly.express as px

@callback(
    Output("target-by-course-and-year-graph", "figure"),
    Input("df-store", "data"),
    Input("filter-course", "value")
)
def update_target_by_course_and_year(data, selected_course):
    if not data:
        return px.bar(title="Sem dados")

    df = pd.DataFrame(data)

    # 🔥 garante coluna binária (ajuste se necessário)
    target = "target_media_percentil"

    # ======================================================
    # 🎯 CASO 1 — SEM CURSO → TOP 10 CURSOS
    # ======================================================
    if selected_course in (None, "None"):

        df_grouped = (
            df.groupby("curso_nome")[target]
            .mean()
            .reset_index()
            .sort_values(by=target, ascending=False)
            .head(10)
        )

        df_grouped["curso_nome_curto"] = df_grouped["curso_nome"].apply(
            lambda x: x[:40] + "..." if len(x) > 40 else x
        )

        fig = px.bar(
            df_grouped,
            x=target,
            y="curso_nome_curto",
            orientation="h",
            hover_data={"curso_nome": True}
        )

        fig.update_layout(
            yaxis=dict(autorange="reversed")
        )

        return fig

    # ======================================================
    # 🎯 CASO 2 — COM CURSO → EVOLUÇÃO NO TEMPO
    # ======================================================
    else:
        df_course = df[df["curso_nome"] == selected_course]

        # cria eixo temporal combinado
        df_grouped = (
            df_course.groupby("ano")[target]
            .mean()
            .reset_index()
            .sort_values("ano")
        )

        fig = px.bar(
            df_grouped,
            x="ano",
            y=target
        )

        return fig