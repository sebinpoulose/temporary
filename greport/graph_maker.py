import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd


df1 = pd.read_csv("./trail.csv")

fig = make_subplots(
    rows=7, cols=1,
    vertical_spacing=0.03,
    specs=[[{"type": "table"}],
           [{"type": "scatter"}],
            [{"type": "scatter"}],
            [{"type": "scatter"}],
            [{"type": "scatter"}],
           [{"type": "scatter"}],
[{"type": "scatter"}]

           ],subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4", "plot 5","plot 6","plot 7")
)

fig.update_layout()


qe = 7
for elem in df1['TestName'].unique():
    temp = df1.loc[df1['TestName'] == elem]
    fig.add_trace(go.Scatter(
        x=temp["ParameterName"],
        y=temp["Result"],
        mode="markers",
        name="mining revenue",),
        row=qe, col=1
        )
    qe -= 1

fig.add_trace(
    go.Table(
        header=dict(
            values=["TestName", "ParameterName", "Result",
                    "ResultDatetime", "Normal", "ReferenceRange"],
            font=dict(size=10),
            align="left"
        ),
        cells=dict(
            values=[df1[k].tolist() for k in df1.columns[1:]],
            align="left")
    ),
    row=1, col=1
)
fig.update_layout(
    height=2800,
    showlegend=False,
    title_text="Graphical Report for patient : 64842246",
    )



fig.show()
