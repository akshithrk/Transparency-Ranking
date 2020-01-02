import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
# from readers import *
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import csv, os
from pathlib import Path
import plotly.express as px
import pandas as pd
# from abs_path import return_abs_path, return_abs_path2

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.title = "Transparency Ranking"
app.layout = html.Div([
    html.H1(children="An effort to visualize model Re-ranking", style={'textAlign': 'center'}),
    html.Hr(),
    html.Div([
            html.H2("Across years"),
            html.Div(children="This task compares Original rank with the model re-rank of states for the selected year",
                style={'font-style': 'normal'}),
            html.Br(),
            html.Div(children="Years:", style={'font-style': 'italic'}),
            dcc.Dropdown(
                id="drop-down-year-task1",
                style={'color': '#000000', "width": "300px"},
                options=[
                    {'label': '2006', 'value': '2006'},
                    {'label': '2007', 'value': '2007'},
                    {'label': '2008', 'value': '2008'},
                    {'label': '2009', 'value': '2009'},
                    {'label': '2010', 'value': '2010'},
                    {'label': '2011', 'value': '2011'},
                    {'label': '2012', 'value': '2012'},
                    {'label': '2013', 'value': '2013'},
                    {'label': '2014', 'value': '2014'},
                    {'label': '2015', 'value': '2015'},
                    {'label': '2016', 'value': '2016'}],
                value="2006"),
            html.Br(),
            html.Hr(style={'border-style': 'dotted'}),
            html.H4("Small multiples of slope plots"),
            html.Div([
                dcc.Graph(
                    id='Vis-1-1',
                )
            ]),
            html.Br(),
            html.Br(),
        ])
])

#Task callback for Task 1
@app.callback(
    [Output('Vis-1-1', 'figure')],
    [Input("drop-down-year-task1", "value")]
)

