import dash
import dash_bootstrap_components as dbc
from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import base64,os
import pandas as pd
import datetime

dash.register_page(__name__, path='/emailBehavior')

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

layout = dbc.Container([
    dbc.Row([
        dbc.Col([
            html.H2("Email Analysis", style=Headingstyle)
        ])
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Dropdown(id="users", multi=False, value="AAF0535.csv", placeholder="User", 
            
            options=[{"label": i, "value": i} for i in sorted(usernames)],
            style={"width": "550px", "display": "inline-block", "margin-left":"70px"},optionHeight=30,)],
            xs=12, sm=12, md=12, lg=11, xl=11,) 
            ], justify="center"
        ),

    dbc.Row([
        dbc.Col([dcc.Graph(id="emailgraph", figure={}, 
        style={"height": "425px", "margin-top": "-2px", 'width':'895px', 'margin-left':'37px'})])
        ]),

     dbc.Row([
            dbc.Col([
                dcc.Graph(id='after_hour_emails', figure={}, style={"height": "400px", "margin-top": "-2px",'width':'895px', 'margin-left':'37px'})
            ])
        ]),
    dbc.Row([
        dbc.Col([
                dcc.Graph(id='email_attachments', figure={}, style={"height": "400px", "margin-top": "-2px",'width':'895px', 'margin-left':'37px'})
            ])
    ])
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

    fig = px.bar(dataframe, x="date", y=ycol, range_x=[
                 dataframe["date"].min(), dataframe["date"].max()])
    fig.update_layout(title={'text': title, 'y': 0.9},
                      title_x=0.5, font=dict(size=10))
    fig.update_traces(marker_color='#3E6DE3')
    fig.update_yaxes(
        title_standoff=0)
    if dataframe[ycol].sum() == 0:
        fig.update_traces(marker_line_color='#3E6DE3', marker_line_width=4)

    return fig

@callback(
Output("emailgraph", "figure"),
 Input("users", "value"))

def plot_email_graph(user):
    df = pd.read_csv(f"E:\\UEBA_Notebooks\\user_files\\{user}")
    df["date"] = pd.to_datetime(df["str_date"])
    colors = ['#FF4533', '#FFA833', '#3E6DE3']
    fig = px.bar(df, x="date", y=df.columns[1:4], color_discrete_sequence=colors, range_x=[
                 df["date"].min(), df["date"].max()])
    fig.update_layout(title={'text': f"Count of email sentiments of user {user}",
                      'y': 0.9}, title_x=0.5, font=dict(size=10))
    return fig

@callback(
    Output("after_hour_emails", "figure"),
    Input("users", "value")
)
def after_hour_emails(user):
    df = pd.read_csv(
        f"E:\\UEBA_Notebooks\\after_hour_Email_userfiles\\{user[0:7]}_after_hour_emails.csv")
    fig = plot_graph(df, 'date', 'After_hour_emails',
                     f"Count of after hour emails sent by user {user[0:7]}")
    return fig


@callback(
    Output('email_attachments', 'figure'),
    Input('users', 'value')
)
def plot_email_attachments(user):
    df = pd.read_csv(
        f"E:\\UEBA_Notebooks\\no_of_email_attachments\\{user[0:7]}_attachments.csv")
    fig = plot_graph(df, 'date', 'attachments',
                     f"No of email attachments sent by user {user[0:7]} per day")
    return fig