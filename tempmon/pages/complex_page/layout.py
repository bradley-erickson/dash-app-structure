# notes
'''
This directory is meant to be for a specific page.
We will define the page and import any page specific components that we define in this directory.
This file should serve the layouts and callbacks.
The callbacks could be in their own file, but you'll need to make sure to import the file so they load.
'''

# package imports
import dash
from dash import html
import dash_bootstrap_components as dbc

# local imports
from .comp1 import random_component
from components import create_dog_image_card, NumberFactAIO

dash.register_page(
    __name__,
    path='/complex',
    title='Complex page'
)

layout = html.Div(
    [
        html.H3('Random component'),
        random_component,
        html.H3('Dog pics'),
        dbc.Row(
            [
                create_dog_image_card('labrador', 'n02099712_3503'),
                create_dog_image_card('labrador', 'n02099712_607')
            ]
        ),
        html.H3('Number Fact'),
        NumberFactAIO(number=1)
    ]
)
