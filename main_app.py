import pandas as pd
import numpy as np
import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html, dash_table, State
from dash.dependencies import Input, Output
import plotly_express as px
import pandas_datareader.data as web
import datetime
import base64

app = dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP])


# styling the sidebar
SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16.5rem",
    "padding": "2rem 1rem",
    "background-color": "rgb(233 249 255)",
    "color": "#000000",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "overflow": "hidden"
}

nav_style = {
    "font-family": "fangsong",
    "line-height": "inherit",
    "font-size": "16px",
    "color": "black"
}
img_style = {
    'height': '200px',
    'width': '212px',
    'margin-bottom': '-72px',
    'margin-top': '-69px'
}


logo = base64.b64encode(open('assets\\logo.png', 'rb').read()).decode('ascii')

sidebar = html.Div(
    [
        html.Img(src='data:image/png;base64,{}'.format(logo),
                 alt="logo", style=img_style),
        html.Hr(),

        dbc.Nav(
            [   
                dbc.NavLink("Home", href="/", active="exact", style=nav_style),
                dbc.NavLink("Email Behavior", href="/emailBehavior",
                            active="exact", style=nav_style),
                dbc.NavLink("Logon Behavior", href="/logonBehavior",
                            active="exact", style=nav_style),
                dbc.NavLink("File Behavior", href="/fileBehavior",
                            active="exact", style=nav_style),
                dbc.NavLink("Http Behavior", href="/http",
                            active="exact", style=nav_style),
                dbc.NavLink("Device Behavior", href="/deviceBehavior",
                            active="exact", style=nav_style),
                dbc.NavLink("Dataset Insights", href="/dataset",
                            active="exact", style=nav_style)
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    html.Link(rel="stylesheet", href="/assets/custom.css"),
    sidebar,
    content,
    dash.page_container
])

if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
