# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 09:26:48 2020

@author: JeffTheKiller
"""


#c_dataframe.py

import numpy as np
import pandas as pd
arr_pand=np.random.randint(0,10,6).reshape(2,3)
df1=pd.DataFrame(arr_pand)

s1=df1[0]
s2=df1[1]
s2=df1[2]

df1[3]=s1
df1[4]=s1*s2

datos_fisicos_uno=pd.DataFrame(
    arr_pand,
    columns=[
        'Estatura(cm)',
        'Peso(Kg)',
        'Edad (anios)'])
datos_fisicos_dos=pd.DataFrame(
    arr_pand,
    columns=[
        'Estatura(cm)',
        'Peso(Kg)',
        'Edad (anios)'],
    index=['Jeferson','Juan'])
print(datos_fisicos_dos['Peso(Kg)'])
serie_peso=datos_fisicos_dos['Peso(Kg)']
datos_jeferson=serie_peso['Jeferson']
print("SERIE PESO:",serie_peso)
print("MIS DATOS:",datos_jeferson)

df1.index=['Narvaez','Pepe']
df1.index=['Karla','Carolina']
df1.columns=['A','B','C','D','E']











