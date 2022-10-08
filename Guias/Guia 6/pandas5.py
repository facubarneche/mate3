"""
5. El archivo comercio_interno.csv contiene información sobre el comercio interno desde la década del 90. Escribe un programa que:
a. Muestre por pantalla las dimensiones del Data Frame, el número de datos que contiene, los nombres de sus columnas y filas, los tipos de datos de las columnas, las 10 primeras filas y las 10 últimas filas.
b. Muestre por pantalla un gráfico de los datos de empleo por provincia y su relación con la columna valor.
c. Muestre por pantalla la columna alcance_nombre ordenada alfabéticamente.
d. Muestre un gráfico de la actividad_producto_nombre agrupados en relación al valor
e. Sume por alcance_nombre los valores de los años 2009 al 2019
f. Muestre un gráfico de la actividad_producto_nombre en la provincia de Mendoza del año 2015 al 2019
"""
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def main():

    datos = pd.read_csv('Clases/Unsam.Clase.6/dataset/14.comercio_interno.csv', encoding='latin-1')
    df = pd.DataFrame(datos)

    #Punto A

    #Funcion que devuelve la dimension del DataFrame
    def dimension(param):
        return param.ndim
    #FinDef

    #Funcion que devuelve la cantidad de elementos del DataFrame
    def dataSize(param):
        return param.size
    #FinDef

    #Funcion axes devuelve la lista de etiquetas de eje de fila y etiquetas de eje de columna.
    def labelAxes(param):
        return param.axes
    #FinDef

    #Funcion que devuelve los tipos de datos de las columnas
    def columnTypes(param):
        return param.dtypes
    #FinDef

    #Funcion que devuelve las primeras n filas (en este caso queremos 10, pero se pueden cambiar)
    def firstRows(param, n):
        return param.head(n)
    #FinDef

    #Funcion que devuelve las ultimas n filas (en este caso queremos 10, pero se pueden cambiar)
    def lastRows(param, n):
        return param.tail(n)
    #FinDef

    #Impresiones
    df_dim = dimension(df)
    print(f'La dimension del Data Frame es de: {df_dim}')

    df_size = dataSize(df)
    print(f'El numero de datos que contiene es: {df_size} elementos')

    # RangeIndex son las filas (son numericas paso a paso, de a 1) y las filas = index
    df_axes = labelAxes(df)
    print(f'Los nombres de sus columnas y filas son: \n {df_axes}')

    df_types = columnTypes(df)
    print(f'Tipo de datos de las columnas: \n {df_types}')

    df_first = firstRows(df, 10)
    print(f'Las primeras 10 filas son: \n {df_first}')

    df_last = lastRows(df, 10)
    print(f'Las ultimas 10 filas son: \n {df_last}')


    #Punto B

    #Borramos datos que no sirven
    df = df.drop(df[df['alcance_nombre'] == 'Argentina'].index)
    df = df.drop(df[df['alcance_nombre'] == 'GRAN BUENOS AIRES'].index)
    df = df.drop(df[df['alcance_nombre'] == 'INDETERMINADA'].index)
    df = df.drop(df[df['alcance_nombre'] == 'PARTIDOS DEL GBA'].index)
    df = df.drop(df[df['alcance_nombre'] == 'RESTO DE BUENOS AIRES'].index)

    df = df.drop(['sector_id','sector_nombre','variable_id','indicador','unidad_de_medida','fuente','frecuencia_nombre',
'cobertura_nombre','alcance_id'], axis=1)
    
    #Configuraciones para el grafico torta
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    df.groupby('alcance_nombre')['valor'].sum().plot(kind='pie',
    legend='Reverse',
    autopct='%0.2f %%',
    fontsize=6,
    labels=None,
    pctdistance=1.10
    )
    plt.axis('equal')
    plt.ylabel('')
    plt.tight_layout()
    plt.title('Comercio interno por\nProvincias y CABA\n de 2010 a 2019', weight='bold', size=14)
    plt.show()

    #Punto C

    print('\nMuestre por pantalla la columna alcance_nombre ordenada alfabéticamente.\n')
    orderProvince = df.sort_values('alcance_nombre')
    print(orderProvince)

    #Punto D
    print('\nMuestre un gráfico de la actividad_producto_nombre agrupados en relación al valor\n')

    #Configuraciones para el grafico torta
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    df.groupby('actividad_producto_nombre')['valor'].sum().plot(kind='pie',
    legend='Reverse',
    autopct='%0.2f %%',
    fontsize=6,
    labels=None,
    pctdistance=1.10
    )
    plt.axis('equal')
    plt.ylabel('')
    plt.tight_layout()
    plt.title('Comercio interno por\actividad_producto_nombre\n', weight='bold', size=14)
    plt.show()

    #Punto E

    print('\nSume por alcance_nombre los valores de los años 2009 al 2019\n')
    
    df['indice_tiempo'] = pd.to_datetime(df['indice_tiempo'], format='%d/%m/%Y')
    df['año'], df['mes'] = df['indice_tiempo'].dt.year, df['indice_tiempo'].dt.month
    df2 = df.drop(df[df['año'] < 2009].index)
    print(df2['alcance_nombre'])

    #Configuraciones para el grafico torta
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    df2.groupby('alcance_nombre')['valor'].sum().plot(kind='pie',
    legend='Reverse',
    autopct='%0.2f %%',
    fontsize=6,
    labels=None,
    pctdistance=1.10
    )
    plt.axis('equal')
    plt.ylabel('')
    plt.tight_layout()
    plt.title('Sume por alcance_nombre los valores de los años 2009 al 2019\n', weight='bold', size=14)
    plt.show()

    #Punto F
    print('\nMuestre un gráfico de la actividad_producto_nombre en la provincia de Mendoza del año 2015 al 2019\n')
    
    df['indice_tiempo'] = pd.to_datetime(df['indice_tiempo'], format='%d/%m/%Y')
    df['año'], df['mes'] = df['indice_tiempo'].dt.year, df['indice_tiempo'].dt.month
    df3 = df.drop(df[df['año'] < 2015].index)

    #Configuraciones para el grafico torta
    fig = plt.figure(figsize=(8,8))
    ax = fig.add_subplot(111)
    df3.groupby('actividad_producto_nombre')['valor'].sum().plot(kind='pie',
    legend='Reverse',
    autopct='%0.2f %%',
    fontsize=6,
    labels=None,
    pctdistance=1.10
    )
    plt.axis('equal')
    plt.ylabel('')
    plt.tight_layout()
    plt.title('actividad_producto_nombre en la provincia de Mendoza del año 2015 al 2019\n', weight='bold', size=14)
    plt.show()

if __name__ == '__main__':
    main()
