# package imports
import dash
import dash_bootstrap_components as dbc

# local imports
from components.login import login_card

dash.register_page(__name__)

# login screen
layout = dbc.Row(
    dbc.Col(
        login_card,
        md=6,
        lg=4,
        xxl=3,
    ),
    justify='center'
)
