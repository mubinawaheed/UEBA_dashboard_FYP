import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import base64

dash.register_page(__name__, path='/dataset')

CONTENT_STYLE = {
    "margin-left": "17rem",
    "margin-right": "2rem",
    "padding": "1rem 1rem",
    "margin-top":"-62px"
}

heading_style = {
    "font-family": "fangsong",
    "font-weight": "bold",
    "line-height": "inherit",
    "font-size": "1.55rem",
    # "margin-top": "-47px",
    'color': '#2f71b2'
}
img_style_nu = {
    'max-width': '115px',
    'height': '131px',
    'margin-top': '-34px',
    'margin-left': '50px'
}
timerImg = {
    'width': '137px',
    'margin-bottom': '23px',
    'margin-top': '-14px',
    'margin-left': '47px'
}
textstyle={
    "font-family": "fangsong",
    "font-size": "16.5px",
    "color": "#444040",
    "text-align": "justify",
    "margin-top": "1px"
}

tagstyle={
    'color': '#3b6cc5',
    'font-size': '30px',
    'font-weight': 'bold',
    'text-align': 'center'
 }

normaluser = base64.b64encode(
    open('assets\\normaluser.png', 'rb').read()).decode('ascii')
mal_user = base64.b64encode(
    open('assets\\mal_user.png', 'rb').read()).decode('ascii')
timer = base64.b64encode(
    open('assets\\timer.png', 'rb').read()).decode('ascii')


layout = dbc.Container([
    dbc.Row(
        [dbc.Col(
            [html.Div(html.H2("Dataset Insights", style=heading_style, className="text-center my-2")),
             html.Hr(), ], xs=10, sm=10, md=10, lg=10, xl=10)]),

    dbc.Row([
        dbc.Col([html.P(["The dataset used in this research is ", html.Strong(" Carnegie Mellon Univserity "), "certified Insider Threat Dataset version r4.2"],
                        style=textstyle)], xs=12, sm=12, md=12, lg=11, xl=11,)
    ]),
    dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        "Malicious Insiders", className='text-center', style={'font-size': '20px'}),
                    dbc.CardBody(html.P('70', className="card-text", style=tagstyle)),
                    html.Img(
                        src='data:image/png;base64,{}'.format(mal_user),
                        alt="User Image",
                        style=img_style_nu
                    ),
                ], style={"width": "13rem", 'margin-top': '10px'},
                )], width={'size': 3}),

            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        "Normal users", className='text-center', style={'font-size': '20px'}),
                    dbc.CardBody(html.P('930', className="card-text", style=tagstyle)),
                    html.Img(
                        src='data:image/png;base64,{}'.format(normaluser),
                        alt="User Image",
                        style=img_style_nu
                    ),
                ], style={"width": "13rem",'margin-top': '10px'},
                )], width={'size': 3}),

            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        "Timeline", className='text-center', style={'font-size': '20px'}),
                    dbc.CardBody(html.P('18 months', className="card-text", style=tagstyle)),
                    html.Img(
                        src='data:image/png;base64,{}'.format(timer),
                        alt="timer Image",
                        style=timerImg
                    ),

                ], style={"width": "13rem",'margin-top': '10px'},
                )], width={'size': 3}),

            ],
            # style={'justify-content': 'center'}
            ),


], style=CONTENT_STYLE)
