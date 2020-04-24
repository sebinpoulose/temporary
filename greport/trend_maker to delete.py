import plotly
import plotly.graph_objects as go
import pandas as pd


def make_trend(pid, testname):
    global title
    title = ""
    df = pd.read_csv("./media/Lab-Results-07112019.csv", header=0,
                     names=['PatientID', 'TestName', 'ParameterName', 'Result',
                            'ResultDatetime', 'Normal', 'ReferenceRange'])
    df = df.loc[df['PatientID'] == int(pid)]
    df = df.loc[df['TestName'] == testname]
    df = df[df['ParameterName'] != 'Comment']
    df = df[df['ParameterName'] != 'Comment:']
    df = df[df['Result'] != 'Subhead']
    df = df[df['Result'] != 'SubHead']
    df = df.sort_values('Normal', ascending=False)
    color = []
    for ele in df['Normal']:
        if ele == "N":
            color.append("green")
        elif ele == "H":
            color.append("red")
        else:
            color.append("blue")
    if len(df['ResultDatetime'].unique()) > 1:
        title += "Trend for "+testname
        data = []
        for elem in df['ResultDatetime'].unique():
            temp = df.loc[df['ResultDatetime'] == elem]
            data.append(
                    go.Bar(name=elem, x=temp['ParameterName'], y=temp['Result'],
                           text=temp['Result'], textposition='auto', width=0.3,
                           marker=dict(color=color),
                           ))
        fig = go.Figure(data=data)
        fig.update_layout(barmode='group')
    else:
        title += "Graph for "+testname+" on "+df['ResultDatetime'].unique()[0]
        dateandhour = df['ParameterName']
        values = df['Result']
        fig = go.Figure(data=[
            go.Bar(name='Present', x=dateandhour, y=values, text=values,
                   textposition='auto', width=0.3, marker=dict(color=color),)])
    fig.update_layout(
            title=title, xaxis_title="Parameters", yaxis_title="Values",
            font=dict(family="Courier New, monospace", size=24, color="#0f0f0f"))
    plotly.offline.plot(fig, filename='./templates/report.html', auto_open=False)
