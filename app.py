import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from downloading import Loader
from plotting import Plotter
from preprocessing import Preprocessor
import pandas as pd


stocks = ['PLAN', 'T', 'BVB.DE', 'BTI', 'CNK', 'INTC']
load = Loader('1d')
process = Preprocessor('Close')
plotter = Plotter('Stock Analysis', 'return', 'rolling_mean')

total_df = pd.DataFrame()
for name in stocks:
    df = load.download(name, '2021-01-01', '2021-04-20')
    df = process.addStatistics(df, 10)
    total_df = total_df.append(df)

app = dash.Dash(__name__)

app.layout = html.Div([

    html.H1("Analysis of exact stocks", style={'text-align': 'center'}),

    dcc.Dropdown(id="select stock's Ticker",
                 options=[
                     {"label": "ANAPLAN", "value": 'PLAN'},
                     {"label": "British American Tobacco", "value": 'BTI'},
                     {'label': 'Borussia', 'value': 'BVB.DE'}],
                 multi=False,
                 value='ANAPLAN',
                 style={'width': "40%"}
                 ),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='stock', figure={})

])

# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='stock', component_property='figure')],
    [Input(component_id="select stock's Ticker", component_property='value')]
)

def update_graph(option_slctd):
    print(option_slctd)
    print(type(option_slctd))

    container = "The stock chosen by you is: {}".format(option_slctd)
    current_df = total_df[total_df['ticker']==option_slctd]
    fig = plotter.plotChart(current_df, 20)
    return container, fig


if __name__ == '__main__':
    app.run_server(debug=True)