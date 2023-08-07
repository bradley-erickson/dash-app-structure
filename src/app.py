# notes
'''
This file is for housing the main dash application.
This is where we define the various css items to fetch as well as the layout of our application.
'''

# package imports
#from flask import Flask
#from flask_login import LoginManager
import datetime
import os

import dash

#import dash_bootstrap_components as dbc
# local imports
#from utils.settings import APP_HOST, APP_PORT, APP_DEBUG, DEV_TOOLS_PROPS_CHECK
#from components.login import User, login_location
from components import simple_plot  #footer, navbar,
from dash import Input, Output, dcc, html

#server = Flask(__name__)
app = dash.Dash(
    __name__,
    # server=server,
    # use_pages=True,    # turn on Dash pages
    # external_stylesheets=[
    #     dbc.themes.BOOTSTRAP,
    #     dbc.icons.FONT_AWESOME
    # ],  # fetch the proper css items we want
    # meta_tags=[
    #     {   # check if device is a mobile device. This is a must if you do any mobile styling
    #         'name': 'viewport',
    #         'content': 'width=device-width, initial-scale=1'
    #     }
    # ],
    # suppress_callback_exceptions=True,
    title='Dash app structure'
)

#server.config.update(SECRET_KEY=os.getenv('SECRET_KEY'))

# Login manager object will be used to login / logout users
#login_manager = LoginManager()
#login_manager.init_app(server)
#login_manager.login_view = '/login'

# @login_manager.user_loader
# def load_user(username):
#     """This function loads the user by user id. Typically this looks up the user from a user database.
#     We won't be registering or looking up users in this example, since we'll just login using LDAP server.
#     So we'll simply return a User object with the passed in username.
#     """
#     return User(username)

import plotly.express as px
import plotly.graph_objs as go
from utils.preprocess_data import generate_dfs, get_test_data

data = get_test_data()
rs02, rs10 = generate_dfs()

@app.callback(
    Output(component_id="simple_plot", component_property="figure"),
    #Input("line-selector", "value"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
)
def update_charts(start_date, end_date):
    filtered_data = rs02.query(
        "date >= @start_date and date <= @end_date"
    )
    # trace1 = go.Scatter(x=filtered_data["date"], y=filtered_data["server room temp"], mode='lines', name='server room temp')
    # trace2 = go.Scatter(x=filtered_data["date"], y=filtered_data["outdoor temp"], mode='lines', name='outdoor temp')
    # selected_traces = [trace for trace in [trace1, trace2] if trace['name'] in selected_lines]
    # fig = go.Figure()
    # for trace in selected_traces:
    #     fig.add_trace(trace)
    #return {'data': selected_traces}
    simple_figure = px.line(x=filtered_data["date"], y=filtered_data["server room temp"], labels={"server room temp": "server room"}, title="rs02")
    simple_figure.add_scatter(x=filtered_data["date"], y=filtered_data["outdoor temp"], mode='lines', name='outdoor temp', yaxis="y1")
    simple_figure.add_scatter(x=filtered_data["date"], y=filtered_data["total jobs"], mode='lines', name='total jobs', yaxis="y2")
    simple_figure.update_layout(xaxis_title="Date", yaxis=dict(title='Temperature °C'), yaxis2=dict(title="Jobs", overlaying="y", side="right")),
                                #yaxis_title="Temperature (°C)", yaxis2_title="Jobs", showlegend=True)
   
    return simple_figure

@app.callback(
    Output(component_id="rs10", component_property="figure"),
    #Input("line-selector", "value"),
    Input("date-range", "start_date"),
    Input("date-range", "end_date"),
)
def update_rs10(start_date, end_date):
    filtered_data = rs10.query(
        "date >= @start_date and date <= @end_date"
    )
    # trace1 = go.Scatter(x=filtered_data["date"], y=filtered_data["server room temp"], mode='lines', name='server room temp')
    # trace2 = go.Scatter(x=filtered_data["date"], y=filtered_data["outdoor temp"], mode='lines', name='outdoor temp')
    # selected_traces = [trace for trace in [trace1, trace2] if trace['name'] in selected_lines]
    # fig = go.Figure()
    # for trace in selected_traces:
    #     fig.add_trace(trace)
    #return {'data': selected_traces}
    simple_figure = px.line(x=filtered_data["date"], y=filtered_data["server room temp"], title="rs10 (🌹)")
    simple_figure.add_scatter(x=filtered_data["date"], y=filtered_data["outdoor temp"], mode='lines', name='outdoor temp')
    simple_figure.add_scatter(x=filtered_data["date"], y=filtered_data["total jobs"], mode='lines', name='total jobs', yaxis="y2")
    simple_figure.update_layout(xaxis_title="Date", yaxis=dict(title='Temperature °C'), yaxis2=dict(title="Jobs", overlaying="y", side="right")),
    #simple_figure.update_layout(xaxis_title="Date", yaxis_title="Temperature (°C)")
   
    return simple_figure


def serve_layout():
    '''Define the layout of the application'''
    return html.Div(
        children = [
            html.Div(
                children = [
                    html.P(children="🌹", className="header-emoji"),
                    html.H1(children="Cluster Monitoring", className="header-title"),
                    html.P(
                        children=(
                            "Insights into our clusters"
                        ),
                        className="header-description",
                    ),
                ],
                className="header",
            ),
            #login_location,
            #navbar,
            #simple_plot,
            # dbc.Container(
            #     dash.page_container,
            #     class_name='my-2'
            # ),
            #footer
            html.Div(
                children=[
                    html.Div(
                        children=[
                            html.Div(
                                children="Date Range", className="menu-title"
                            ),
                            dcc.DatePickerRange(
                                id="date-range",
                                min_date_allowed=datetime.date(2023, 7, 24),#.date(),
                                max_date_allowed=rs02["date"].max(),#.date(),
                                start_date=datetime.date(2023, 7, 24),#.date(),
                                end_date=rs02["date"].max(),#.date(),
                            ),
                        ]
                    ),
                ],
                className="menu",
            ),
            html.Div(
                children=[
                    # dcc.Checklist(
                    #     id='line-selector',
                    #     options=[
                    #         {'label': 'server room temp', 'value': 'server room temp'},
                    #         {'label': 'outdoor temp', 'value': 'outdoor temp'},
                    #     ],
                    #     value=['server room temp', 'outdoor temp'],  # Initial lines to show
                    #     labelStyle={'display': 'inline-block'}
                    # ),
                    html.Div(
                        children = dcc.Graph(
                            id="simple_plot",
                            config={"displayModeBar": False},
                            #figure={"data": [trace1, trace2]}
                        ),
                        className="card",
                    ),
                    html.Div(
                        children = dcc.Graph(
                            id="rs10",
                            config={"displayModeBar": False},
                            #figure={"data": [trace1, trace2]}
                        ),
                        className="card",
                    ),
                ],
                className="wrapper",
            ),
        ]
    )


app.layout = serve_layout   # set the layout to the serve_layout function
#server = app.server         # the server is needed to deploy the application




if __name__ == "__main__":
    app.run_server(
        #host=APP_HOST,
        #port=APP_PORT,
        debug=True #APP_DEBUG,
        #dev_tools_props_check=DEV_TOOLS_PROPS_CHECK
    )

