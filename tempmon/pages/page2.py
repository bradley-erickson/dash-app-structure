# package imports
import dash
from dash import html, dcc, Output, Input, callback
import dash_bootstrap_components as dbc
from flask_login import current_user

dash.register_page(__name__)

logged_out_layout = html.Div(
    [
        'Please login before viewing this page.',
        html.Br(),
        dbc.Button(
            'Login',
            href='/login'
        )
    ],
    className='text-center'
)

logged_in_layout = html.Div(
    [
        html.H1('Page 2'),
        dcc.RadioItems(
            id='page-2-radios',
            options=[{'label': i, 'value': i} for i in ['Orange', 'Blue', 'Red']],
            value='Orange',
        ),
        html.Div(id='page-2-content'),
        html.Br(),
        dcc.Link('Go to Page 1', href='/page-1'),
        html.Br(),
        dcc.Link('Go back to home', href='/'),
    ]
)

def layout():
    if not current_user.is_authenticated:
        return logged_out_layout
    return logged_in_layout


@callback(Output('page-2-content', 'children'), Input('page-2-radios', 'value'))
def page_2_radios(value):
    return f'You have selected {value}'
