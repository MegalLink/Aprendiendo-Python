import numpy as np
import pandas as pd
from scipy import misc
# 1) Examen

## 2) Crear un vector de ceros de tamaño 10
print("Ejericio 2")
vector_zeros=np.zeros(10)
print(vector_zeros)
## 3) Crear un vector de ceros de tamaño 10 y el de la posicion 5 sea igual a 1
print("Ejericio 3")
vector_zeros[5]=1
print(vector_zeros)

## 4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.
print("Ejericio 4")
arreglo_ej4=np.arange(50)
print(arreglo_ej4)
print("invertido")
print(arreglo_ej4[::-1])
## 5) Crear una matriz de 3 x 3 con valores del cero al 8
print("Ejericio 5")
print(np.arange(9).reshape(3,3))

## 6) Encontrar los indices que no sean cero en un arreglo
print("Ejericio 6")
arreglo_ej6=np.array([1,2,0,0,4,0])
print(arreglo_ej6[arreglo_ej6!=0])

## 7) Crear una matriz de identidad 3 x 3 
print("Ejericio 7")
print(np.eye(3))
## 8) Crear una matriz 3 x 3 x 3 con valores randomicos
print("Ejericio 8")
print(np.random.rand(3,3,3))
## 9) Crear una matriz 10 x 10 y encontrar el mayor y el menor
print("Ejericio 9")
arreglo_ej9=np.arange(100).reshape(10,10)
print(f"Maximo {arreglo_ej9.max()}")
print(f"Minimo {arreglo_ej9.min()}")


## 10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)
print("Ejericio 10")
mapache = misc.face()
print(mapache)
## 11) ¿Como crear una serie de una lista, diccionario o arreglo?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serieDict=pd.Series(mydict)

## 12) ¿Como convertir el indice de una serie en una columna de un DataFrame?

print("Ejercicio 12")
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
#print(mydict.keys())
ser = pd.Series(mydict) 
#print(ser.index)
datafr=pd.DataFrame(ser.index)
print(datafr)
# Transformar la serie en dataframe y hacer una columna indice
datafr2=pd.DataFrame(ser)
## 13) ¿Como combinar varias series para hacer un DataFrame?


ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))
dfseries=pd.DataFrame(ser1)
dfseries[1]=pd.DataFrame(ser2)

## 14) ¿Como obtener los items que esten en una serie A y no en una serie B?

ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])
ser_res_14=ser1[~ser1.isin(ser2)]

## 15) ¿Como obtener los items que no son comunes en una serie A y serie B?


ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

ser_res_15=pd.concat([ser1[~ser1.isin(ser2)],ser2[~ser2.isin(ser1)]],verify_integrity=False)

## 16) ¿Como obtener el numero de veces que se repite un valor en una serie?


ser_16 = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))
res_ser_16=len(ser_16[ser_16=='a'])


## 17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?


np.random.RandomState(100)
ser_17 = pd.Series(np.random.randint(1, 5, [12]))
#Este no acabe

## 18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un `shape` definido?



ser_18 = pd.Series(np.random.randint(1, 10, 35))
#shape(7,5)
#Este no acabe

## 19) ¿Obtener los valores de una serie conociendo la posicion por indice?



ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u
res_19=ser[pos]

## 20) ¿Como anadir series vertical u horizontalmente a un DataFrame?



ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))



## 21)¿Obtener la media de una serie agrupada por otra serie?

#groupby tambien esta disponible en series.



frutas = pd.Series(np.random.choice(['manzana', 'banana', 'zanahoria'], 10))
pesos = pd.Series(np.linspace(1, 10, 10))
print(pesos.tolist())
print(frutas.tolist())
#> [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
#> ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']

# Los valores van a cambiar por ser random
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64




## 22)¿Como importar solo columnas especificas de un archivo csv?

#https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv.