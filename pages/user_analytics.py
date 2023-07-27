import dash

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
dash.register_page(__name__, path='/user_analytics')

df = px.data.tips()
days = df.day.unique()
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}
layout = html.Div(
    [
        dcc.Dropdown(
            id="dropdown",
            options=[{"label": x, "value": x} for x in days],
            value=days[0],
            clearable=False,
            style={"width": "50%"}
        ),
        dcc.Graph(id="bar-chart"),
    ],
    style=CONTENT_STYLE
)


@callback(Output("bar-chart", "figure"), Input("dropdown", "value"))
def update_bar_chart(day):
    mask = df["day"] == day
    fig = px.bar(df[mask], x="sex", y="total_bill", color="smoker", barmode="group")
    return fig