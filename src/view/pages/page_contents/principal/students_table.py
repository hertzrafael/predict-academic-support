from dash import html, dash_table
from global_df import df
from config import config


def get():
    df_filtered = df[config.table_columns]

    max_year = 2024
    max_period = df_filtered[df_filtered['ano'] == max_year]['periodo'].max()

    df_filtered = (
        df_filtered[(df_filtered['ano'] == max_year) & (df_filtered['periodo'] == max_period) & (df_filtered['situacao'] == "MATRICULADO")]
        [config.students_table_columns]
        .sort_values(by=['target_media_percentil', 'score_risco'], ascending=[False, False])
    )

    return html.Div(
        html.Div(
            [
                html.Div(
                    html.H1(f"Tabela de Alunos Matriculados ({max_year}.{max_period})", className="font-semibold text-lg")
                ),
                html.Div(
                    dash_table.DataTable(
                        id="table",
                        columns=[{"name": i, "id": i} for i in df_filtered.columns],
                        data=df_filtered.to_dict("records"),
                        page_current=0,
                        page_size=15,
                        page_action='native',
                        style_table={
                            "overflowX": "auto",
                            "maxWidth": "100%",
                            "width": "100%"
                        },
                        style_cell={
                            "maxWidth": "150px",
                            "overflow": "hidden",
                            "textOverflow": "ellipsis",
                            "whiteSpace": "nowrap",
                        }
                    ),
                    className="mt-3 w-full overflow-x-auto",
                ),
            ],
            className="bg-white rounded-lg border border-gray-200 p-3",
        ),
        className="p-3 w-full overflow-hidden"
    )
