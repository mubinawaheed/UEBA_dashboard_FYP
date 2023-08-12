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

img_style_nu = {
    'max-width': '115px',
    'height': '131px',
    'margin-top': '-34px',
    'margin-left': '62px'
}
timerImg = {
    'width': '137px',
    'margin-bottom': '23px',
    'margin-top': '-14px',
    'margin-left': '47px'
}

normaluser = base64.b64encode(
    open('assets\\normaluser.png', 'rb').read()).decode('ascii')
mal_user = base64.b64encode(
    open('assets\\mal_user.png', 'rb').read()).decode('ascii')
timer = base64.b64encode(
    open('assets\\timer.png', 'rb').read()).decode('ascii')


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
                     detects anomalies and suspicious activities in the user behavior.",
                        style={"font-family": "fangsong", "font-size": "14px", "color": "#444040", "text-align": "justify",
                               "margin-top": "1px",
                               },))
            ], xs=12, sm=12, md=12, lg=11, xl=11,)
            ]
            # f1f9d0; #bac880
        ),
        dbc.Row([
            dbc.Col([
                html.H2("Dataset Insights",
                        style=heading_style, className="my-2")
            ])
        ]),
        dbc.Row([
            dbc.Col([html.P("The dataset used in this research is Carnegie Mellon Univserity certified Insider Threat Dataset version r4.2",
                            style={"font-family": "fangsong", "font-size": "14px", "color": "#444040", "text-align": "justify",
                                   "margin-top": "1px", })])
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        "Malicious Insiders", className='text-center', style={'font-size': '20px'}),
                    dbc.CardBody(html.P('70', className="card-text", style={'color': '#3b6cc5', 'font-size': '30px', 'font-weight': 'bold', 'text-align': 'center'
                                                                            })),
                    html.Img(
                        src='data:image/png;base64,{}'.format(mal_user),
                        alt="User Image",
                        style=img_style_nu
                    ),
                ], style={"width": "14rem", 'margin-bottom': '10px'},
                )], width={'size': 4, 'order': 1}),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        "Normal users", className='text-center', style={'font-size': '20px'}),
                    dbc.CardBody(html.P('930', className="card-text", style={'color': '#3b6cc5', 'font-size': '30px', 'font-weight': 'bold', 'text-align': 'center'
                                                                             })),
                    html.Img(
                        src='data:image/png;base64,{}'.format(normaluser),
                        alt="User Image",
                        style=img_style_nu
                    ),
                ], style={"width": "14rem", 'margin-bottom': '10px'},
                )], width={'size': 4}),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        "Timeline", className='text-center', style={'font-size': '20px'}),
                    dbc.CardBody(html.P('18 months', className="card-text", style={'color': '#3b6cc5', 'font-size': '30px', 'font-weight': 'bold', 'text-align': 'center'
                                                                                   })),
                    html.Img(
                        src='data:image/png;base64,{}'.format(timer),
                        alt="timer Image",
                        style=timerImg
                    ),

                ], style={"width": "14rem", 'margin-bottom': '10px'},
                )], width={'size': 4, 'order': 1}),
        ],
            style={'justify-content': 'center'}
        ),


    ],
    # fluid=True,
    # className="g-0",
    style=CONTENT_STYLE,
)
