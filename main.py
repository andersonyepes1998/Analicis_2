from data.aparatamentos import apartamento1,apartamento2
import pandas as pd
#CREAR EL DATAFRAME

tabla1=pd.DataFrame(apartamento1,columns=['edades'])
tabla2=pd.DataFrame(apartamento2,columns=['edades'])
tabla3=pd.read_csv("./data/empleados.csv")

print(tabla1)
print(tabla2)

estadisticasAPTO1=tabla1.describe()
estadisticasAPTO2=tabla2.describe()
estadisticasEmpleados=tabla3.describe()

print(estadisticasAPTO1)
print("\n")
print(estadisticasAPTO2)
print("\n")
print(estadisticasEmpleados)