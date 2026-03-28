from dash import Dash
from view import layout

import os


app = Dash(
    __name__, 
    assets_folder=os.path.join(os.path.dirname(os.path.dirname(__file__)), 'assets')
)
app.layout = layout.get()


if __name__ == '__main__':
    app.run(debug=True)