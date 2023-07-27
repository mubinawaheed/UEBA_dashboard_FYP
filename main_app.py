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

app=dash.Dash(__name__, use_pages=True, external_stylesheets=[dbc.themes.BOOTSTRAP],
        meta_tags=[{'name':'viewport','content':'width=device-width, initial-scale:1.0'}])


app.layout=html.Div([
    dash.page_container
    ]
)

if __name__=='__main__':
    app.run_server(debug=True,port=3000)