import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash.exceptions import PreventUpdate
from readers import *
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import csv, os
from pathlib import Path
import plotly.express as px
import pandas as pd
from abs_path import return_abs_path, return_abs_path2

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.title = "Transparency Ranking"
app.layout = html.Div([
    html.H1(children="An effort to visualize model ranking", style={'textAlign': 'center'}),
    html.Hr(),
html.Div([
        html.H2("Across years"),
        html.Div(children="This task studies the re-ranking of states across different years ",
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
        html.H4("Visualization"),
        html.Div([
            dcc.Graph(
                id='Vis-1-1',
            )
        ]),
        html.Br(),
        html.Br(),
    ])

#Task callback for Task 1
@app.callback(
    [Output('Vis-1-1', 'figure')],
    [Input("drop-down-year-task1", "value")
    # ,
    #  Input("radio-option-task1", "value")
    ],
)
def update_graph(year, option):
    # if(option == "time_of_the_day"):
        filename = "/Users/ak/Documents/GitHub/Transparency-Ranking/finance datasets/all.csv"
        title = "Model re-ranking vs Original ranking for the selected year"
        df = pd.pd.read_csv(
            '/Users/ak/Documents/GitHub/Transparency-Ranking/finance datasets/all.csv')
        fig = make_subplots(rows=5, cols=2,
                    specs=[[{"type": "domain"}, {"type": "domain"}],
                        [{"type": "domain"}, {"type": "domain"}],
                        [{"type": "domain"}, {"type": "domain"}],
                        [{"type": "domain"}, {"type": "domain"}],
                        [{"type": "domain"}, {"type": "domain"}]]
        )
        # 1
        #  left
        fig.add_trace(
            go.Parcoords(
                dimensions = list([
                    dict(range = [1,50],
                        constraintrange = [15,35],
                        label = "Ground Truth", values = df['two_realRank']),
                    
                    dict(range = [1,50],
                        label = 'Ada Rerank', values = df['map_AdaRank_rerank'])
                ])
            ), 
            row=1,
            col=1
        ),
        # 2
        # Right
        fig.add_trace(
            go.Parcoords(
                dimensions = list([
                    dict(range = [1,50],
                        constraintrange = [15,35],
                        label = "Ground Truth", values = df['two_realRank2']),
                    
                    dict(range = [1,50],
                        label = 'LambdaMART Rerank', values = df['map_LambdaMART_rerank'])
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
                        label = "Ground Truth", values = df['two_realRank3']),
                    
                    dict(range = [1,50],
                        label = 'LambdaRank Rerank', values = df['map_LambdaRank_rerank'])
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
                        label = "Ground Truth", values = df['two_realRank4']),
                    
                    dict(range = [1,50],
                        label = 'ListNet Rerank', values = df['map_ListNet_rerank'])
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
                        label = "Ground Truth", values = df['two_realRank5']),
                    
                    dict(range = [1,50],
                        label = 'MART Rerank', values = df['map_MART_rerank'])
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
                        label = "Ground Truth", values = df['two_realRank6']),
                    
                    dict(range = [1,50],
                        label = 'RankBoost Rerank', values = df['map_RankBoost_rerank'])
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
                        label = "Ground Truth", values = df['two_realRank7']),
                    
                    dict(range = [1,50],
                        label = 'RankNet Rerank', values = df['map_RankNet_rerank'])
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
                        label = "Ground Truth", values = df['two_realRank8']),
                    
                    dict(range = [1,50],
                        label = 'coordinate_ascent Rerank', values = df['map_coordinate_ascent_rerank'])
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
                        label = "Ground Truth", values = df['two_realRank9']),
                    
                    dict(range = [1,50],
                        label = 'linear_regression Rerank', values = df['map_linear_regression_rerank'])
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
                        label = "Ground Truth", values = df['two_realRank10']),
                    
                    dict(range = [1,50],
                        label = 'random_forest Rerank', values = df['map_random_forest_rerank'])
                ])
            ), 
            row=5,
            col=2
        )
        fig.update_layout(
            autosize=False,
            width=1000,
            height=1500
            )
        fig.show()
        # fig1 = px.line(df, x='Time of the Day (in Hrs)', y='Power(kW)', color='Year',title=title)
        # fig1.update_xaxes(ticks="inside", dtick=1, title_font=dict(family='Georgia', color='black'),tickfont=dict(family='Georgia', color='black'))
        # fig1.update_yaxes(title_font=dict(family='Georgia', color='black'), tickfont=dict(family='Georgia', color='black'))
        # fig1.update_layout(font=dict(family="Georgia", color="black"))

        # return [fig1]
    # else:
    #     filename = "visualizations/task1_" + str(option) + "_" + str(year) + ".csv"
    #     #filename = "visualizations/task1_time_of_the_day" + "_" + str(year) + ".csv"
    #     title = "Average Power Consumption during different seasons " + "(" + str(year) + ")"
    #     df = pd.read_csv(filename, names=["Seasons", 'Power(kW)'])
    #     fig1 = px.bar(df, x='Seasons', y='Power(kW)',  title=title,text="Power(kW)")
    #     fig1.update_xaxes(ticks="inside", title_font=dict(family='Georgia', color='black'),tickfont=dict(family='Georgia', color='black'))
    #     fig1.update_yaxes(title_font=dict(family='Georgia', color='black'),tickfont=dict(family='Georgia', color='black'))
    #     fig1.update_layout(font=dict(family="Georgia", color="black"))

    #     return [fig1]


if __name__ == "__main__":
    app.run_server(debug=False)
