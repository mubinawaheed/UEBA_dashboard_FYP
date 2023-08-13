import dash
import pandas as pd
from dash import html, dcc, callback
import plotly_express as px
import plotly.graph_objects as go
import os
import datetime
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import base64
dash.register_page(__name__, path="/")

CONTENT_STYLE = {
    "margin-top": "-70px",
    "padding": "1rem",
    "margin-left": "16rem",
    "overflow": "hidden"
}

heading_style = {
    "font-family": "fangsong",
    "line-height": "inherit",
    "font-size": "1.55rem",
    "color":"#2f71b2",
    "font-weight":"bold"
}

accuracy_graph1 = base64.b64encode(open('autoen_acc.png', 'rb').read()).decode('ascii')
accuracy_graph2 = base64.b64encode(open('huber_loss.png', 'rb').read()).decode('ascii')

graph_style1 = {
    'height': '250px',
    'width': '350px',
    'marginLeft': "10px",
    "marginTop": "15px"
}

graph_style2 = {
    'height': '250px',
    'width': '350px',
    "marginTop": "15px"
}
caption_style={
    'font-size': '13px',
    'font-family': 'monospace',
    'margin-left': '130px',
}

textstyle={
    "font-family": "fangsong",
     "font-size": "14px",
    "color": "#444040",
    "text-align": "justify",
    "margin-top": "1px",
}

layout = dbc.Container(
    [
    dbc.Row(
        [dbc.Col(
            [html.Div(html.H2("User and Entity Behaviour Analysis (UEBA)", style=heading_style, className="my-2 text-center")
            ), html.Hr(), ], xs=12, sm=12, md=12, lg=11, xl=11)]
    ),
    
    dbc.Row(
        [dbc.Col([
            (html.P("User and entity behavior analytics is a statistical approach to mitigate insider threats and discover malicious insiders within an \
            organization. It monitors and analyzes user activities over a period of time and\
            detects anomalies and suspicious activities in the user behavior.", style=textstyle,))
        ], xs=12, sm=12, md=12, lg=11, xl=11,)
        ]
    ),

    dbc.Row([
        dbc.Col([
            html.H4("Model Performance - 83% Accurate", style=heading_style, className="my-2 mx-2")
        ])
    ]),

    dbc.Row([
    dbc.Col(
        [html.Figure([
            html.Img(src='data:image/png;base64,{}'.format(accuracy_graph1), alt="Model Accuracy", style=graph_style1),
            html.Figcaption("LSTM autoencoder", style=caption_style)]),
        ], width=6),

    dbc.Col(
        [html.Figure([
            html.Img(src='data:image/png;base64,{}'.format(accuracy_graph2), alt="Model Accuracy", style=graph_style2),
            html.Figcaption("LSTM autoencoder",style=caption_style)]),
        ], width=6),
    ])
    ],
    style=CONTENT_STYLE,
)
