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

# app_options = {
#     "HomeA": ["FurnaceHRV [kW]", "Refrigerator [kW]", "KitchenDenLights [kW]", "DishwasherDisposalSinkLight [kW]",
#               "OfficeLights [kW]", "CellarOutlets [kW]", "Dryer [kW]", "BasementOutdoorOutlets [kW]"],
#     "HomeB": ["Grid [kW]", "AC [kW]", "Furnace [kW]", "Utility Rm + Basement Bath [kW]", "Home Office (R) [kW]",
#               "Home office [kW]", "Guest Bedroom / Media Room [kW]", "Fridge [kW]"],
#     "HomeC": ["LivingRoomOutlets [kW]", "House overall [kW]", "Furnace 1 [kW]", "Furnace 2 [kW]", "Home office [kW]",
#               "Fridge [kW]", "Wine cellar [kW]", "Living room [kW]"],
#     "HomeF": ["WaterHeater [kW]", "Refrigerator [kW]", "Furnace [kW]", "Family_Rm [kW]", "Dryer [kW]", "WaterHeater1 "
#                                                                                                        "[kW]",
#               "WaterHeater2 [kW]", "WaterHeater3 [kW]"],
#     "HomeD": ["HousePanel [kW]", "FreshAirVentilation [kW]", "LivingRoomReceptacles [kW]", "WashingMachine [kW]", "WorkshopReceptacleBathHeater [kW]", "Basement&amp;HallLighting [kW]", "GuestHouseBathroom [kW]", "GuestHouseBedroom [kW]"],
#     "HomeG": ["HVAC air handler [kW]", "Water pump [kW]", "Range oven [kW]", "Electronics closet [kW]", "Hot tub [kW]",
#               "Wall oven [kW]", "ERV + humidifier + fountain [kW]", "DL bedroom outlets [kW]"],
#     "HomeH": ["Kitchen Outlet/Espresso (32) [kW]", "Dishwasher (17) [kW]", "Kitchen (39) [kW]", "Oven (7+5) [kW]",
#               "Dryer (36+34) [kW]", "Basement/Dehumidifier (31) [kW]", "Dining Room (15) [kW]",
#               "1st Floor Bedroom (37) [kW]"]
# }
# year_options = {
#     "HomeA": ["2014", "2015", "2016"],
#     "HomeB": ["2014", "2015", "2016"],
#     "HomeC": ["2014", "2015", "2016"],
#     "HomeD": ["2015", "2016"],
#     "HomeF": ["2014", "2015", "2016"],
#     "HomeG": ["2015", "2016"],
#     "HomeH": ["2016"]
# }

# home_options_task3 = {
#     "2014":["HomeA","HomeB","HomeC","HomeF"],
#     "2015":["HomeA","HomeB","HomeC","HomeF"],
#     "2016":["HomeA","HomeB","HomeC","HomeD","HomeF"]

# }

# color_list = [
#     '#1f77b4',  # muted blue
#     '#ff7f0e',  # safety orange
#     '#2ca02c',  # cooked asparagus green
#     '#d62728',  # brick red
#     '#9467bd',  # muted purple
#     '#8c564b',  # chestnut brown
#     '#e377c2',  # raspberry yogurt pink
#     '#7f7f7f',  # middle gray
#     '#bcbd22',  # curry yellow-green
#     '#17becf'  # blue-teal
# ]
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
        # html.Div(children="Time Parameters:", style={'font-style': 'italic'}),
        # dcc.RadioItems(
        #     id="radio-option-task1",
        #     options=[
        #         {'label': 'Time of the day', 'value': 'time_of_the_day'},
        #         {'label': 'Seasons', 'value': 'seasons'}
        #     ],
        #     value="time_of_the_day"),
        # html.Br(),
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
#     ,
#     html.Div([
#         html.Hr(),
#         html.H2("Task2"),
#         html.Div(children="This task studies the power consumption of apartments across different weather parameters "
#                           "like temperature, humidity and weather summary. This study contains data of 114 apartments "
#                           "across three years (2014, 2015, 2016)", style={'font-style': 'normal'}),
#         html.Br(),
#         html.Div(children="Years:", style={'font-style': 'italic'}),
#         dcc.Dropdown(
#             id="drop-down-year-task2",
#             style={'color': '#000000', "width": "300px"},
#             options=[
#                 {'label': '2014', 'value': '2014'},
#                 {'label': '2015', 'value': '2015'},
#                 {'label': '2016', 'value': '2016'}],
#             value="2014"),
#         html.Br(),
#         html.Div(children="Weather Conditions:", style={'font-style': 'italic'}),
#         dcc.RadioItems(
#             id="radio-weather-task2",
#             options=[
#                 {'label': 'Temperature', 'value': 'temperature'},
#                 {'label': 'Humidity', 'value': 'humidity'},
#                 {'label': 'Weather Summary (snowy, rainy, clear ...)', 'value': 'summary'}
#             ],
#             value="temperature"),
#         html.Br(),
#         html.Hr(style={'border-style': 'dotted'}),
#         html.H4("Primary Visualization"),
#         html.Div([
#             dcc.Graph(
#                 id='Vis-2-1',
#             )
#         ]),
#         html.Br(),
#         html.H4("Alternative Visualization"),
#         html.Div([
#             dcc.Graph(
#                 id='Vis-2-2',
#             )
#         ]),
#         html.Br(),
#     ]),

