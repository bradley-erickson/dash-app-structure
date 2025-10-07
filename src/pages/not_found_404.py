# pages/not_found_404.py
'''
This file creates the 404 not found page.
If this file is not included, Dash will the same layout shown below.
If you need a more customized 404 not found page, modify this file.
'''
import dash
from dash import html

dash.register_page(__name__, path='/404')

layout = html.Div(
    [
        html.H1('404 - Page not found'),
        html.Div(
            html.A('Return home', href='/')
        )
    ]
)
