import pandas as pd
import numpy as np

#1. Leer los archivhos csv de empleados y bonificaciones
df_empleados = pd.read_csv('empleados.csv')
df_bonificaciones = pd.read_csv('bonificaciones.csv')

#2. mostrar los datos leidos
print("\nDatos de empleados")
print(df_empleados)
print("\nDatos de bonificaciones")
print(df_bonificaciones)

#3. aplicar funciones personalizadas
#definir funcion para calcular el salario anual
def salario_anual(salario_mensual):
    return salario_mensual * 12

#aplicar la funcion a la columna salario de df_empleados
df_empleados['salario_anual'] = df_empleados['Salario'].apply(salario_anual)
print("\nDatos de empleados con salario anual")
print(df_empleados)

#4. uso de apply() para aplicar funciones mas complejas
#crear una funcion que calcule si un empleado tiene mas de 5 años de antiguedad
def antiguedad_5_anios(fecha_ingreso):
    today = pd.to_datetime('today')
    antiguedad = today - pd.to_datetime(fecha_ingreso)
    return antiguedad.days / 365 > 5
  
#aplicar la funcion a la columna Fecha de Ingreso para crear antiguedad 5 años
df_empleados['antiguedad_5_anios'] = df_empleados['Fecha_Ingreso'].apply(antiguedad_5_anios)

print("\nDatos de empleados con antiguedad 5 años")
print(df_empleados)

#5. crear tablas pivote (pivote tables)
#crear una tabla pivote que muestre el salario promedio por departamento
pivot_departamento = df_empleados.pivot_table(values='Salario', index='Departamento' ,aggfunc='mean')
print("\nTabla pivote de salario promedio por departamento")
print(pivot_departamento)

#6. merge y join para combinar dataframes
#realizar un merge entre los dos dataframes usando la columna 'ID_empleado'
df_completo = pd.merge(df_empleados, df_bonificaciones, on='ID_Empleado', how='left')

print("\ndataset combinado con las bonificaciones de los empleados Merge")
print(df_completo)

#realizar un join con un df diferente usando el indice
#creamos un df adicional de departamento con la informacion de ubicacio
df_departamento = pd.DataFrame({'Departamento': ['Ventas', 'TI', 'Ventas', 'TI'],
                                'Ubicacion': ['Mexico', 'USA', 'Mexico', 'USA']})

#establecer departamento como indice del df de dapartamento
df_departamento.set_index('Departamento', inplace=True)

#realizar un join entre el df de empleados y el de departamento usando la columna departamento
df_join = df_empleados.set_index('Departamento').join(df_departamento)

print("\nDataset de empleados con ubicacion del departamento Join")
print(df_join)