#     html.Div([
#         html.Hr(),
#         html.H2("Task3"),
#         html.Div(children="This task studies the power consumption of different appliances across different time parameters. This study "
#                           "contains data of appliances like furnace, refrigerator etc., across three years (2014, "
#                           "2015, 2016)", style={'font-style': 'normal'}),
#         html.Br(),

#         html.Div(children="Years:", style={'font-style': 'italic'}),
#         dcc.Dropdown(
#             id="drop-down-year-task3",
#             style={'color': '#000000', 'width': '300px'},
#             options=[
#                 {'label': '2014', 'value': '2014'},
#                 {'label': '2015', 'value': '2015'},
#                 {'label': '2016', 'value': '2016'}],
#             value="2016"
#         ),
#         html.Div(children="Homes:", style={'font-style': 'italic'}),
#         dcc.Dropdown(
#             id="drop-down-homes-task3",
#             style={'color': '#000000', 'width': '300px'},
#             value='HomeA',
#             options=[
#                 {'label': 'Home A', 'value': 'HomeA'},
#                 {'label': 'Home B', 'value': 'HomeB'},
#                 {'label': 'Home C', 'value': 'HomeC'},
#                 {'label': 'Home F', 'value': 'HomeF'},
#                 {'label': 'Home G', 'value': 'HomeG'},
#                 {'label': 'Home H', 'value': 'HomeH'}
#             ]
#         ),
#         html.Br(),
#         html.Hr(style={'border-style': 'dotted'}),
#         html.H4("Visualization"),
#         html.Div([
#             dcc.Graph(
#                 id='Vis-3-1',
#             )
#         ])
#     ]),
#     html.Div([
#         html.Hr(),
#         html.H2("Task4"),
#         html.Div(children="This task studies the power consumption of different appliances across 7 homes. This study "
#                           "contains data of appliances like furnace, refrigerator etc., across three years (2014, "
#                           "2015, 2016)", style={'font-style': 'normal'}),
#         html.Br(),

#         html.Div(children="Years:", style={'font-style': 'italic'}),
#         dcc.Dropdown(
#             id="drop-down-year",
#             style={'color': '#000000', 'width': '300px'},
#             value="2016"
#         ),
#         html.Div(children="Appliances:", style={'font-style': 'italic'}),
#         dcc.Dropdown(
#             id="drop-down-apps",
#             style={'color': '#000000', 'width': '1200px'},
#             multi=True,
#         ),
#         html.Div(children="Homes:", style={'font-style': 'italic'}),
#         dcc.Dropdown(
#             id="drop-down-homes",
#             style={'color': '#000000', 'width': '300px'},
#             value='HomeA',
#             options=[
#                 {'label': 'Home A', 'value': 'HomeA'},
#                 {'label': 'Home B', 'value': 'HomeB'},
#                 {'label': 'Home C', 'value': 'HomeC'},
#                 {'label': 'Home D', 'value': 'HomeD'},
#                 {'label': 'Home F', 'value': 'HomeF'},
#                 {'label': 'Home G', 'value': 'HomeG'},
#                 {'label': 'Home H', 'value': 'HomeH'}
#             ]
#         ),
#         html.Div(children="Weather Conditions:", style={'font-style': 'italic'}),
#         dcc.RadioItems(
#             id="radio-weather",
#             options=[
#                 {'label': 'Temperature', 'value': 'temperature'},
#                 {'label': 'Pressure', 'value': 'pressure'},
#                 {'label': 'WindSpeed', 'value': 'windSpeed'}
#             ],
#             value="temperature"
#         ),
#         html.Br(),
#         html.Hr(style={'border-style': 'dotted'}),
#         html.H4("Primary Visualization"),
#         html.Div([
#             dcc.Graph(
#                 id='Vis-1',
#             ),
#             html.Br(),
#             html.H4("Alternative Visualization"),
#             dcc.Graph(
#                 id='Vis-2',
#             )
#         ])
#     ])
# ])


# @app.callback(
#     [Output("drop-down-year", "options"),
#      Output("drop-down-apps", "options")],
#     [Input("drop-down-homes", "value")])
# def update_comps(home_name):
#     return [{'label': i, 'value': i} for i in year_options[home_name]], [{'label': i, 'value': i} for i in
#                                                                          app_options[home_name]]
# #Options callback for task 3
# @app.callback(
#     [Output("drop-down-homes-task3", "options")],
#     [Input("drop-down-year-task3", "value")])
# def update_comps(year):
#     return [[{'label': i, 'value': i} for i in home_options_task3[year]]]

# # Task callback for Task 4
# @app.callback(
#     [Output('Vis-1', 'figure'),
#      Output("Vis-2", "figure")],
#     [Input("drop-down-homes", "value"),
#      Input("drop-down-year", "value"),
#      Input("drop-down-apps", "value"),
#      Input("radio-weather", "value")],
# )
# def update_graph(home_name, year, apps, weather):
#     df = merger(home_name, year)

#     df["Temperature range"] = df["temperature"].apply(roundup_v1)
#     df["Temperature range"] = [("(" + str(row - 10) + "," + str(row) + ")") for row in df["Temperature range"]]

#     df["Pressure range"] = df["pressure"].apply(roundup_v1)
#     df["Pressure range"] = [("(" + str(row - 10) + "," + str(row) + ")") for row in df["Pressure range"]]

#     df["windSpeed range"] = df["windSpeed"].apply(roundup_v2)
#     df["windSpeed range"] = [("(" + str(row - 1) + "," + str(row) + ")") for row in df["windSpeed range"]]

#     fig_1 = make_subplots(specs=[[{"secondary_y": True}]])
#     fig_2 = make_subplots(rows=1, cols=3, y_title="Power Consumption [kW]")

#     color_count = 0
#     fig_1.add_trace(
#         go.Scatter(x=df["Date"],
#                    y=df[weather],
#                    name=weather,
#                    line=dict(color="black", width=0.5)),
#         secondary_y=True
#     )
#     if apps is None:
#         raise PreventUpdate
#     else:
#         for app in apps:
#             fig_1.add_trace(
#                 go.Scatter(x=df["Date"],
#                            y=df[app],
#                            name=app,
#                            line=dict(color=color_list[color_count], width=1)),
#                 secondary_y=False
#             )
#             fig_2.add_trace(
#                 go.Scatter(
#                     x=df["Temperature range"].sort_values(ascending=True),
#                     y=df[app],
#                     name=app,
#                     mode='markers',
#                     marker_color=color_list[color_count],
#                     opacity=0.5
#                 ), row=1, col=1,
#             )
#             fig_2.add_trace(
#                 go.Scatter(
#                     x=df["Pressure range"].sort_values(ascending=True),
#                     y=df[app],
#                     name=app,
#                     mode='markers',
#                     marker_color=color_list[color_count],
#                     opacity=0.5,
#                     showlegend=False
#                 ), row=1, col=2
#             )
#             fig_2.add_trace(
#                 go.Scatter(
#                     x=df["windSpeed range"].sort_values(ascending=True),
#                     y=df[app],
#                     name=app,
#                     mode='markers',
#                     marker_color=color_list[color_count],
#                     opacity=0.5,
#                     showlegend=False
#                 ), row=1, col=3
#             )
#             color_count += 1

#     fig_1.update_layout(title='Appliance Power Consumption of ' + home_name + ' ' + year)
#     fig_1.update_xaxes(title_text="Months", nticks=6)
#     fig_1.update_yaxes(title_text=weather, secondary_y=True)
#     fig_1.update_yaxes(title_text="Power Consumption", secondary_y=False)
#     fig_2.update_xaxes(title_text="Temperature (C)", row=1, col=1)
#     fig_2.update_xaxes(title_text="Pressure(mBar)", row=1, col=2)
#     fig_2.update_xaxes(title_text="WindSpeed(kmph)", row=1, col=3)
#     fig_2.update_layout(title='Appliance Power Consumption of ' + home_name + ' ' + year)

