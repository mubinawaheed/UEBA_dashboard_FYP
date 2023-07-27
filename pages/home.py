import dash
import pandas as pd
from dash import html, dcc, callback
import plotly_express as px
import plotly.graph_objects as go
import os
import datetime
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

dash.register_page(__name__, path="/")
usernames = os.listdir("E:\\UEBA_Notebooks\\user_files")

CONTENT_STYLE = {
    "overflow-x": "hidden",
    "padding": "0.5rem 0.5rem",
}

heading_style = {
    "font-family": "monospace",
    "line-height": "inherit",
    "font-size": "1.55rem",
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
                     detects anomalies and suspicious activities in the user behavior.",
                        style={"font-family": "monospace", "font-size": "12px", "color": "#444040", "text-align": "justify",
                               "margin-top": "1px",
                               },))
            ], xs=12, sm=12, md=12, lg=11, xl=11,)
            ]
            # f1f9d0; #bac880
        ),
        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        "Accuracy", className='text-center', style={'font-size': '25px'}),
                    dbc.CardBody(html.P('To be added', className="card-text", style={'color': '#3b6cc5', 'font-size': '30px', 'font-weight': 'bold', 'text-align': 'center'
                                                                                     })),
                ], style={"width": "15rem", 'margin-bottom': '10px'},
                )]),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        "Total Malicious Insiders", className='text-center', style={'font-size': '20px'}),
                    dbc.CardBody(html.P('70', className="card-text", style={'color': '#3b6cc5', 'font-size': '30px', 'font-weight': 'bold', 'text-align': 'center'
                                                                            })),
                ], style={"width": "15rem", 'margin-bottom': '10px'},
                )]),
            dbc.Col([
                dbc.Card([
                    dbc.CardHeader(
                        "Normal users", className='text-center', style={'font-size': '25px'}),
                    dbc.CardBody(html.P('930', className="card-text", style={'color': '#3b6cc5', 'font-size': '30px', 'font-weight': 'bold', 'text-align': 'center'
                                                                             })),
                ], style={"width": "15rem", 'margin-bottom': '10px'},
                )]),
        ],
            style={'margin-left': '2rem', 'margin-bottom': '5px'}
        ),
        dbc.Row(
            [dbc.Col([dcc.Dropdown(id="users", multi=False, value="AAF0535.csv", placeholder="User", options=[
                {"label": i, "value": i} for i in sorted(usernames)], style={"width": "550px", "display": "inline-block"},
                optionHeight=30,),

                html.H3(id='user_name', style={
                        'text-align': 'center', "font-family": "monospace", 'font-weight': 'bold', 'margin-top': "11px"}),

                dcc.Graph(id="emailgraph", figure={}, style={
                          "height": "425px", "margin-top": "-2px"}),
                html.H4("Training Data", style={
                        "font-family": "monospace", 'font-size': '20px'}),
                html.P("The data has been trained on CMU-certified insider threat dataset r4.2",
                       style={"font-family": "monospace", "font-size": "12px", "color": "#444040", "text-align": "justify"})
            ],
                xs=12, sm=12, md=12, lg=11, xl=11,)
            ], justify="center",
        ),
        dbc.Row([dbc.Col([
            dcc.Graph(id='connect_graph', figure={}, style={
                      "height": "330px", "margin-top": "-2px"})
        ], xs=12, sm=12, md=12, lg=6, xl=6,
            # width={'size':6}
            ),
                dbc.Col([
                    dcc.Graph(id='logon_graph', figure={}, style={
                                "height": "330px", "margin-top": "-2px"})
                ], xs=12, sm=12, md=12, lg=6, xl=6)
            ], align="center"
        ),

        dbc.Row([
            dbc.Col([
                dcc.Graph(id='after_hour_emails', figure={}, style={
                          "height": "330px", "margin-top": "-2px"})
            ], xs=12, sm=12, md=12, lg=6, xl=6),

            dbc.Col([
                dcc.Graph(id='files_copied', figure={}, style={
                          "height": "310px", "margin-top": "-2px"})
            ], xs=12, sm=12, md=12, lg=6, xl=6)
        ]),

        dbc.Row([
            dbc.Col([
                dcc.Graph(id='Logon_Attempts', figure={}, style={
                          "height": "330px", "margin-top": "-2px"})
            ], xs=12, sm=12, md=12, lg=6, xl=6),

            dbc.Col([
                dcc.Graph(id='email_attachments', figure={}, style={
                          "height": "310px", "margin-top": "-2px"})
            ], xs=12, sm=12, md=12, lg=6, xl=6)
        ])

    ],
    className="g-0",
    style=CONTENT_STYLE,
)
# helper function


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
    Output('user_name', 'children'),
    Input('users', "value")
)
def display_username(value):
    return f'Behavior of user {value}'


@callback(Output("emailgraph", "figure"), Input("users", "value"))
def plot_email_graph(user):
    df = pd.read_csv(f"E:\\UEBA_Notebooks\\user_files\\{user}")
    df["date"] = pd.to_datetime(df["str_date"])
    colors = ['#FF4533', '#FFA833', '#3E6DE3']
    fig = px.bar(df, x="date", y=df.columns[1:4], color_discrete_sequence=colors, range_x=[
                 df["date"].min(), df["date"].max()])
    fig.update_layout(title={'text': "Count of email sentiments",
                      'y': 0.9}, title_x=0.5, font=dict(size=10))
    return fig


@callback(
    Output("connect_graph", "figure"),
    Input("users", "value")
)
def plot_connect_graphs(user):
    df = pd.read_csv(f"E:\\UEBA_Notebooks\\user_files\\{user}")
    fig = plot_graph(df, 'str_date', 'Connect', 'Count of USB connects')
    return fig


@callback(
    Output("logon_graph", "figure"),
    Input("users", "value")
)
def plot_logon_graphs(user):
    df = pd.read_csv(
        f"E:\\UEBA_Notebooks\\after_hour_logon_userfiles\\{user[0:7]}_after_hour_logon.csv")
    fig = plot_graph(df, 'date', 'after_hour_logon',
                     'Count of after hour Logons')
    return fig


@callback(
    Output("after_hour_emails", "figure"),
    Input("users", "value")
)
def after_hour_emails(user):
    df = pd.read_csv(
        f"E:\\UEBA_Notebooks\\after_hour_Email_userfiles\\{user[0:7]}_after_hour_emails.csv")
    fig = plot_graph(df, 'date', 'After_hour_emails',
                     "Count of after hour emails sent")
    return fig


@callback(
    Output('files_copied', 'figure'),
    Input('users', 'value')
)
def plot_files_copied(user):
    df = pd.read_csv(
        f"E:\\UEBA_Notebooks\\files_copied_userfiles\\file_features_{user[0:7]}.csv")
    fig = plot_graph(df, 'str_date', 'files_copied',
                     "Count of files copied per day")
    return fig

@callback(
    Output('Logon_Attempts', 'figure'),
    Input('users', 'value')
)
def plot_files_copied(user):
    df = pd.read_csv(
        f"E:\\UEBA_Notebooks\\Logon Attempts all users\\{user[0:7]}_logonAttempts.csv")
    fig = plot_graph(df, 'date', 'Logon attempts',
                     "Count of Logon attempts per day")
    return fig


@callback(
    Output('email_attachments', 'figure'),
    Input('users', 'value')
)
def plot_files_copied(user):
    df = pd.read_csv(
        f"E:\\UEBA_Notebooks\\no_of_email_attachments\\{user[0:7]}_attachments.csv")
    fig = plot_graph(df, 'date', 'attachments',
                     "No of email attachments per day")
    return fig
