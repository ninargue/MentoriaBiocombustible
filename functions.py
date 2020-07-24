import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
import pymysql as sql

def detalles_dataframe(dataframe):
    print(f'Dimensión del dataset (filas, columnas): {dataframe.shape}\n')
    print(f'{dataframe.info()}\n')
    return dataframe.head()

def dataframe_desde_querys(tablas, conexion):
    dataframe = pd.concat([pd.read_sql_query(f"SELECT * FROM {tabla};", conexion) for tabla in tablas], ignore_index=True)
    return dataframe

def query_union_to_dataframe_with_chunk(tablas, conexion):
    query = "".join([f'SELECT * FROM {tabla} UNION ' for tabla in tablas])[:-7]
    chunks=[]
    for chunk in pd.read_sql(query, conexion, chunksize = 10000):
        chunks.append(chunk)
    return pd.concat(chunks, ignore_index=True)