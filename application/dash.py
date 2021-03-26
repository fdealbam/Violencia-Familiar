import dash
import matplotlib.pyplot as plt 
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import dash_table
import sidetable as stb
import datetime
from datetime import datetime, timedelta
from datetime import date
import geopandas as gpd
import flask
import os

yesterday = datetime.now() - timedelta(1)
yea = datetime.strftime(yesterday, '%Y%m%d')

today = date.today()
d2 = today.strftime("Fecha de actualización : %d-%m-%Y")



###############################
# DATABASES
############################### Abre archivos


#os.chdir(r"C:\Users\PRIME\AnacondaProjects\Project_curso\\")

delitos = pd.read_csv("https://github.com/fdealbam/Violencia-Familiar/blob/main/ViolenciaFamiliar2015_2021.csv?raw=true")
delitos.drop('Unnamed: 0',1, inplace=True)

delitos.groupby(['Año','Entidad','Tipo de delito'])['Enero', 
                 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
       'Julio', 'Agosto', 'Septiembre', 'Octubre',
       'Noviembre', 'Diciembre'].sum().to_csv("00.csv",  header=True)

fem= pd.read_csv("00.csv")

############################################### separación de años

year15= fem[fem.Año == 2015]
year16= fem[fem.Año == 2016]
year17= fem[fem.Año == 2017]
year18= fem[fem.Año == 2018]
year19= fem[fem.Año == 2019]
year20= fem[fem.Año == 2020]
year21= fem[fem.Año == 2021]

############################################### Agregar suffix de años

y15 = year15.add_suffix('15')
y15.rename(columns ={'Año15': 'Año', 'Tipo de delito15': 'Tipo de delito', 'Unnamed: 015' : 'Unnamed: 0',
                            'Entidad15': 'Entidad'}, inplace = True)

y16 = year16.add_suffix('16')
y16.rename(columns ={'Año16': 'Año', 'Tipo de delito16': 'Tipo de delito', 'Unnamed: 016' : 'Unnamed: 0',
                            'Entidad16': 'Entidad'}, inplace = True)

y17 = year17.add_suffix('17')
y17.rename(columns ={'Año17': 'Año', 'Tipo de delito17': 'Tipo de delito', 'Unnamed: 017' : 'Unnamed: 0',
                            'Entidad17': 'Entidad'}, inplace = True)

y18= year18.add_suffix('18')
y18.rename(columns ={'Año18': 'Año', 'Tipo de delito18': 'Tipo de delito','Unnamed: 018' : 'Unnamed: 0',
                            'Entidad18': 'Entidad'}, inplace = True)

y19= year19.add_suffix('19')
y19.rename(columns ={'Año19': 'Año', 'Tipo de delito19': 'Tipo de delito', 'Unnamed: 019' : 'Unnamed: 0',
                            'Entidad19': 'Entidad'}, inplace = True)

y20= year20.add_suffix('20')
y20.rename(columns ={'Año20': 'Año', 'Tipo de delito20': 'Tipo de delito','Unnamed: 020' : 'Unnamed: 0',
                            'Entidad20': 'Entidad'}, inplace = True)

y21= year21.add_suffix('21')
y21.rename(columns ={'Año21': 'Año', 'Tipo de delito21': 'Tipo de delito','Unnamed: 021' : 'Unnamed: 0',
                            'Entidad21': 'Entidad'}, inplace = True)



############################################### Concat todos los años

fa = y15.merge(y16, on="Entidad",  how="inner")
fb = fa.merge(y17, on="Entidad",  how="inner")
fc = fb.merge(y18, on="Entidad",  how="inner")
fd = fc.merge(y19, on="Entidad",  how="inner")
fe = fd.merge(y20, on="Entidad",  how="inner")
ff = fe.merge(y21, on="Entidad",  how="inner")
                    
femi15_21 = ff[[
 'Entidad','Enero15','Febrero15','Marzo15','Abril15','Mayo15','Junio15',
 'Julio15','Agosto15','Septiembre15','Octubre15','Noviembre15','Diciembre15',
 
 'Enero16','Febrero16','Marzo16','Abril16','Mayo16','Junio16','Julio16',
 'Agosto16','Septiembre16','Octubre16','Noviembre16','Diciembre16',

 'Enero17','Febrero17','Marzo17','Abril17','Mayo17','Junio17','Julio17',
 'Agosto17','Septiembre17','Octubre17','Noviembre17','Diciembre17',
    
 'Enero18','Febrero18','Marzo18','Abril18','Mayo18','Junio18','Julio18',
 'Agosto18','Septiembre18','Octubre18','Noviembre18','Diciembre18',
 
 'Enero19','Febrero19','Marzo19','Abril19','Mayo19','Junio19','Julio19',
 'Agosto19','Septiembre19','Octubre19','Noviembre19','Diciembre19',

 'Enero20','Febrero20','Marzo20','Abril20','Mayo20','Junio20','Julio20',
 'Agosto20','Septiembre20','Octubre20','Noviembre20','Diciembre20',
    
 'Enero21','Febrero21'#,'Marzo21','Abril21','Mayo21','Junio21','Julio21',
# 'Agosto21','Septiembre21','Octubre21','Noviembre21','Diciembre21'
             ]]



