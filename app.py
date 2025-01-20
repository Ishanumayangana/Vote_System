from dash import Dash
import dash
from dash import dcc, html
from layout import layout
from callback import register_callbacks
import db_handler

# Initialize the Dash app
app = dash.Dash(__name__)

# Initialize the database (this creates the table if not exists)
db_handler.init_db()

# Setup layout for the Dash app
app.layout = layout

# Register callbacks for Dash interactivity
register_callbacks(app)

# Run the Dash app using the built-in server (no Uvicorn needed)
if __name__ == '__main__':
    app.run_server(debug=True)
