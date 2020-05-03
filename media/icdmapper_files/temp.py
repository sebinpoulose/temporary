import plotly
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from greport import loader


def make_graph(pid):
    a = loader.get_data_object(pid)
    specs = []
    row = len(a)

    titles = []
    for elem in a:
        specs.append([{"type": "bar"}])
        titles.insert(0, elem[1]+" on "+elem[0])

    fig = make_subplots(rows=row, cols=1, horizontal_spacing=0.3,
                        column_width=[500], specs=specs, subplot_titles=tuple(titles))

    for elem in a:
        color = []
        paraname = []
        reslist = []
        for ele in elem[2]:
            paraname.append(ele[0])
            reslist.append(ele[2])
            if ele[1] == "N":
                color.append("green")
            elif ele[1] == "H":
                color.append("red")
            else:
                color.append("blue")

        fig.add_trace(go.Bar(y=paraname, x=reslist, marker=dict(color=color),
                             width=.3, orientation="h",), row=row, col=1)
        print(color)
        row -= 1

    fig.update_layout(
        height=4000,
        showlegend=False,
        title_text="Graphical Report for patient : ",
    )
    plotly.offline.plot(fig, filename='reporttest.html', auto_open=False)


df = pd.read_csv("Lab-Results-07112019.csv")
df = df[df['ParameterName'] != 'Comment']
df = df[df['Result'] != 'Subhead']
df = df[df['Result'] != 'SubHead']
df = df[pd.to_numeric(df['Result'], errors='coerce').notnull()]
print(len(df['PatientID'].unique()))
for pid in df['PatientID'].unique():
    temp = df.loc[df['PatientID'] == pid]
    for test in temp['TestName'].unique():
        temp = temp.loc[temp['TestName'] == test]
        if len(temp['ResultDatetime'].unique()) > 1:
            print(pid, test, len(temp['ResultDatetime'].unique()))

"""
only 15 out of 200 patients have trend possibility
35102389 Blood Routine Examination ( CBC With ESR ) 2
57441216 Electrolytes 2                                     - nice perfect
57513050 APTT 2
64762523 APTT 2                                             - working
64772001 Blood Routine Examination ( CBC With ESR ) 2       - wrong
64870925 Platelet Count 2
64927058 Electrolytes 2
64931118 Blood Routine Examination ( CBC With ESR ) 2
64938636 Complete Haemogram ( CBC ) 2
64945895 Electrolytes 2
64948779 APTT 2
64950389 Calcium ( serum ) 2
64951677 Blood Routine Examination ( CBC With ESR ) 2
64951698 Bilirubin Total 2
64952860 CBC With IT Ratio  ( Neonatal ) 2
"""