##CRear columna de TOTAL ANUAL 
femi15_21['Total2015']= femi15_21[[ 'Enero15', 'Febrero15', 'Marzo15', 'Abril15', 'Mayo15',
                               'Junio15', 'Julio15', 'Agosto15', 'Septiembre15', 'Octubre15',
                               'Noviembre15', 'Diciembre15',]].sum(axis=1)
femi15_21['Total2016']= femi15_21[[ 'Enero16', 'Febrero16', 'Marzo16', 'Abril16', 'Mayo16',
                               'Junio16', 'Julio16', 'Agosto16', 'Septiembre16', 'Octubre16',
                               'Noviembre16', 'Diciembre16',]].sum(axis=1)
femi15_21['Total2017']= femi15_21[[ 'Enero17', 'Febrero17', 'Marzo17', 'Abril17', 'Mayo17',
                               'Junio17', 'Julio17', 'Agosto17', 'Septiembre17', 'Octubre17',
                               'Noviembre17', 'Diciembre17',]].sum(axis=1)
femi15_21['Total2018']= femi15_21[[ 'Enero18', 'Febrero18', 'Marzo18', 'Abril18', 'Mayo18',
                               'Junio18', 'Julio18', 'Agosto18', 'Septiembre18', 'Octubre18',
                               'Noviembre18', 'Diciembre18',]].sum(axis=1)
femi15_21['Total2019']= femi15_21[[ 'Enero19', 'Febrero19', 'Marzo19', 'Abril19', 'Mayo19',
                               'Junio19', 'Julio19', 'Agosto19', 'Septiembre19', 'Octubre19',
                               'Noviembre19', 'Diciembre19',]].sum(axis=1)
femi15_21['Total2020']= femi15_21[[ 'Enero20', 'Febrero20', 'Marzo20', 'Abril20', 'Mayo20',
                               'Junio20', 'Julio20', 'Agosto20', 'Septiembre20', 'Octubre20',
                               'Noviembre20', 'Diciembre20',]].sum(axis=1)

femi15_21['Total2021']= femi15_21[[ 'Enero21','Febrero21'#, 'Marzo21', 'Abril21', 'Mayo21',
                                   #'Junio21','Julio21','Agosto21','Septiembre21','Octubre21',
                                   #'Noviembre21','Diciembre21'
                                  ]].sum(axis=1)


#identificadores
conf_2015= femi15_21.Total2015.sum()
conf_2016= femi15_21.Total2016.sum()
conf_2017= femi15_21.Total2017.sum()
conf_2018= femi15_21.Total2018.sum()
conf_2019= femi15_21.Total2019.sum()
conf_2020= femi15_21.Total2020.sum()
conf_2021= femi15_21.Total2021.sum()



################################################## PREPARA GRAFICA MENSUAL
pagra = ff[[
  'Enero15', 'Febrero15', 'Marzo15', 'Abril15', 'Mayo15', 'Junio15', 'Julio15', 'Agosto15', 
    'Septiembre15', 'Octubre15', 'Noviembre15', 'Diciembre15',
 
 'Enero16', 'Febrero16', 'Marzo16', 'Abril16', 'Mayo16', 'Junio16', 'Julio16', 'Agosto16', 
    'Septiembre16', 'Octubre16', 'Noviembre16', 'Diciembre16',

 'Enero17', 'Febrero17', 'Marzo17', 'Abril17', 'Mayo17', 'Junio17', 'Julio17', 'Agosto17', 
    'Septiembre17', 'Octubre17', 'Noviembre17', 'Diciembre17', 
    'Enero18', 'Febrero18', 'Marzo18',    'Abril18', 'Mayo18', 'Junio18', 'Julio18', 'Agosto18',
    'Septiembre18', 'Octubre18', 'Noviembre18', 'Diciembre18',
 
 'Enero19', 'Febrero19', 'Marzo19', 'Abril19', 'Mayo19', 'Junio19', 'Julio19', 'Agosto19', 
    'Septiembre19', 'Octubre19', 'Noviembre19', 'Diciembre19',

 'Enero20', 'Febrero20', 'Marzo20', 'Abril20', 'Mayo20', 'Junio20', 'Julio20', 'Agosto20',
    'Septiembre20','Octubre20', 'Noviembre20', 'Diciembre20',

 'Enero21', 'Febrero21'#, 'Marzo21', 'Abril21', 'Mayo21', 'Junio21', 'Julio21', 'Agosto21',
  #  'Septiembre21','Octubre21','Noviembre21','Diciembre21'
            ]]


