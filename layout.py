import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import plotly.graph_objects as go

import dash
from dash.dependencies import Input, Output

app = dash.Dash()  # initialising dash app
df = px.data.stocks()  # reading stock price dataset
print(df)


# def stock_prices():
#     # line chart showing Google stock prices over time
#     fig = go.Figure(
#         [
#             go.Scatter(
#                 x=df["date"],
#                 y=df["AAPL"],
#                 line=dict(color="firebrick", width=4),
#                 name="Google",
#             )
#         ]
#     )
#     fig.update_layout(
#         title="Prices over time", xaxis_title="Dates", yaxis_title="Prices"
#     )

#     return fig


app.layout = html.Div(
    id="parent",
    children=[
        html.H1(
            id="H1",
            children="Stock Prices Dashboard",
            style={"textAlign": "center", "marginTop": 40, "marginBottom": 40}
        ),
        dcc.Dropdown(
            id="dropdown",
            options=[
                {"label": "Google", "value": "GOOG"},
                {"label": "Apple", "value": "AAPL"},
                {"label": "Amazon", "value": "AMZN"},
                {"label": "Microsoft", "value": "MSFT"}
            ],
            value="GOOG"
        ),
        dcc.Graph(id="line_plot")  # figure=stock_prices()
    ],
)


@app.callback(
    Output(component_id="line_plot", component_property="figure"),
    [Input(component_id="dropdown", component_property="value")]
)
def graph_update(dropdown_value):
    print(f"This is our dropdown_value: {dropdown_value}")
    fig = go.Figure(
        [
            go.Scatter(
                x=df["date"],
                y=df[f"{dropdown_value}"],
                line=dict(color="firebrick", width=4)
            )
        ]
    )

    fig.update_layout(
        title="Stock Prices Dashboard", xaxis_title="Dates", yaxis_title="Prices"
    )

    return fig


if __name__ == "__main__":
    app.run_server()
