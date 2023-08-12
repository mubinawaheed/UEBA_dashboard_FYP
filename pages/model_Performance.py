import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import base64

dash.register_page(__name__, path='/model_Performance')

CONTENT_STYLE = {
    "margin-left": "16rem",
    "margin-right": "2rem",
    "padding": "1rem 1rem",
}

heading_style = {
    "font-family": "fangsong",
    "font-weight": "bold",
    "line-height": "inherit",
    "font-size": "1.55rem",
    "margin-top": "-47px",
    'color':'#2f71b2'
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

layout = dbc.Container([
    dbc.Row(
        [dbc.Col(
            [html.Div(html.H2("Model Performance - 83% Accurate", style=heading_style, className="text-center")),
             html.Hr(), ], xs=12, sm=12, md=12, lg=11, xl=11)]),

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
], style=CONTENT_STYLE)
