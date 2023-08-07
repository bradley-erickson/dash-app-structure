# notes
'''
This file is a simple AIO component that contains an input and a div.
The input determines which number you want a fact of.
For more information about AIO components, check out the official documentation:
https://dash.plotly.com/all-in-one-components
'''

# package imports
from dash import html, dcc, callback, Output, Input, MATCH
import dash_bootstrap_components as dbc
import uuid

# local imports
from utils.api import get_number_fact


class NumberFactAIO(html.Div):

    class ids:
        text = lambda aio_id: {
            'component': 'NumberFactAIO',
            'subcomponent': 'div',
            'aio_id': aio_id
        }
        input = lambda aio_id: {
            'component': 'NumberFactAIO',
            'subcomponent': 'input',
            'aio_id': aio_id
        }

    ids = ids

    def __init__(
        self,
        number=0,
        aio_id=None
    ):
        if aio_id is None:
            aio_id = str(uuid.uuid4())

        fact = get_number_fact(number)

        super().__init__([
            dcc.Input(
                id=self.ids.input(aio_id),
                value=number,
                type='number',
                min=0
            ),
            html.Div(
                children=fact,
                id=self.ids.text(aio_id)
            )
        ])

    @callback(
        Output(ids.text(MATCH), 'children'),
        Input(ids.input(MATCH), 'value')
    )
    def update_number_fact(value):
        fact = get_number_fact(value)
        return fact
