import dash

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
dash.register_page(__name__, path='/data')

df = px.data.tips()
days = df.day.unique()
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
layout = html.Div(
    [
        html.P('this is data page')
    ],
    
    style=CONTENT_STYLE
)

