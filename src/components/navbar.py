# notes
'''
This file is for creating a navigation bar that will sit at the top of your application.
Much of this page is pulled directly from the Dash Bootstrap Components documentation linked below:
https://dash-bootstrap-components.opensource.faculty.ai/docs/components/navbar/
'''

# package imports
from dash import html, clientside_callback, ClientsideFunction, Output, Input, State
import dash_bootstrap_components as dbc

import utils.constants as c
import utils.images

_PREFIX = 'navbar'
_TOGGLE = f'{_PREFIX}-navbar'
_COLLAPSE = f'{_PREFIX}-collapse'

# if your navbar contains any datetime components
# make sure to turn this into a function instead
navbar = dbc.Navbar(dbc.Container([
    dbc.NavbarBrand([
        html.Img(
            height='40px',
            src=utils.images.ENCODED_LOGO,
            className='d-none d-md-inline'
        ),
        html.Img(
            height='40px',
            src=utils.images.ENCODED_LOGO_SMALL,
            className='d-md-none'
        ),
        html.Span('My Application', className='ms-2')
    ], href='/'),
]), id=_PREFIX, color=c.BOOTSTRAP.COLOR.DARK, dark=True)

clientside_callback(
    ClientsideFunction(c.DASH.CLIENTSIDE, 'toggleWithButton'),
    Output(_COLLAPSE, c.DASH.IS_OPEN),
    Input(_TOGGLE, c.DASH.N_CLICKS),
    State(_COLLAPSE, c.DASH.IS_OPEN)
)
