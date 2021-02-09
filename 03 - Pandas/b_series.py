# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 07:58:11 2020

@author: JeffTheKiller
"""

import numpy as np
import pandas as pd
lista_numeros=[1,2,3,4]
tupla_numeros=(1,2,3,4)
np_numeros=np.array((1,2,3,4))

series_a=pd.Series(lista_numeros)
series_b=pd.Series(tupla_numeros)
series_c=pd.Series(np_numeros)

series_d=pd.Series([True,False,12,12.12,"Adrian",None,(1),[2],{"Nombre":"Jeferson"}])
print(series_d[3])

lista_ciudades=["Ambato","Cuenca","Loja","Quito"]
serie_ciudad=pd.Series(lista_ciudades,index=["A","C","L","Q"])

print (serie_ciudad[3])
print(serie_ciudad["C"])

valores_ciudad={
    "Ibarra":9500,
    "Guayaquil":10000,
    "Cuenta":7000,
    "Quito":8000,
    "Loja":3000}
serie_valor_ciudad=pd.Series(valores_ciudad)
ciudades_menor_5k=serie_valor_ciudad<5000
print(type(serie_valor_ciudad))
print(type(ciudades_menor_5k))
print(ciudades_menor_5k)
s5=serie_valor_ciudad[ciudades_menor_5k]

serie_valor_ciudad=serie_valor_ciudad*1.1
serie_valor_ciudad["Quito"]=serie_valor_ciudad["Quito"]-50
print ("Lima" in serie_valor_ciudad)





svc_cuadrado=np.square(serie_valor_ciudad)
ciudades_uno=pd.Series({"Montañita":3000,
                        "Guayaquil":10000,
                        "Quito":2000})

ciudades_dos=pd.Series({"Loja":3000,
                        "Ambato":10000})
ciudades_uno["Loja"]=0
print(ciudades_uno+ciudades_dos)
#ademas de add hay sub mul div
ciudaddes_add=ciudades_uno.add(ciudades_dos)
 
 #El verify_integrity sirve para ver si los datos se estan repitiendo
#concat y append es lo mismo
#ciudad_concat=pd.concat([ciudades_uno,ciudades_dos],verify_integrity=True)
print(ciudades_uno.max())
print(ciudades_uno.min())

print(ciudades_uno.mean())
print(ciudades_uno.median())
print(np.average(ciudades_uno))
print(ciudades_uno.head(2))
print(ciudades_uno.tail(2))
resultado=ciudade_uno.where(ciudades_uno<5999)