pagrafm = pagra.stb.subtotal()
pagrafm.to_csv("0000procesod.csv")
#Selecciona ultima columna (Totales)
other  = pd.read_csv('0000procesod.csv')
other_s = other.iloc[32]
other_b = pd.DataFrame(other_s)
other_b.to_csv('0000procesodi.csv')
vuelve_a_abrir = pd.read_csv('0000procesodi.csv')
##Elimina filas 0 a 4 
gra_mes = vuelve_a_abrir.drop([0])
#Renombra titulo de columna
gra_mes = gra_mes.rename(columns= {"Unnamed: 0": "Mes"})
gra_mes = gra_mes.rename(columns= {"32": "Total"})
gra_mes['Total'] = pd.to_numeric(gra_mes['Total'])


#Grafica mensual 
graf_meses = go.Figure()
graf_meses.add_trace(go.Bar(x=gra_mes['Mes'],y=gra_mes['Total'],
                marker_color='indianred'  # cambiar nuemeritos de rgb
                ))
graf_meses.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 12,
    yaxis=dict(
        title='Acumulados mensuales',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    #autosize=False,
    #width=1000,
    #height=400
    )





#- FILE JSON PARA ENTIDADES ------------------------------------------------------------------------------



################################################ SUMA TODOS LOS AÑOS ranking de municipios por estado (3edos)

#filtro de feminicidio
delitos.groupby(['Municipio','Entidad',])['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo',
                                             'Junio','Julio', 'Agosto', 'Septiembre', 'Octubre',
                                             'Noviembre', 'Diciembre'].sum().to_csv('0000procesofem.csv')

fem_filter1=pd.read_csv('0000procesofem.csv')
fem_filter1[['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
                                 'Septiembre','Octubre','Noviembre','Diciembre']] = fem_filter1[['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
                                 'Septiembre','Octubre','Noviembre','Diciembre']].astype(int)
    
fem_filter1['Total']=fem_filter1[['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto',
                                 'Septiembre','Octubre','Noviembre','Diciembre']].sum(1)




#- FILE MUNICIPIOS ------------------------------------------------------------------------------

fem_filter1.fillna(0, inplace=True) 
fem_filter1['Total']=fem_filter1['Total'].astype(int)


############################################### filtro para estados(4) e identifiación de mpios y abs feminicidios

# estado 1
estado1=fem_filter1[fem_filter1.Entidad=='Ciudad de México']
edo1orden=estado1[['Municipio','Total']].sort_values('Total',ascending=False)
#1
edo1mpio1=edo1orden.iloc[0]['Municipio']
edo1mpio1v=edo1orden.iloc[0]['Total']
#2
edo1mpio2=edo1orden.iloc[1]['Municipio']
edo1mpio2v=edo1orden.iloc[1]['Total']
#3
edo1mpio3=edo1orden.iloc[2]['Municipio']
edo1mpio3v=edo1orden.iloc[2]['Total']
#4
edo1mpio4=edo1orden.iloc[3]['Municipio']
edo1mpio4v=edo1orden.iloc[3]['Total']
#5
edo1mpio5=edo1orden.iloc[4]['Municipio']
edo1mpio5v=edo1orden.iloc[4]['Total']


# estado 2
estado2=fem_filter1[fem_filter1.Entidad=='Nuevo León']
edo2orden=estado2[['Municipio','Total']].sort_values('Total',ascending=False)
#1
edo2mpio1=edo2orden.iloc[0]['Municipio']
edo2mpio1v=edo2orden.iloc[0]['Total']
#2
edo2mpio2=edo2orden.iloc[1]['Municipio']
edo2mpio2v=edo2orden.iloc[1]['Total']
#3
edo2mpio3=edo2orden.iloc[2]['Municipio']
edo2mpio3v=edo2orden.iloc[2]['Total']
#4
edo2mpio4=edo2orden.iloc[3]['Municipio']
edo2mpio4v=edo2orden.iloc[3]['Total']
#5
edo2mpio5=edo2orden.iloc[4]['Municipio']
edo2mpio5v=edo2orden.iloc[4]['Total']


# estado 3
estado3=fem_filter1[fem_filter1.Entidad=='Chihuahua']
edo3orden=estado3[['Municipio','Total']].sort_values('Total',ascending=False)
#1
edo3mpio1=edo3orden.iloc[0]['Municipio']
edo3mpio1v=edo3orden.iloc[0]['Total']
#2
edo3mpio2=edo3orden.iloc[1]['Municipio']
edo3mpio2v=edo3orden.iloc[1]['Total']
#3
edo3mpio3=edo3orden.iloc[2]['Municipio']
edo3mpio3v=edo3orden.iloc[2]['Total']
#4
edo3mpio4=edo3orden.iloc[3]['Municipio']
edo3mpio4v=edo3orden.iloc[3]['Total']
#5
edo3mpio5=edo3orden.iloc[4]['Municipio']
edo3mpio5v=edo3orden.iloc[4]['Total']


# estado 4
estado4=fem_filter1[fem_filter1.Entidad=='Guanajuato']
edo4orden=estado4[['Municipio','Total']].sort_values('Total',ascending=False)
#1
edo4mpio1=edo4orden.iloc[0]['Municipio']
edo4mpio1v=edo4orden.iloc[0]['Total']
#2
edo4mpio2=edo4orden.iloc[1]['Municipio']
edo4mpio2v=edo4orden.iloc[1]['Total']
#3
edo4mpio3=edo4orden.iloc[2]['Municipio']
edo4mpio3v=edo4orden.iloc[2]['Total']
#4
edo4mpio4=edo4orden.iloc[3]['Municipio']
edo4mpio4v=edo4orden.iloc[3]['Total']
#5
edo4mpio5=edo4orden.iloc[4]['Municipio']
edo4mpio5v=edo4orden.iloc[4]['Total']



######################################################### tablas Ranking municipios
# tabla 1
patabla1 = {'Mpio' : [edo1mpio1,edo1mpio2,edo1mpio3,edo1mpio4,edo1mpio5],
            'Casos': [edo1mpio1v,edo1mpio2v,edo1mpio3v,edo1mpio4v,edo1mpio5v],}

patabla1a = pd.DataFrame (patabla1, columns = ['Mpio','Casos'])


############## tabla 2
patabla2 = {'Mpio'  : [edo2mpio1,edo2mpio2,edo2mpio3,edo2mpio4,edo2mpio5],
            'Casos' : [edo2mpio1v,edo2mpio2v,edo2mpio3v,edo2mpio4v,edo2mpio5v],}

patabla2a = pd.DataFrame (patabla2, columns = ['Mpio','Casos'])


############## tabla 3
patabla3 = {'Mpio'  : [edo3mpio1,edo3mpio2,edo3mpio3,edo3mpio4,edo3mpio5],
            'Casos' : [edo3mpio1v,edo3mpio2v,edo3mpio3v,edo3mpio4v,edo3mpio5v],}

patabla3a = pd.DataFrame (patabla3, columns = ['Mpio','Casos'])


############## tabla 4
patabla4 = {'Mpio'  : [edo4mpio1,edo4mpio2,edo4mpio3,edo4mpio4,edo4mpio5],
            'Casos' : [edo4mpio1v,edo4mpio2v,edo4mpio3v,edo4mpio4v,edo4mpio5v],}

patabla4a = pd.DataFrame (patabla4, columns = ['Mpio','Casos'])




######################################################### Graf. Tasas de feminicidios por entidad 2015-2020

junto1 = pd.read_csv('https://raw.githubusercontent.com/fdealbam/feminicidios/main/application/POB_15_21.csv')
fem15_21 = femi15_21[['Entidad', 'Total2015', 'Total2016', 'Total2017',
       'Total2018', 'Total2019', 'Total2020', 'Total2021']]

junto15_21 = fem15_21.merge(junto1,right_on='NOM_ENT',left_on='Entidad')
junto15_21["Entidad"].replace('Veracruz de Ignacio de la Llave','Veracruz' , inplace=True)

junto15_21['Totfem1521']=junto15_21[['Total2015', 'Total2016', 'Total2017', 'Total2018','Total2019', 'Total2020', 'Total2021']].sum(1)
junto15_21['Totpob1521']=junto15_21[['POB15', 'POB16', 'POB17', 'POB18','POB19', 'POB20', 'POB21']].sum(1)
junto15_21['Tasa1521']=((junto15_21.Totfem1521/junto15_21.Totpob1521)*100000).round(2)



######################################################### Grafica tasa POR ENTIDAD
TasasFem15_21index=junto15_21[['Entidad','Totfem1521','Totpob1521','Tasa1521']].sort_values('Tasa1521',ascending=False)

graf_tasafem = go.Figure()
graf_tasafem.add_trace(go.Bar(x=TasasFem15_21index['Entidad'],y=TasasFem15_21index['Tasa1521'],
                marker_color='sandybrown'  # cambiar nuemeritos de rgb
                ))

graf_tasafem.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    #title='Tasa feminicidio periodo 2015-2020',
    xaxis_tickfont_size= 12,
    yaxis=dict(
        title='Totales acumulados por entidad',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    autosize=True,
#    width=2100,
#    height=600
    )


######################################################### Grafica de Totales por entidad 

TasasTot15_21index=junto15_21[['Entidad','Totfem1521','Totpob1521','Tasa1521']].sort_values('Totfem1521',ascending=False)