#     return fig_1, fig_2

# # Task callback for Task 2
# @app.callback(
#     [Output('Vis-2-1', 'figure'),
#      Output("Vis-2-2", "figure")],
#     [Input("drop-down-year-task2", "value"),
#      Input("radio-weather-task2", "value")],
# )
# def update_graph(year, weather):
#     if (weather == "summary"):
#         filename = "visualizations/task2_" + str(weather) + "_" + str(year) + "_bar.csv"
#         title = "Mean Power Consumption across different weather " + str(weather) + "(" + str(year) + ")"
#         xaxis_title_dict = {"summary": "Weather Summary"}  # used in both visualizations
#         df = pd.read_csv(filename, names=[str(weather), 'power'])
#         fig1 = px.bar(df, x=str(weather), y='power', title=title, text='power')
#         fig1.update_xaxes(ticks="inside", title_font=dict(family='Georgia', color='black'),
#                           tickfont=dict(family='Georgia', color='black'))
#         fig1.update_yaxes(title_font=dict(family='Georgia', color='black'),
#                           tickfont=dict(family='Georgia', color='black'))
#         fig1.update_layout(font=dict(family="Georgia", color="black"), xaxis_title=xaxis_title_dict[str(weather)],
#                            yaxis_title="Power(kW)")

#         filename = "visualizations/task2_" + str(weather) + "_" + str(year) + "_box.csv"
#         title = "Power Consumption across different " + str(weather) + " (Box-Plot)(" + str(year) + ")"
#         df = pd.read_csv(filename, names=[str(weather), 'power'])
#         fig2 = px.box(df, x=str(weather), y='power', points="all", title=title)
#         fig2.update_xaxes(ticks="inside", title_font=dict(family='Georgia', color='black'),
#                           tickfont=dict(family='Georgia', color='black'))
#         fig2.update_yaxes(title_font=dict(family='Georgia', color='black'),
#                           tickfont=dict(family='Georgia', color='black'))
#         fig2.update_layout(font=dict(family="Georgia", color="black"), xaxis_title=xaxis_title_dict[str(weather)],
#                            yaxis_title="Power(kW)")

#         return [fig1, fig2]
#     else:
#         filename = "visualizations/task2_" + str(weather) + "_" + str(year) + "_line.csv"
#         title = "Mean Power Consumption across different " + str(weather) + "(" + str(year) + ")"
#         xaxis_title_dict = {"temperature": "Temperature(in F)",
#                             "humidity": "Humidity(g/m3)"}  # used in both visualizations
#         df = pd.read_csv(filename, names=[str(weather), 'power'])
#         fig1 = px.line(df, x=str(weather), y='power', title=title)
#         fig1.update_xaxes(ticks="inside", title_font=dict(family='Georgia', color='black'),
#                           tickfont=dict(family='Georgia', color='black'))
#         fig1.update_yaxes(title_font=dict(family='Georgia', color='black'),
#                           tickfont=dict(family='Georgia', color='black'))
#         fig1.update_layout(font=dict(family="Georgia", color="black"), xaxis_title=xaxis_title_dict[str(weather)],
#                            yaxis_title="Power(kW)")

#         filename = "visualizations/task2_" + str(weather) + "_" + str(year) + "_box.csv"
#         title = "Power Consumption across different " + str(weather) + " (Box-Plot)(" + str(year) + ")"
#         xaxis_tick_dict = {"temperature": dict(tickmode='array', tickvals=[0, 10, 20, 30, 40, 50, 60, 70, 80, 90],
#                                                ticktext=['(-10 to 0)', '(0 to 10)', '(10 to 20)', '(20 to 30)',
#                                                          '(30 to 40)', '(40 to 50)', '(50 to 60)', '(60 to 70)',
#                                                          '(70 to 80)', '(80 to 90)', '(90 to 100)']),
#                            "humidity": dict(tickmode='array',
#                                             tickvals=[0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
#                                             ticktext=['(-0.1 to 0)', '(0 to 0.1)', '(0.1 to 0.2)', '(0.2 to 0.3)',
#                                                       '(0.3 to 0.4)', '(0.4 to 0.5)', '(0.5 to 0.6)', '(0.6 to 0.7)',
#                                                       '(0.7 to 0.8)', '(0.8 to 0.9)', '(0.9 to 1)'])}
#         df = pd.read_csv(filename, names=[str(weather), 'power'])
#         fig2 = px.box(df, x=str(weather), y='power', title=title)
#         fig2.update_xaxes(ticks="inside", dtick=1, title_font=dict(family='Georgia', color='black'),
#                           tickfont=dict(family='Georgia', color='black'))
#         fig2.update_yaxes(title_font=dict(family='Georgia', color='black'),
#                           tickfont=dict(family='Georgia', color='black'))
#         fig2.update_layout(font=dict(family="Georgia", color="black"), xaxis_title=xaxis_title_dict[str(weather)],
#                            yaxis_title="Power(kW)", xaxis=xaxis_tick_dict[str(weather)])

#         return [fig1, fig2]

# #Task callback for Task 3
# @app.callback(
#     [Output('Vis-3-1', 'figure')],
#     [Input("drop-down-year-task3", "value"),
#      Input("drop-down-homes-task3", "value")],
# )
# def update_graph(year, home):
#     filename = "visualizations/Task3_" + str(home) + "_" + str(year) + ".csv"
#     title = "Total Power Consumption across different appliances in  " + str(home) + "(" + str(year) + ")"
#     df = pd.read_csv(filename, names=["Appliance", 'Power'])
#     fig1 = px.bar(df, x="Appliance", y='Power', title=title, text="Power")
#     fig1.update_xaxes(ticks="inside", title_font=dict(family='Georgia', color='black'),tickfont=dict(family='Georgia', color='black'))
#     fig1.update_yaxes(title_font=dict(family='Georgia', color='black'),tickfont=dict(family='Georgia', color='black'))
#     fig1.update_layout(font=dict(family="Georgia", color="black"), xaxis_title="Appliances",yaxis_title="Power(kW)")
#     '''
#     fig2 = px.scatter(df, x="Appliance", y='Power', title=title)
#     fig2.update_xaxes(ticks="inside", title_font=dict(family='Georgia', color='black'),tickfont=dict(family='Georgia', color='black'))
#     fig2.update_yaxes(title_font=dict(family='Georgia', color='black'), tickfont=dict(family='Georgia', color='black'))
#     fig2.update_layout(font=dict(family="Georgia", color="black"), xaxis_title="Appliances", yaxis_title="Power(kW)")
#     '''
#     return [fig1]


#Task callback for Task 1
@app.callback(
    [Output('Vis-1-1', 'figure')],
    [Input("drop-down-year-task1", "value"),
     Input("radio-option-task1", "value")],
)
def update_graph(year, option):
    if(option == "time_of_the_day"):
        filename = "visualizations/task1_" + str(option) + "_" + str(year) + ".csv"
        title = "Cumulative Power Consumption during different time of the day " + "(" + str(year) + ")"
        df = pd.read_csv(filename, names=["Time of the Day (in Hrs)", 'Power(kW)', 'Year'])
        fig1 = px.line(df, x='Time of the Day (in Hrs)', y='Power(kW)', color='Year',title=title)
        fig1.update_xaxes(ticks="inside", dtick=1, title_font=dict(family='Georgia', color='black'),tickfont=dict(family='Georgia', color='black'))
        fig1.update_yaxes(title_font=dict(family='Georgia', color='black'), tickfont=dict(family='Georgia', color='black'))
        fig1.update_layout(font=dict(family="Georgia", color="black"))

        return [fig1]
    else:
        filename = "visualizations/task1_" + str(option) + "_" + str(year) + ".csv"
        #filename = "visualizations/task1_time_of_the_day" + "_" + str(year) + ".csv"
        title = "Average Power Consumption during different seasons " + "(" + str(year) + ")"
        df = pd.read_csv(filename, names=["Seasons", 'Power(kW)'])
        fig1 = px.bar(df, x='Seasons', y='Power(kW)',  title=title,text="Power(kW)")
        fig1.update_xaxes(ticks="inside", title_font=dict(family='Georgia', color='black'),tickfont=dict(family='Georgia', color='black'))
        fig1.update_yaxes(title_font=dict(family='Georgia', color='black'),tickfont=dict(family='Georgia', color='black'))
        fig1.update_layout(font=dict(family="Georgia", color="black"))

        return [fig1]


if __name__ == "__main__":
    app.run_server(debug=False)
