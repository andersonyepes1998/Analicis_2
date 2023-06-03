import pandas as pd
import matplotlib.pyplot as plt

def calacularPromedioSalarioPorEdad(dataframe, rangos,columnaInteres, columnaPromediar, nombreGrafica):
    plt.figure()

    #crear una columna nueva por rangos de edad

    dataframe['rangosEdad']=pd.cut(dataframe[columnaInteres],bins=rangos)

    #calcular la suma de los salarios por edad...

    salarioPorRango=dataframe.groupby('rangosEdad')['columnaPromediar'].sum()

    #definimos datos a graficar

    salario=salarioPorRango.values
    rangosEdad=salarioPorRango.index

    plt.pie(salario, labels=rangosEdad, autopct='%1.1f%%')
    plt.title('SALARIOS POR RANGOS DE EDAD')

    plt.savefig(f'./assets/img/{nombreGrafica}.png')
