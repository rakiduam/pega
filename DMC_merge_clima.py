import pandas as pd
import numpy as np
import geopandas as gpd
import os
from glob import glob
import datetime

entDIR = os.environ['ONEDRIVE'] + '\\AGROCLIMA_COMPARTIDO\\CNR\\CLIMA\\DMC\\DESORDENADO\\'
outDIR = os.environ['ONEDRIVE'] + '\\AGROCLIMA_COMPARTIDO\\CNR\\CLIMA\\DMC\\ORDENADO\\'

os.chdir(entDIR)

archivos_xls = None
archivos_xls = glob(entDIR + '*.xls*')
archivos_xls.sort()

nombres = None
nombres = list(set([(nom.split('\\')[-1]).split('_')[0] for nom in archivos_xls]))

dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')

#fechas = pd.datetime(start='1980-01-01', end='2020-01-01')

tx, tn, tm, hr, pp, et, rs = None, None, None, None, None, None, None
tx = pd.DataFrame(index=pd.date_range(start='1980/01/01',end='2021/01/01',freq='d',closed='left'), columns=nombres)
tn = pd.DataFrame(index=pd.date_range(start='1980/01/01',end='2021/01/01',freq='d',closed='left'), columns=nombres)

libros_xls = []

for count, archivo in enumerate(nombres):
    print(archivo)
    libros_xls = [pd.read_excel(xls, index_col=1) for xls in glob(entDIR + archivo + '*.xlsx')]
    for count, i in enumerate(libros_xls):
        if count == 0:
            aa = i
        else:
            aa = aa.append(i)
    aa = aa.sort_index()
    aa = aa.iloc[:,1:]
    aa.to_excel(outDIR+archivo+'.xlsx', sheet_name=archivo, freeze_panes=[1,1])
    aa = None





#%%

    for hoja in libros_xls:
        #print(hoja)


libros_xls[1].columns


        df_leido = pd.read_excel(archivo)
        df_leido = df_leido.apply(pd.to_numeric)


