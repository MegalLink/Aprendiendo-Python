# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:09:07 2020

@author: JeffTheKiller
"""
import pandas as pd
import os
path="./data/artwork_data.csv"

df1=pd.read_csv(path,nrows=10)
columnas=['id','artist','title','medium','year']
df2=pd.read_csv(path, nrows=10,usecols=columnas)

df3=pd.read_csv(path, nrows=10,usecols=columnas,index_col='id')


path_guardado='./data/artwork_data.pickle'

df3.to_pickle(path_guardado)

df4=pd.read_pickle(path_guardado)





























