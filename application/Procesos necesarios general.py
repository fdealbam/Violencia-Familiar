#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import pandas as pd
import geopandas as gpd
import sidetable as stb
import matplotlib.pyplot as plt


# In[24]:



# Procesos necesarios (violencia de género)


###################################################
# Proceso inicial de tratamiento de la base completa 
###################################################

#link https://www.gob.mx/sesnsp/acciones-y-programas/incidencia-delictiva-del-fuero-comun-nueva-metodologia?state=published
#descargar con  el nombre: nombre variable 
# "Municipal-Delitos-2015-2021_feb2021"


import pandas as pd
os.chdir(r"C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\\")     #_____________________Ruta Fe
    
columns = ['Año', 'Clave_Ent', 'Entidad', 'Cve. Municipio', 'Municipio',
        'Tipo de delito', 'Subtipo de delito', 'Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
       'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

delitos = pd.read_csv("Municipal-Delitos-2015-2021_feb2021.csv", encoding= "Latin-1", 
                      usecols= columns)

mpios_viol = delitos[delitos["Tipo de delito"] =='Abuso sexual']#|
                     #(delitos["Tipo de delito"] =='Violación equiparada')]
                     
                     
mpios_viol.to_csv('Abusosexual20152021.csv')#, header=True)


#print("Se creo el archivo ahora hay que subirlo al GITHUB")


# In[26]:


tos= pd.read_csv('Abusosexual20152021.csv')#, header=True)
tos.head()


# In[28]:






#########################################
# Tratamiento 
#########################################


delitos = pd.read_csv(r"https://raw.githubusercontent.com/fdealbam/abusosexual/main/Abusosexual20152021.csv")
delitos.drop('Unnamed: 0',1, inplace=True)

delitos.groupby(['Año','Entidad',])['Enero', 
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
 #'Agosto21','Septiembre21','Octubre21','Noviembre21','Diciembre21'
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
femi15_21['Total2021']= femi15_21[[ 'Enero21', 'Febrero21',# 'Marzo20', 'Abril20', 'Mayo20',
                               #'Junio20', 'Julio20', 'Agosto20', 'Septiembre20', 'Octubre20',
                               #'Noviembre20', 'Diciembre20',
                                  ]].sum(axis=1)







##############################################

# M A P A S

##############################################


############################################## Mapas nacionales con división por entidad

year_list=['Total2015','Total2016','Total2017','Total2018','Total2019','Total2020','Total2021']


for e in year_list:
    
# Ruta archivo shp
    os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\bases')     #_____________________Ruta Fe
    #os.chdir(r'C:\Users\IVANOV\AnacondaProjects\0 0 Projects\dash_fem\bases\shp') #_____________________Ruta Wi
    #os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\bases')     #_____________________Ruta Ae

    geo_df=gpd.read_file('México_Estados.shp')

    geo_df.replace(['Coahuila','Distrito Federal','Michoacán',"Veracruz"],
               #por
               ['Coahuila de Zaragoza','Ciudad de México','Michoacán de Ocampo','Veracruz de Ignacio de la Llave'],
               inplace=True, )

    
# Merge para entidades
    concat0 = geo_df.merge(femi15_21,
                           left_on= "ESTADO",
                           right_on="Entidad", how= "right")
    
    concat1 = geo_df.merge(femi15_21,
                           left_on= "ESTADO",
                           right_on="Entidad", how= "right").sort_values(e, ascending=False).head(5)

    a1= concat0.plot(e, #_________________< Cambiar año
                     color='floralwhite',  
                     legend=False, 
                     linewidth=.1, 
                     edgecolor= "black", 
                     figsize=(3,3))

    concat1.plot(e, #_________________< Cambiar año
                 ax=a1 ,
                 color='brown',
                 linewidth=.2, 
                 edgecolor= "black", 
                 figsize=(3,3))

    plt.axis("off")

# Ruta guardado
    os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\results\\')      #_____________________Ruta Fe
    #os.chdir(r'C:\Users\IVANOV\AnacondaProjects\0 0 Projects\dash_fem\resultados') #_____________________Ruta Wi
    #os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\bases')      #_____________________Ruta Ae

    plt.savefig("Mapa abusosexual %s.jpeg" %(e), dpi= 120)
    print("Guardado abusosexual %s" %(e))
    plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Violacion

# In[5]:


delitos = pd.read_csv("https://github.com/fdealbam/Violacion/blob/main/Violacion2015_2021.csv?raw=true")
delitos.drop('Unnamed: 0',1, inplace=True)


# In[6]:


delitos.groupby(['Año','Entidad',])['Enero', 
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
 #'Agosto21','Septiembre21','Octubre21','Noviembre21','Diciembre21'
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
femi15_21['Total2021']= femi15_21[[ 'Enero21', 'Febrero21',# 'Marzo20', 'Abril20', 'Mayo20',
                               #'Junio20', 'Julio20', 'Agosto20', 'Septiembre20', 'Octubre20',
                               #'Noviembre20', 'Diciembre20',
                                  ]].sum(axis=1)


# In[7]:


year_list=['Total2015','Total2016','Total2017','Total2018','Total2019','Total2020','Total2021']


for e in year_list:
    
# Ruta archivo shp
    #os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\bases')     #_____________________Ruta Fe
    os.chdir(r'C:\Users\IVANOV\AnacondaProjects\0 0 Projects\dash_fem\bases\shp') #_____________________Ruta Wi
    #os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\bases')     #_____________________Ruta Ae

    geo_df=gpd.read_file('México_Estados.shp')

    geo_df.replace(['Coahuila','Distrito Federal','Michoacán',"Veracruz"],
               #por
               ['Coahuila de Zaragoza','Ciudad de México','Michoacán de Ocampo','Veracruz de Ignacio de la Llave'],
               inplace=True, )

    
# Merge para entidades
    concat0 = geo_df.merge(femi15_21,
                           left_on= "ESTADO",
                           right_on="Entidad", how= "right")
    
    concat1 = geo_df.merge(femi15_21,
                           left_on= "ESTADO",
                           right_on="Entidad", how= "right").sort_values(e, ascending=False).head(5)

    a1= concat0.plot(e, #_________________< Cambiar año
                     color='White',  
                     legend=False, 
                     linewidth=.1, 
                     edgecolor= "black", 
                     figsize=(3,3))

    concat1.plot(e, #_________________< Cambiar año
                 ax=a1 ,
                 color='brown',
                 linewidth=.2, 
                 edgecolor= "black", 
                 figsize=(3,3))

    plt.axis("off")

# Ruta guardado
    #os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\bases')      #_____________________Ruta Fe
    os.chdir(r'C:\Users\IVANOV\AnacondaProjects\0 0 Projects\dash_fem\resultados') #_____________________Ruta Wi
    #os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\bases')      #_____________________Ruta Ae

    plt.savefig("Mapa violacion %s.jpeg" %(e), dpi= 120)
    print("Guardado violacion %s" %(e))
    plt.show()


# In[ ]:





# In[ ]:





# # Violencia familiar

# In[16]:





# In[17]:


# viene del github


delitos = pd.read_csv("https://github.com/fdealbam/Violencia-Familiar/blob/main/ViolenciaFamiliar2015_2021.csv?raw=true")
delitos.drop('Unnamed: 0',1, inplace=True)



delitos.groupby(['Año','Entidad'])['Enero', 
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


# In[19]:


###############################################

# M A P A S 

###############################################

year_list=['Total2015','Total2016','Total2017','Total2018','Total2019','Total2020','Total2021']


for e in year_list:
    
# Ruta archivo shp
    
    os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\bases')     #_____________________Ruta Fe
    #os.chdir(r'C:\Users\IVANOV\AnacondaProjects\0 0 Projects\dash_fem\bases\shp') #_____________________Ruta Wi
    #os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\bases')     #_____________________Ruta Ae

    geo_df=gpd.read_file('México_Estados.shp')

    geo_df.replace(['Coahuila','Distrito Federal','Michoacán',"Veracruz"],
               #por
               ['Coahuila de Zaragoza','Ciudad de México','Michoacán de Ocampo','Veracruz de Ignacio de la Llave'],
               inplace=True, )

    
# Merge para entidades
    concat0 = geo_df.merge(femi15_21,
                           left_on= "ESTADO",
                           right_on="Entidad", how= "right")
    
    concat1 = geo_df.merge(femi15_21,
                           left_on= "ESTADO",
                           right_on="Entidad", how= "right").sort_values(e, ascending=False).head(5)

    a1= concat0.plot(e, #_________________< Cambiar año
                     color='floralwhite',  
                     legend=False, 
                     linewidth=.1, 
                     edgecolor= "black", 
                     figsize=(3,3))

    concat1.plot(e, #_________________< Cambiar año
                 ax=a1 ,
                 color='brown',
                 linewidth=.2, 
                 edgecolor= "black", 
                 figsize=(3,3))

    plt.axis("off")

# Ruta guardado
    os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\results\\')      #_____________________Ruta Fe
    #os.chdir(r'C:\Users\IVANOV\AnacondaProjects\0 0 Projects\dash_fem\resultados') #_____________________Ruta Wi
    #os.chdir(r'C:\Users\win\AnacondaProjects\0 0 Projects\Project_11\bases')      #_____________________Ruta Ae

    plt.savefig("Mapa violfam %s.jpeg" %(e), dpi= 120)
    print("Guardado violfam %s" %(e))
    plt.show()


# In[ ]:





# In[ ]:





# In[ ]:




