import numpy as np
import pandas as pd
import os
import xlsxwriter


import pandas as pd
import numpy as np
import os

ruta_pickle = "E://EPN//PYTHON//py-narvaez-jeferson//03 - Deber//artwork_data.pickle"

df = pd.read_pickle(ruta_pickle)
sub_df = df.iloc[49989:50519:,].copy()

path_excel = "./artwork_chart.xlsx"

num_artistas = sub_df['artist'].value_counts()

writer = pd.ExcelWriter(path_excel,engine='xlsxwriter')

num_artistas.to_excel(writer,sheet_name='Artistas')
workbook = writer.book
worksheet = writer.sheets['Artistas']

chart = workbook.add_chart({'type': 'column','name':'Artistas'})
chart.add_series({
    
    'values':     '=Artistas!$B$2:$B$21',
    'categories': '=Artistas!$A$2:$A$21',
    'gap':        20,
    'data_labels': {'value': True},
})
chart.set_title({'name': 'Artwork by artist'})
chart.set_legend({'none': True})
chart.set_style(9)
worksheet.insert_chart('D2', chart, {'x_scale': 2.0, 'y_scale': 2.0})
writer.save()