graf_totfem = go.Figure()
graf_totfem.add_trace(go.Bar(x=TasasTot15_21index['Entidad'],y=TasasTot15_21index['Totfem1521'],
                marker_color='indianred'  # cambiar nuemeritos de rgb
                ))

graf_totfem.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    #title='Tasa feminicidio periodo 2015-2020',
    xaxis_tickfont_size= 12,
    yaxis=dict(
        title='Tasa cada 100 000 habitantes',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    autosize=True,
 #   width=2100,
  #  height=600
    )





####################################

# A P P

####################################

########### Define your variables
mytitle=' '
tabtitle='Violencia familiar'
sourceurl='https://www.gob.mx/sesnsp/acciones-y-programas/datos-abiertos-de-incidencia-delictiva?state=published'


server = flask.Flask(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes. LUX], server=server)

body = html.Div([
# Cintillo 000
        dbc.Row(
           [
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
                        width={'size': 1,  "offset": 1}),
               dbc.Col(html.H1("Violencia familiar (2015-2020)"),
                        width={'offset' : 2}),
           ]),

#Cintillo 00    
    dbc.Row(
           [
               dbc.Col(html.H6(d2),           #Fecha de actualización
               width={'size' : "auto",
                      'offset' : 4}), 
               dbc.Col(html.H6("Fuente: SENSNSP"),
                        width={'size': 3,  "offset":1 }),
            ]),
               
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
    
    
#cintillo 0
    
     dbc.Row(
           [
               dbc.Col(html.H1(["Casos ", 
                                dbc.Badge("anuales", color="info", className="mr-1")]),
                        width={'size': 8,  "offset":1 }),
            ]),

       html.Hr(),
       html.Hr(),
       html.Hr(),
    
     dbc.Row(
           [
               dbc.Col(html.H5("2015")),
               dbc.Col(html.H5("2016")),
               dbc.Col(html.H5("2017")),
               dbc.Col(html.H5("2018")),
               dbc.Col(html.H5("2019")),
               dbc.Col(html.H5("2020")),
           ], justify= "start"),
    
#Cintillo 1
    dbc.Row(
           [
               dbc.Col(html.H1([str(f"{conf_2015:,}")])),
                   #conf_2015)),
               dbc.Col(html.H1([str(f"{conf_2016:,}")])),
               dbc.Col(html.H1([str(f"{conf_2017:,}")])),
               dbc.Col(html.H1([str(f"{conf_2018:,}")])),
               dbc.Col(html.H1([str(f"{conf_2019:,}")])),
               dbc.Col(html.H1([str(f"{conf_2020:,}")])),
            ],justify= "start"),
    
# Cintillo 1.1
        dbc.Row([
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Violencia-Familiar/blob/main/application/static/mapa2015.jpeg?raw=true")),
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Violencia-Familiar/blob/main/application/static/mapa2016.jpeg?raw=true")),
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Violencia-Familiar/blob/main/application/static/mapa2017.jpeg?raw=true")),
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Violencia-Familiar/blob/main/application/static/mapa2018.jpeg?raw=true")),
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Violencia-Familiar/blob/main/application/static/mapa2019.jpeg?raw=true")),
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Violencia-Familiar/blob/main/application/static/mapa2020.jpeg?raw=true")),
               #dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Violencia-Familiar/blob/main/application/static/mapa2021.jpeg?raw=true")),
          
        ]),
# Cintillo párrafos
       html.Hr(),
    
      dbc.Row([
               dbc.Col(dbc.Container([
                       html.P(
                           "En 2015 en 10 entidades se registró  71.56 % de la violencia familiar (91,181 delitos) :  Nuevo León  (17,062),  Ciudad de México  (16,103),  Chihuahua  (12,273),  Guanajuato  (10,298),  Baja California  (8,892),  Jalisco  (8,543),  Puebla  (5,024),  México  (4,722),  Tabasco  (4,230),  y  Morelos  (4,034).",
                    className="top",)
                                ], fluid=True)
                       
                      ),
          dbc.Col(dbc.Jumbotron([
                   dbc.Container([
                       html.P(
                           "En 2016 en 10 entidades se registró  67.16 % de la violencia familiar (103,361 delitos) :  Ciudad de México  (18,426),  Nuevo León  (17,773),  Chihuahua  (11,960),  Jalisco  (11,431),  Guanajuato  (11,133),  Baja California  (8,315),  Coahuila de Zaragoza  (6,885),  Tamaulipas  (6,378),  Puebla  (5,586),  y  México  (5,474).",
                    className="top")
                                ], fluid=True)
                                    ], fluid=True)
                      ),
          dbc.Col(
                   dbc.Container([
                       html.P(
                           "En 2017 en 10 entidades se registró  62.45 % de la violencia familiar (105,906 delitos) :  Ciudad de México  (18,360),  Nuevo León  (17,145),  Chihuahua  (11,583),  Guanajuato  (11,253),  Jalisco  (9,557),  Coahuila de Zaragoza  (8,968),  Baja California  (8,554),  Tamaulipas  (7,030),  México  (6,860),  y  Tabasco  (6,596).",
                    className="top")
                                ], fluid=True)
                                    )
                      ,
          dbc.Col(dbc.Jumbotron([
                   dbc.Container([
                       html.P(
                           "En 2018 en 10 entidades se registró  59.54 % de la violencia familiar (107,290 delitos) :  Ciudad de México  (19,931),  Nuevo León  (16,410),  Chihuahua  (11,227),  Guanajuato  (10,356),  Baja California  (9,904),  Coahuila de Zaragoza  (9,791),  Jalisco  (8,850),  Puebla  (7,296),  Tamaulipas  (7,029),  y  México  (6,496).",
                    className="top")
                                ], fluid=True)
                                    ], fluid=True)
                      ),
          dbc.Col(dbc.Container([
                       html.P(
                           "En 2019 en 10 entidades se registró  59.48 % de la violencia familiar (125,029 delitos) :  Ciudad de México  (25,775),  Nuevo León  (16,339),  Guanajuato  (11,142),  Jalisco  (11,053),  Chihuahua  (10,968),  Coahuila de Zaragoza  (10,647),  Baja California  (10,455),  Veracruz de Ignacio de la Llave  (10,324),  México  (9,249),  y  Puebla  (9,077).",
                    className="top")
                                ], fluid=True)
                      ),
          dbc.Col(dbc.Jumbotron([
                   dbc.Container([
                       html.P(
                          "En 2020 en 10 entidades se registró  61.55 % de la violencia familiar (135,425 delitos) :  Ciudad de México  (27,769),  Nuevo León  (17,940),  México  (16,915),  Jalisco  (11,890),  Chihuahua  (11,293),  Baja California  (10,781),  Veracruz de Ignacio de la Llave  (10,386),  Guanajuato  (10,035),  Coahuila de Zaragoza  (9,291),  y  Puebla  (9,125).",
                    className="top")
                                ], fluid=True)
                                    ], fluid=True),
                  
                      ),
 
      ]),
                
    
       html.Hr(),
       html.Hr(),
       
#---------Grafica mensual
     dbc.Row(
           [
               dbc.Col(html.H1(["Casos ", 
                       dbc.Badge("mensuales", color="info", className="mr-1")]), 
                                       width={'size': 11,  "offset":1 })]),
       dbc.Row([        
               dbc.Col(html.H5("(hasta febrero 2021)"),
                                       width={ 'size': 3, "offset":1 }),

            ]),
   
    dbc.Row(
        [
            dbc.Col(dcc.Graph(figure=graf_meses, config= "autosize")),
        ]),

      
       html.Hr(),
       html.Hr(),
    
##Cintillo mapas y ranking

    #títulos
     dbc.Row(
           [
               dbc.Col(html.H1([dbc.Badge("Municipios", color="info", className="ml-1"), 
                               " en entidades con más casos acumulados ",]),
                       
                        width={'size': 10,  "offset":1 }),
            ]),

       html.Hr(),
       html.Hr(),
       html.Hr(),
    
     dbc.Row(
           [
               dbc.Col(html.H3("Ciudad de México", ),
                       #width=1, 
                       lg={'size': 1,  "offset": 1, }
                      ),
               
               dbc.Col(html.H3("México"),
                        #width=1, 
                       lg={'size': 1,  "offset": 1, }
                      ),
               
               dbc.Col(html.H3("Nuevo León "),
                       # width=1, 
                       lg={'size': 3,  "offset": 2, }
                      ),
                      
               dbc.Col(html.H3("Jalisco "),
                       # width=1, 
                       lg={'size': 1,  "offset": 1, }
                      ),
           ], #, justify= "end", 
    align= "center"),

    
    dbc.Row([
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Violencia-Familiar/blob/main/application/static/cdmx.jpeg?raw=true"),
                      #width=4,lg={'size': 3,  "offset": 3, }
                      ),
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Violencia-Familiar/blob/main/application/static/mx1.jpg?raw=true"),
                      #width=4,lg={'size': 3,  "offset": 3, }
                      ),
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Violencia-Familiar/blob/main/application/static/nvoleon.jpeg?raw=true"),
                      #width=4,lg={'size': 3,  "offset": 3, }
                      ),
               dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/Violencia-Familiar/blob/main/application/static/jal.jpeg?raw=true"),
                      #width=4,lg={'size': 3,  "offset": 3, }
                      ),
           ], no_gutters=True),
       #html.Hr(),

    #################################################################  MUNICIPIOS ranking    




    dbc.Row([
               dbc.Col(dbc.Container([
                       html.P(
                          "Las 10 alcaldías con más violencia familiar fueron: Iztapalapa (24,331), Gustavo A. Madero (15,405), Cuauhtémoc (10,556), Álvaro Obregón (10,006), Tlalpan (9,403), Coyoacán (8,537), Iztacalco (8,115), Venustiano Carranza (7,423), Xochimilco (6,696), y Azcapotzalco (6,457).",
 
                    className="top",)
                                ], fluid=True)
                       
                      ),
          dbc.Col(dbc.Jumbotron([
                   dbc.Container([
                       html.P(
                           "Los 10 municipios con más violencia familiar fueron: Ecatepec de Morelos (5,828), Toluca (3,926), Nezahualcóyotl (3,353), Naucalpan de Juárez (3,304), Cuautitlán Izcalli (2,310), Tlalnepantla de Baz (1,964), Atizapán de Zaragoza (1,936), Chalco (1,853), Tultitlán (1,835), y Tecámac (1,664).",
                    className="top")
                                ], fluid=True)
                                    ], fluid=True)
                      ),

       dbc.Col(
                   dbc.Container([
                       html.P(
                           "Los 10 municipios con más violencia familiar fueron: Monterrey (20,079), Guadalupe (11,511), Apodaca (10,997), Juárez (10,074), García (9,976), San Nicolás de los Garza (5,758), Santa Catarina (5,543), Cadereyta Jiménez (3,127), Pesquería (3,029), y Salinas Victoria (1,633).",
                    className="top")
                                ], fluid=True)
                                    )
                      ,
          dbc.Col(dbc.Jumbotron([
                   dbc.Container([
                       html.P(
                          "Los 10 municipios con más violencia familiar fueron: Guadalajara (14,481), Zapopan (11,968), Tlajomulco de Zúñiga (6,400), Tonalá (5,527), Puerto Vallarta (3,333), El Salto (1,779), Tepatitlán de Morelos (964), Lagos de Moreno (889), Autlán de Navarro (759), y Ameca (660).",
                    className="top")
                                ], fluid=True)
                                    ], fluid=True)
                      ),
      ]),

