from dash import Dash

import layout
import os


app = Dash(
    __name__, 
    use_pages=True,
    assets_folder=os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'assets')
)
app.layout = layout.get()


if __name__ == '__main__':
    app.run(debug=True)