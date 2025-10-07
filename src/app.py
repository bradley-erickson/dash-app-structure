# app.py
'''
This file is for housing the main dash application.
This is where we define the various css items to fetch as well as the layout of our application.
'''
import dash
from dash import html
import dash_bootstrap_components as dbc
from flask import Flask

import utils.constants as c
import utils.settings
utils.settings.load_settings()

if c.RUNTIME.DEPLOYMENT_TYPE == c.DEPLOYMENT.PRODUCTION:
    print('Monkey patching for Gevent')
    from gevent import monkey
    monkey.patch_all()

import components.navbar

server = Flask(__name__)
server.config.update(SECRET_KEY=c.RUNTIME.SECRET_KEY)
app = dash.Dash(
    __name__,
    server=server,
    use_pages=True,    # turn on Dash pages
    external_stylesheets=[
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
    title='Structuring a dash app'
)
server = app.server         # the server is needed to deploy the application


def serve_layout():
    '''Define the layout of the application'''
    return html.Div(
        [
            components.navbar.navbar,
            dbc.Container(
                dash.page_container,
                class_name='my-2'
            ),
        ]
    )


app.layout = serve_layout   # set the layout to the serve_layout function

if __name__ == "__main__":
    app.run(
        host=c.RUNTIME.HOST,
        port=c.RUNTIME.PORT,
        debug=c.RUNTIME.DEBUG,
    )
