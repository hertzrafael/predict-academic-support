from dash import html, dcc
from global_df import df


def get():
    students = df.sort_values(by=["ano", "periodo"], ascending=[False, False])["id_discente"].dropna().unique()
    
    initial_options = [{"label": f"Aluno {student}", "value": student} for student in students[:50]]
    initial_value = students[0] if len(students) > 0 else None
    
    return html.Div(
        html.Div(
            [
                html.Label("Selecione um Estudante (ID)", className="font-semibold text-sm mb-1 block text-gray-700"),
                dcc.Dropdown(
                    id="sim-student-dropdown",
                    options=initial_options,
                    value=initial_value,
                    clearable=False,
                    className="w-full text-sm",
                    placeholder="Selecione..."
                )
            ],
            className="bg-white rounded-lg border border-gray-200 p-4 w-full md:w-1/3"
        ), 
        className="mt-8 p-3 w-full"
    )
