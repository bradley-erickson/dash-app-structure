# notes
'''
This file is for housing the main dash application.
This is where we define the various css items to fetch as well as the layout of our application.
'''

# package imports
import dash
from dash import html
import dash_bootstrap_components as dbc

# local imports
from utils.settings import APP_HOST, APP_PORT, APP_DEBUG, DEV_TOOLS_PROPS_CHECK
from components import navbar, footer

# This provides dbc styling for non-dbc components.
# For instance, this will style dcc.Dropdown components like dbc.Select components.
# All we need to do is set a single class name at the root of the app, see below.
dbc_css = 'https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.css'

app = dash.Dash(
    __name__,
    use_pages=True,    # turn on Dash pages
    external_stylesheets=[
        dbc_css,
        dbc.themes.BOOTSTRAP,
        dbc.icons.FONT_AWESOME
    ],  # fetch the proper css items we want
    meta_tags=[
        {   # check if device is a mobile device. This is a must if you do any mobile styling
            'name': 'viewport',
            'content': 'width=device-width, initial-scale=1'
        }
    ],
    suppress_callback_exceptions=True,
    title='Dash app structure'
)


def serve_layout():
    '''Define the layout of the application'''
    return html.Div(
        [
            navbar,
            dbc.Container(
                dash.page_container
            ),
            footer
        ],
        className='dbc' # style things like dbc
    )


app.layout = serve_layout   # set the layout to the serve_layout function
server = app.server         # the server is needed to deploy the application

if __name__ == "__main__":
    app.run_server(
        host=APP_HOST,
        port=APP_PORT,
        debug=APP_DEBUG,
        dev_tools_props_check=DEV_TOOLS_PROPS_CHECK
    )

