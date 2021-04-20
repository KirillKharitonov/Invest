import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Plotter:

    def __init__(self, title, return_col, rolling_col):
        self.title = title
        self.return_col = return_col
        self.rolling_col = rolling_col

    def plotChart(self, df, n, daily=True):
        fig = make_subplots(rows=1, cols=2, column_widths=[2, 1],
                            specs=[[{"secondary_y": True}, {"secondary_y": True}]])
        fig.add_trace(go.Candlestick(x=df.Date,
                                     open=df.Open,
                                     high=df.High,
                                     low=df.Low,
                                     close=df.Close), 1, 1)
        fig.add_trace(go.Line(x=df.Date, y=df[self.rolling_col], name='Rolling mean'), 1, 1, secondary_y=False)
        fig.add_trace(go.Line(x=df.Date, y=df[self.return_col], name='Return'), 1, 1, secondary_y=True)
        fig.add_trace(go.Histogram(x=df[self.return_col], name='Distribution of Returns',
                                   nbinsx=n, histnorm='probability density'), 1, 2)
        if daily == True:
            fig.update_xaxes(
                rangeslider_visible=True,
                rangebreaks=[dict(bounds=["sat", "mon"])]
            )
            fig.layout.yaxis2.title = "Return"
            fig.update_xaxes(title='Дневная доходность', col=2, row=1)
        else:
            fig.update_xaxes(
                rangeslider_visible=True,
                rangebreaks=[
                    dict(bounds=["sat", "mon"]),
                    dict(bounds=[19, 9.5], pattern="hour")
                ]
            )
            fig.layout.yaxis2.title = "Return"
            fig.update_xaxes(title='Доходность', col=2, row=1)
        fig.update_layout(
            title=self.title,
            #yaxis_title=df.ticker[0],
            xaxis_rangeslider_visible=False,
            height=1000,
            width=2500
        )
        #fig.show()
        return fig