############################################  MUNICIPIOS ranking (OPCION  2)
 #  dbc.Row([
 #             dbc.Col(dbc.Container([
 #                     html.P(
 #                         "Ecatepec de Morelos (56)"
 #                         "Chimalhuacán (35)"
 #                         "Nezahualcóyotl (31)"
 #                         "Toluca (27)"
 #                         "Naucalpan de Juárez (22)"
 #                         "Ixtapaluca (22)"
 #                         "Zumpango (21)"
 #                         "Tecámac (19)"
 #                         "Cuautitlán Izcalli (19)"
 #                         "Valle de Chalco Solidaridad (16)",
 #                  className="top",)
 #                              ],)
 #                     
 #                    ),
 #        dbc.Col(dbc.Jumbotron([
 #                 dbc.Container([
 #                     html.P(
 #                         "Veracruz (49)"
 #                         "Xalapa (42)"
 #                         "Coatzacoalcos (25)"
 #                         "Córdoba (24)"
 #                         "Poza Rica de Hidalgo (17)"
 #                         "Tuxpan (13)"
 #                         "Papantla (12)"
 #                         "Tierra Blanca (11)"
 #                         "Minatitlán (11)"
 #                         "San Andrés Tuxtla (11)",
 #                  className="top")
 #                              ], )
 #                                  ], )
 #                    ),
 #        dbc.Col(
 #                 dbc.Container([
 #                     html.P(
 #                         "Iztapalapa (68)"
 #                         "Gustavo A. Madero (37)"
 #                         "Tlalpan (35)"
 #                         "Cuauhtémoc (34)"
 #                         "Xochimilco (25)"
 #                         "Miguel Hidalgo (19)"
 #                         "Álvaro Obregón (17)"
 #                         "Tláhuac (16)"
 #                         "Coyoacán (14)"
 #                         "Venustiano Carranza (14)",
 #                  className="top")
 #                              ],)
 #                                  )
 #                    ,
 #        dbc.Col(dbc.Jumbotron([
 #                 dbc.Container([
 #                     html.P(
 #                         "Guadalajara (51)"
 #                         "Tlajomulco de Zúñiga (38)"
 #                         "Zapopan (34)"
 #                         "El Salto (24)"
 #                         "Tonalá (17)"
 #                         "Puerto Vallarta (10)"
 #                         "Ocotlán (6)"
 #                         "Tequila (6)"
 #                         "Mezquitic (6)"
 #                         "Ixtlahuacán de los Membrillos (6)",
 #                  className="top")
 #                              ], )
 #                                  ], )
 #                    ),
 #    ]),
 #  
