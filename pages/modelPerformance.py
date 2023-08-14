import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import base64,os
import pandas as pd
import datetime

dash.register_page(__name__, path='/modelPerformance')

usernames = os.listdir("E:\\UEBA_Notebooks\\user_files")

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
    "font-size": "1.57rem",
    "text-align":"center",
    'color': '#2f71b2'
}

graphstyle={
    "height": "440px",
    'width':'950px',
    # 'margin-left':'20px'
}

layout = dbc.Container([

    dbc.Row(
        [dbc.Col([
            html.Div(html.H2("User Classification", style=heading_style)),
            html.Hr(), 
            ], xs=10, sm=10, md=10, lg=10, xl=10)]),

    dbc.Row([
        dbc.Col([
            html.Strong("Threshold = 0.01")
        ])
    ]),
    
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='user-graph-normal', figure={}, 
            style=graphstyle)])
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='user-graph-mal', figure={}, 
            style=graphstyle)])
    ]),
],
style=CONTENT_STYLE)


@callback(
    Output('user-graph-normal', 'figure'),
    Input('user-graph-normal', 'relayoutData')
)
def recon_error_normal_users(relayoutData):
    df = pd.read_csv(f"normal_users.csv")
    df_no_duplicates = df.drop_duplicates(subset='user', keep='first')
    fig = px.bar(df_no_duplicates, x="user", y='recon_error')

    fig.update_layout(title={'text': 'Value of reconstruction error for normal users', 'y': 0.9},title_x=0.5, font=dict(size=10))
    fig.update_traces(marker_color='#3E6DE3')

    return fig

@callback(
    Output('user-graph-mal', 'figure'),
    Input('user-graph-mal', 'relayoutData')
)
def recon_error_mal_users(relayoutData):
    df = pd.read_csv(f"mal_users.csv")
    fig = px.bar(df, x="user", y='recon_error')

    fig.update_layout(title={'text': 'Value of reconstruction error for malicious users', 'y': 0.9},title_x=0.5, font=dict(size=10))
    fig.update_traces(marker_color='#3E6DE3')

    return fig


