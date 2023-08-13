import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import base64,os
import pandas as pd
import datetime

dash.register_page(__name__, path='/logonBehavior')

usernames = os.listdir("E:\\UEBA_Notebooks\\user_files")

CONTENT_STYLE = {
    "margin-left": "12.5rem",
    "margin-right": "2rem",
    "padding": "1rem 1.2rem",
}

Headingstyle={
    'text-align': 'center',
    "font-family": "fangsong",
    'font-weight': 'bold',
    'margin-top': "-51px",
    'color':'#2f71b2'
}

optionStyle={
    "width": "550px",
    "display": "inline-block",
    "margin-left":"60px"
}

graphstyle={
    "height": "420px",
    'width':'820px',
    'margin-left':'50px'
}

layout = dbc.Container([

    dbc.Row([
        dbc.Col([
            html.H2("Logon Analysis", style=Headingstyle)
        ])
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id="users", multi=False, value="AAF0535.csv", placeholder="User", 
            
            options=[{"label": i, "value": i} for i in sorted(usernames)],
            style=optionStyle, optionHeight=30,)],
            xs=12, sm=12, md=12, lg=11, xl=11,) 
            ], justify="center"
        ),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='Logon_Attempts', figure={}, 
            style=graphstyle)
        ]),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='logon_graph', figure={}, 
            style=graphstyle)])
    ]),
],
style=CONTENT_STYLE)

def plot_graph(dataframe, xcol, ycol, title):
    dataframe["date"] = pd.to_datetime(dataframe[xcol])

    # this piece of code is especially added to cater empty files in file_copied directory
    if dataframe.empty:
        start_date = '2010-01-02'
        end_date = '2011-05-16'
        dates = pd.date_range(start=start_date, end=end_date, freq='D')
        dataframe['date'] = dates
        dataframe[ycol] = 0

    fig = px.bar(dataframe, x="date", y=ycol, range_x=[dataframe["date"].min(), dataframe["date"].max()])

    fig.update_layout(title={'text': title, 'y': 0.9},title_x=0.5, font=dict(size=10))
    fig.update_traces(marker_color='#3E6DE3')

    fig.update_yaxes(title_standoff=0)

    if dataframe[ycol].sum() == 0:
        fig.update_traces(marker_line_color='#3E6DE3', marker_line_width=4)

    return fig

@callback(
    Output('Logon_Attempts', 'figure'),
    Input('users', 'value')
)
def plot_logon_attempts(user):
    df = pd.read_csv(f"E:\\UEBA_Notebooks\\Logon Attempts all users\\{user[0:7]}_logonAttempts.csv")
    fig = plot_graph(df, 'date', 'Logon attempts',f"Count of Logon attempts per day of user {user[0:7]}")
    return fig

@callback(
    Output("logon_graph", "figure"),
    Input("users", "value")
)
def plot_logon_graphs(user):
    df = pd.read_csv(
        f"E:\\UEBA_Notebooks\\after_hour_logon_userfiles\\{user[0:7]}_after_hour_logon.csv")
    fig = plot_graph(df, 'date', 'after_hour_logon',f'Count of after hour Logons of user {user[0:7]}')
    return fig