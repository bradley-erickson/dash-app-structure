from dash import dcc, html
from utils.preprocess_data import get_test_data

data = get_test_data()
#print(data.head())

simple_plot = (
    html.Div(
        children=[
            html.Div(
                children=[
                    html.Div(
                        children="Date Range", className="menu-title"
                    ),
                    dcc.DatePickerRange(
                        id="date-range",
                        min_date_allowed=data["date"].min().date(),
                        max_date_allowed=data["date"].max().date(),
                        start_date=data["date"].min().date(),
                        end_date=data["date"].max().date(),
                    ),
                ]
            ),
        ],
        className="menu",
    ),
    html.Div(
                children=[
                    html.Div(
                    children = dcc.Graph(
                        id="simple_plot",
                        config={"displayModeBar": False},
                        # figure={
                        #     "data": [
                        #         {
                        #             "x": data["date"],
                        #             "y": data["server room temp"],
                        #             "type": "lines",
                        #         },
                        #     ],
                        #     "layout": {
                        #             "title": {
                        #                 "text": "Server room temp with time",
                        #                 "x": 0.05,
                        #                 "xanchor": "left",
                        #             },
                        #             "xaxis": {"fixedrange": True},
                        #             "yaxis": {
                        #                 "tickprefix": "$",
                        #                 "fixedrange": True,
                        #             },
                        #             "colorway": ["#17b897"],
                        #     },
                        # },
                    ),
                    className="card",
                ),
                ],
                className="wrapper",
)
)