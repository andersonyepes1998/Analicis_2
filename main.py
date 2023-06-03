from data.aparatamentos import apartamento1,apartamento2
import pandas as pd
from helpers.crearTablasHTML import crearTabla
from helpers.crearBarras import graficarPromedioSalarial
from helpers.crearTorta import calacularPromedioSalarioPorEdad
#CREAR EL DATAFRAME

tabla1=pd.DataFrame(apartamento1,columns=['edades'])
tabla2=pd.DataFrame(apartamento2,columns=['edades'])
tabla3=pd.read_csv("./data/empleados.csv")

#EFECTUANDO FILTROS CON PYTHON...

#1-NECESITO DEFINIR UNA CONDICON LOGICA...

empleadosJovenesAnalista1=tabla3.query('cargo=="analista1"')
empleadosJovenesAnalista2=tabla3.query('salario<5000000 and cargo=="analista2"')
empleadosAdespedir=tabla3.query('edad>=50')
print(empleadosJovenesAnalista1)
print(empleadosJovenesAnalista2)
print(empleadosAdespedir)

#2-CREAMOS LA TABLA HTMLCON EL DATAFRAME DEL FILTRO...

crearTabla(empleadosJovenesAnalista1,'tablaJovenes')
crearTabla(empleadosJovenesAnalista2,'tablaAnalisis2')
crearTabla(empleadosAdespedir,'tablaJubilados')


#3-Genera Graficas

graficarPromedioSalarial(empleadosAdespedir,'cargo','salario','graficajubilados')
calacularPromedioSalarioPorEdad(empleadosJovenesAnalista2,[20,30,40,50,60],)