#       html.Hr(),
#       html.Hr(),
#       html.Hr(),
#       html.Hr(),
#       html.Hr(),
#       html.Hr(),
#    
    
    dbc.Row([
               
           ]),
   
    
# Cintillo 3
    
# tablas 3-4    
#    dbc.Row([
#               dbc.Col(dbc.Table.from_dataframe(patabla3a,
#                        bordered="success", size=422, striped=True), 
#                        width=4, lg={'size': 3,  "offset": 2, }),
#        
#               dbc.Col(dbc.Table.from_dataframe(patabla4a,
#                        bordered="success", size=422, striped=True), 
#                        width=4, lg={'size': 3,  "offset": 3, }),
#            ], justify="center", no_gutters=False),
##
 #      html.Hr(),
 #      html.Hr(),
 #      html.Hr(),
 #      html.Hr(),
 #      html.Hr(),
 #      html.Hr(),
 #      html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       
#---------Grafica por entidad
     dbc.Row(
           [
               dbc.Col(html.H1([dbc.Badge("Comparativo", color="info", className="mr-1"),
                               " entre casos acumulados & tasas "]),
                       width={'size': 10,  "offset":1 }),
            ]),

       html.Hr(),
       html.Hr(),
       html.Hr(),
    
    dbc.Row(
           [
               dbc.Col(html.H4("Total acumulado por entidad"),
                        width=2,lg={'size': 4,  "offset": 1, }),

               dbc.Col(html.H4("Tasa por entidad"),
                       width=1, lg={'size': 3,  "offset": 4, }),                     #size=12
               
            ], justify="end",),
   
    dbc.Row(
        [
            dbc.Col(dcc.Graph(figure=graf_totfem , config= "autosize")),
                   #lg={'size': 5,  "offset": 0,}),
            
            dbc.Col(dcc.Graph(figure= graf_tasafem, config= "autosize")),
                   #lg={'size': 5,  "offset": 1,}),
        ], justify="end", no_gutters=True,),

       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
       html.Hr(),
    

