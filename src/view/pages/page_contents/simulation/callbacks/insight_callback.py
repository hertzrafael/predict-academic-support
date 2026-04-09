from dash import Input, Output, callback
from global_df import df
from ai.agent import agent


@callback(
    Output("sim-ia-insight", "children"),
    Input("sim-student-dropdown", "value")
)
def update_options(student_id):
    if not student_id:
        return "Selecione um estudante"
    
    print("Iniciando geração de insight...")
    df_student = df[df["id_discente"] == student_id].sort_values(by=["ano", "periodo"], ascending=[False, False])
    student_json = df_student.to_json(orient="records", force_ascii=False)
    
    insight = agent.run_prompt(student_json)
    
    return insight