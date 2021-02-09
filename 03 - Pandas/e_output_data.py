import numpy as np
import pandas as pd
import os
import sqlite3

path_guardado = "./data/artwork_data.pickle"

df = pd.read_pickle(path_guardado)

sub_df = df.iloc[49980:50519,:].copy()

# Tipos de archivos
#JSON
#Excel
#SQL

# Excel
path_excel = "./data/artwork_data.xlsx"
path_excel_indice = "./data/artwork_data_indice.xlsx"
path_excel_columnas = "./data/artwork_data_columnas.xlsx"

# Con el indice como columna
# sub_df.to_excel(path_excel)

# Sin el indice como columna
# sub_df.to_excel(path_excel_indice, index = False)

columnas = ['artist', 'title', 'year']
sub_df.to_excel(path_excel_columnas, columns = columnas)

# Multiples hojas de trabajo
path_excel_mt = "./data/artwork_data_mt.xlsx"

writer = pd.ExcelWriter(path_excel_mt,
                        engine = 'xlsxwriter')

sub_df.to_excel(writer, sheet_name = 'Primera')
sub_df.to_excel(writer, sheet_name = 'Segunda')
sub_df.to_excel(writer, sheet_name = 'Tercera')

writer.save()

# Formato condicional
num_artistas = sub_df['artist'].value_counts()

print(type(num_artistas))
print(num_artistas)

path_excel_colores = "./data/artwork_data_colores.xlsx"

writer = pd.ExcelWriter(path_excel_colores,
                            engine='xlsxwriter')
# Series

num_artistas.to_excel(writer, 
                      sheet_name = 'Artistas')

# Seleccionando la hoja de trabajo

hoja_artistas = writer.sheets['Artistas']

ultimo_numero = len(num_artistas.index) + 1

# rango_celdas = 'B2:B{}'.format()

rango_celdas = f'B2:B{ultimo_numero}'

print(rango_celdas)

# Formato

formato_artistas = {
        "type": "2_color_scale",
        "min_value": "10",
        "min_type": "percentile",
        "max_value": "99",
        "max_type": "percentile"}

hoja_artistas.conditional_format(rango_celdas,
                                 formato_artistas)

writer.save()

########## SQL ##########

with sqlite3.connect("bdd_artist.bdd") as conexion:
    sub_df.to_sql('py_artistas', conexion)
    

## with mysql.connect('mysql://user:password@ip:puerto/nombre_base')
##      df5.to_sql('tabla_mysql', conexion)
    
########## JSON ##########

sub_df.to_json('artistas.json')

sub_df.to_json('artistas_tabla.json', orient = 'table')









