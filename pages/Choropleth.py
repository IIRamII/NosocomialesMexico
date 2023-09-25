import pandas as pd
import dash
from dash import Dash, html, dcc, dash_table, Input, Output, callback
import plotly.express as px
import requests


##Set de datos de México
# Abrir archivo de datos
d_m = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/MEXICO.csv")
# Obtener geojson que funciona como el mapa
url_mx = 'https://raw.githubusercontent.com/angelnmara/geojson/master/mexicoHigh.json'
mx_region = requests.get(url_mx).json()

# Mapa de México
f_mx = px.choropleth(data_frame=d_m, geojson=mx_region, locations='Estado', featureidkey='properties.name',
                     hover_name="Estado", hover_data=["Casos", "Defunciones"],
                     color='Casos', color_continuous_scale="Darkmint")
f_mx.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")

# MAPA NUEVO LEON
#with open('municipal.json', 'r', encoding='utf-8') as f:
#    NLMap = json.load(f)

NLMap = requests.get("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/municipal.json").json()


d_NL = pd.read_csv("https://raw.githubusercontent.com/IIRamII/NosocomialesMexico/main/data/NUEVOLEON.csv")

f_NL = px.choropleth(data_frame=d_NL, geojson=NLMap, locations='Municipio', featureidkey='properties.NOMBRE',
                     hover_name="Municipio", hover_data=["Casos", "Defunciones"],
                     color='Casos', color_continuous_scale="Darkmint")
f_NL.update_geos(showcountries=True, showcoastlines=True, showland=True, fitbounds="locations")

dash.register_page(__name__)

layout = html.Div(children=[
    html.H1("Mapa Choropleth de México", style={'textAlign': 'center'}),

    html.Div(children=[
        html.H2(children="Casos por Estado", style={'textAlign': 'center'}),
        dcc.Graph(
            id="mapaMexico",
            figure=f_mx),
    ]),

    html.Div(children=[
        html.H2(children="Estado de Nuevo León", style={'textAlign': 'center'}),
        dcc.Graph(
            id="mapaNL",
            figure=f_NL)
    ])
])