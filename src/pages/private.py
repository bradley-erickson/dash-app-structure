# package imports
import dash
from dash import html, dcc, Output, Input, clientside_callback, ClientsideFunction

import utils.constants as c

dash.register_page(__name__)

_PREFIX = '_pages-private'
_RADIO = f'{_PREFIX}-radio'
_SELECTED = f'{_PREFIX}-selected-radio'


def layout():
    cont = html.Div([
        html.H1('Private page'),
        dcc.RadioItems(
            id=_RADIO,
            options=[{c.DASH.LABEL: i, c.DASH.VALUE: i} for i in ['Orange', 'Blue', 'Red']],
            value='Orange',
        ),
        html.Div('You have selected:'),
        html.Div(id=_SELECTED),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
    ])
    return cont


clientside_callback(
    ClientsideFunction(c.DASH.CLIENTSIDE, 'returnValue'),
    Output(_SELECTED, c.DASH.CHILDREN),
    Input(_RADIO, c.DASH.VALUE),
)