def update_graph(year):
    df1 = pd.read_csv('finance datasets/all.csv')
    df = df1.loc[df1['1-qid'] == int(year)]
    fig = make_subplots(rows=5, cols=2,
                specs=[[{"type": "domain"}, {"type": "domain"}],
                    [{"type": "domain"}, {"type": "domain"}],
                    [{"type": "domain"}, {"type": "domain"}],
                    [{"type": "domain"}, {"type": "domain"}],
                    [{"type": "domain"}, {"type": "domain"}]]
    )
    df2 = df[['2-realRank', 'map_AdaRank_rerank']]
    # fig2 = px.parallel_coordinates(df2)

    df3 = df[['2-realRank', 'map_LambdaMART_rerank']]
    # fig3 = px.parallel_coordinates(df3)

    df4 = df[['2-realRank', 'map_LambdaRank_rerank']]
    # fig4 = px.parallel_coordinates(df4)

    df5 = df[['2-realRank', 'map_ListNet_rerank']]
    # fig5 = px.parallel_coordinates(df5)

    df6 = df[['2-realRank', 'map_MART_rerank']]
    # fig6 = px.parallel_coordinates(df6)

    df7 = df[['2-realRank', 'map_RankBoost_rerank']]
    # fig7 = px.parallel_coordinates(df7)

    df8 = df[['2-realRank', 'map_RankNet_rerank']]
    # fig8 = px.parallel_coordinates(df8)

    df9 = df[['2-realRank', 'map_coordinate_ascent_rerank']]
    # fig9 = px.parallel_coordinates(df9)

    df10 = df[['2-realRank', 'map_linear_regression_rerank']]
    # fig10 = px.parallel_coordinates(df10)

    df11 = df[['2-realRank', 'map_random_forest_rerank']]
    # fig11 = px.parallel_coordinates(df11)
    # 1
    #  left
    fig.add_trace(
        go.Parcoords(
            line_color='red',
            dimensions = list([
                dict(range = [1,50],
                    constraintrange = [15,35],
                    label = "Ground Truth", values = df2['2-realRank']),
                
                dict(range = [1,50],
                    label = 'Ada Rerank', values = df2['map_AdaRank_rerank'])
            ])
        ), 
        row=1,
        col=1
    ),
    # 2
    # Right
    fig.add_trace(
        go.Parcoords(
            line_color='yellow',
            dimensions = list([
                dict(range = [1,50],
                    constraintrange = [15,35],
                    label = "Ground Truth", values = df3['2-realRank']),
                
                dict(range = [1,50],
                    label = 'LambdaMART Rerank', values = df3['map_LambdaMART_rerank'])
            ])
        ), 
        row=1,
        col=2
    ),
    # 3
    #  left
    fig.add_trace(
        go.Parcoords(
            dimensions = list([
                dict(range = [1,50],
                    constraintrange = [15,35],
                    label = "Ground Truth", values = df4['2-realRank']),
                
                dict(range = [1,50],
                    label = 'LambdaRank Rerank', values = df4['map_LambdaRank_rerank'])
            ])
        ), 
        row=2,
        col=1
    ),
    # 4
    #  Right
    fig.add_trace(
        go.Parcoords(
            dimensions = list([
                dict(range = [1,50],
                    constraintrange = [15,35],
                    label = "Ground Truth", values = df5['2-realRank']),
                
                dict(range = [1,50],
                    label = 'ListNet Rerank', values = df5['map_ListNet_rerank'])
            ])
        ), 
        row=2,
        col=2
    ),
    # 5
    # Left
    fig.add_trace(
        go.Parcoords(
            dimensions = list([
                dict(range = [1,50],
                    constraintrange = [15,35],
                    label = "Ground Truth", values = df6['2-realRank']),
                
                dict(range = [1,50],
                    label = 'MART Rerank', values = df6['map_MART_rerank'])
            ])
        ), 
        row=3,
        col=1
    ),
    # 6
    #  Right
    fig.add_trace(
        go.Parcoords(
            dimensions = list([
                dict(range = [1,50],
                    constraintrange = [15,35],
                    label = "Ground Truth", values = df7['2-realRank']),
                
                dict(range = [1,50],
                    label = 'RankBoost Rerank', values = df7['map_RankBoost_rerank'])
            ])
        ), 
        row=3,
        col=2
    ),
    # 7
    #  left
    fig.add_trace(
        go.Parcoords(
            dimensions = list([
                dict(range = [1,50],
                    constraintrange = [15,35],
                    label = "Ground Truth", values = df8['2-realRank']),
                
                dict(range = [1,50],
                    label = 'RankNet Rerank', values = df8['map_RankNet_rerank'])
            ])
        ), 
        row=4,
        col=1
    ),
    # 8
    #  Right
    fig.add_trace(
        go.Parcoords(
            dimensions = list([
                dict(range = [1,50],
                    constraintrange = [15,35],
                    label = "Ground Truth", values = df9['2-realRank']),
                
                dict(range = [1,50],
                    label = 'coordinate_ascent Rerank', values = df9['map_coordinate_ascent_rerank'])
            ])
        ), 
        row=4,
        col=2
    ),
    # 9
    # Left
    fig.add_trace(
        go.Parcoords(
            dimensions = list([
                dict(range = [1,50],
                    constraintrange = [15,35],
                    label = "Ground Truth", values = df10['2-realRank']),
                
                dict(range = [1,50],
                    label = 'linear_regression Rerank', values = df10['map_linear_regression_rerank'])
            ])
        ),
        row=5,
        col=1
    ),
    # 10
    # Right
    fig.add_trace(
        go.Parcoords(
            dimensions = list([
                dict(range = [1,50],
                    constraintrange = [15,35],
                    label = "Ground Truth", values = df11['2-realRank']),
                
                dict(range = [1,50],
                    label = 'random_forest Rerank', values = df11['map_random_forest_rerank'])
            ])
        ), 
        row=5,
        col=2
    )
   
    fig.update_layout(autosize=False, height=1500)
    return [fig]

if __name__ == "__main__":
    app.run_server(debug=True)