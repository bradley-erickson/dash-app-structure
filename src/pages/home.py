# package imports
import dash
from dash import html, dcc, clientside_callback, ClientsideFunction, Input, Output

import utils.constants as c

dash.register_page(
    __name__,
    path='/',
    redirect_from=['/home'],
    title='Home'
)

_PREFIX = '_pages-home'
_RADIO = f'{_PREFIX}-radio'
_SELECTED = f'{_PREFIX}-selected-radio'

layout = html.Div(
    [
        html.H1('Home page!'),
        html.A('Private page', href='/private'),
        dcc.RadioItems(
            id=_RADIO,
            options=[{c.DASH.LABEL: i, c.DASH.VALUE: i} for i in ['Orange', 'Blue', 'Red']],
            value='Orange',
        ),
        html.Div('You have selected:'),
        html.Div(id=_SELECTED)
    ]
)

clientside_callback(
    ClientsideFunction(c.DASH.CLIENTSIDE, 'returnValue'),
    Output(_SELECTED, c.DASH.CHILDREN),
    Input(_RADIO, c.DASH.VALUE),
)
