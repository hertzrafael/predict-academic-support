class Config:

    def __init__(self):
        self.nav_icons = [
            {
                "name": "Estatísticas",
                "icon": "chart-column",
                "route": "/"
            },
            {
                "name": "Simulação",
                "icon": "flask-conical",
                "route": "/simulation"
            }
        ]

        self.filters = [
            {
                "id": "filter-course",
                "name": "Cursos",
                "column_name": "curso_nome"
            },
            {
                "id": "filter-year",
                "name": "Ano",
                "column_name": "ano"
            },
            {
                "id": "filter-period",
                "name": "Período",
                "column_name": "periodo"
            },
            {
                "id": "filter-campus",
                "name": "Campus",
                "column_name": "campus"
            }
        ]

        self.kpis = [
            {
                "type": "kpi-card",
                "index": "students",
                "name": "Total de Alunos",
                "icon": "users"
            },
            {
                "type": "kpi-card",
                "index": "courses",
                "name": "Total de Cursos",
                "icon": "book"
            },
            {
                "type": "kpi-card",
                "index": "campuses",
                "name": "Total de Campi",
                "icon": "building"
            },
            {
                "type": "kpi-card",
                "index": "periods",
                "name": "Total de Períodos",
                "icon": "calendar"
            }
        ]

        self.table_columns = [
            "id_discente",
            "target_media_percentil",
            "score_risco",
            "media_geral",
            "ano",
            "periodo",
            "situacao",
            "sexo",
            "estado_civil",
            "raca_declarada",
            "ano_ingresso",
            "periodo_ingresso",
            "status_discente",
            "ch_integralizada",
            "ch_pendente",
            "ano_nascimento",
            "faixa_renda_familiar",
            "uf_titulo_eleitor_pb",
            "uf_naturalidade_pb",
            "sigla_academica",
            "sigla_centro",
            "curso_nome",
            "campus",
            "turno_estrutura_curricular",
            "carga_horaria"
        ]

        self.students_table_columns = [
            "id_discente",
            "target_media_percentil",
            "score_risco",
            "media_geral",
            "sexo",
            "estado_civil",
            "raca_declarada",
            "ano_ingresso",
            "periodo_ingresso",
            "status_discente",
            "sigla_academica",
            "sigla_centro",
            "curso_nome",
            "turno_estrutura_curricular"
        ]

config = Config()