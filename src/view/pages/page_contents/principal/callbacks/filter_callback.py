from dash import Input, Output, callback
from config import config
from global_df import df


@callback(
    [Output(f["id"], "options") for f in config.filters],
    [Input(f["id"], "value") for f in config.filters]
)
def update_filter_options(*values):
    outputs = []

    for i, f in enumerate(config.filters):
        df_filtered = df.copy()

        for j, value in enumerate(values):
            if i == j:
                continue  # 🔥 ignora o próprio filtro

            column = config.filters[j]["column_name"]

            if value != "None":
                df_filtered = df_filtered[df_filtered[column] == value]

        column = f["column_name"]

        options = sorted(df_filtered[column].dropna().unique())

        formatted = [
            {"label": f"Todos os {f['name']}", "value": "None"},
            *[{"label": opt, "value": opt} for opt in options]
        ]

        outputs.append(formatted)

    return outputs