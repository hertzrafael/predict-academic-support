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

config = Config()