# nuevo
    
  # #dbc.Jumbotron(
   #[
   #    dbc.Container(
   #        [
   #            html.H4("Consideraciones generales "),
   #            html.P(
   #                "Los feminicidios son un problema aún irresuelto y son tema central de la " 
   #                "agenda de seguridad nacional. Su gravedad se observa "
   #                "en los registros anuales y registros mensuales, que se presentan al "
   #                "inicio de esta visualización."
   #                "Existe mayor atención institucional al fenómeno y fuerte preocupación de la sociedad, " 
   #                "lo que se evidencia en el hecho que todos seamos más vigilantes al respecto. "
   #                "No obstante, aún hace falta más acción social, sobretodo, más intervención institucional "
   #                "para diseñar estrategias efectivas de prevención y promover su denuncia. Es imperante "
   #                "acabar con esta violencia de género. "
   #                "El presente dashboard (tablero de datos) es un ejercicio institucional con el objeto de "
   #                "informar a la sociedad. La información proviene del Secretariado Ejecutivo Nacional del Sistema Nacional de "
   #                "Seguridad Pública (SENSNSP). El lector debe ser advertido que el período cubierto "
   #                "es del mes de enero de 2015 hasta el mes de enero del 2021. "
   #                "Ademas, esta dashboard seguramente puede ser completado con otras fuentes de información "
   #                "gubernamental y por toda aquella información proveniente de organizaciones civiles que " 
   #                "dan seguimiento al tema. En ningún caso, este contenido representa algún "
   #                "posicionamiento partidista, personal o institucional, mucho menos opinión o postura alguna "
   #                "sobre el fenómeno. ",
   #                className="lead"),
   #            html.Hr(),
   #            html.H5("Metodología "),
   #            html.P(
   #                "Esta información fue tratada con el lenguaje de programación Python y varias de las librerías "
   #                "más comunes (Dash, Choropleth, Pandas, Numpy, Geopandas, etc.), que nos ayudan a automatizar "
   #                "la recurrencia (request) a la fuente de información y las operaciones necesarias para creargraficas "
   #                "interactivas y mapas presentados. ",
   #                className="lead"),
   #                
   #        ], fluid=True,
   #    )
   #],
   #fluid=True,
   #),    
    
        
    
    
    

    dbc.Row([
                                    #https://github.com/fdealbam/CamaraDiputados/blob/b11ef31e8e0f73e1a4a06ce60402563e1bd0122e/application/static/logocamara.jfif
           dbc.Col(dbc.CardImg(src="https://github.com/fdealbam/CamaraDiputados/blob/main/application/static/logocamara.jfif?raw=true"),
                        width=4, lg={'size': 1,  "offset": 3, }),
            
           dbc.Col(html.H6(" S e c r e t a r í a   G e n e r a l," 
                           " Secretaría de Servicios Parlamentarios, "
                           " México, 2021 "),
                  width={'size': 3, 'offset': 0}),
               ], justify="start",),
        
            ])


app.layout = html.Div([body])

from application.dash import app
from settings import config

if __name__ == "__main__":
    app.run_server()
