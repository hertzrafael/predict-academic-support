from dash import Input, Output, callback, State
from global_df import df


@callback(
    Output("sim-student-dropdown", "options"),
    Input("sim-student-dropdown", "search_value"),
    State("sim-student-dropdown", "value")
)
def update_options(search_value, current_value):
    # Obtém os mais recentes para o default
    students = df.sort_values(by=["ano", "periodo"], ascending=[False, False])["id_discente"].dropna().unique()

    
    if not search_value:
        filtered_list = students[:50].tolist()
    else:
        # Quando há busca
        filtered = df[
            df["id_discente"].astype(str).str.contains(str(search_value), case=False, na=False)
        ]["id_discente"].unique()
        filtered_list = filtered[:50].tolist()

    # Garante que o valor atual selecionado permaneça nas opções, senão ele some da tela
    if current_value is not None and current_value not in filtered_list:
        filtered_list.insert(0, current_value)

    return [
        {"label": f"Aluno {student}", "value": student}
        for student in filtered_list
    ]