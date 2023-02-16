"""Limpieza de datos

Script creado con la finalidad de contener funciones relacionadas con la 
limpieza de los datos.  

Este script se puede importar como módulo y contiene la siguiente función:

    * llenado_datos_faltantes - regresa la tabla con los datos faltantes
    llenos de la columna seleccionada.
    
    * llenado_todos_datos_faltantes - regresa la tabla con todos los datos
    faltantes llenos.

    * quitar_columnas - regresa los datos sin las columnas seleccionadas 


"""


#Importar paquetes
import pandas as pd

def llenado_datos_faltantes(datos, variables, valor):
  #For para llenar los datos faltantes de las columnas seleccionadas
  for col in variables:
    datos[col].fillna(valor, inplace=True)


def llenado_todos_datos_faltantes(datos):
  #For para llenar todos los datos faltantes según el tipo de variable
  for col in datos.columns:
      if((datos[col].dtype == 'float64') or (datos[col].dtype == 'int64')):
        datos[col].fillna(datos[col].mean(), inplace=True)
      else:
        datos[col].fillna(datos[col].mode()[0], inplace=True)


def quitar_columnas(datos, columnas):
  #Quitar colummnas definidas
  datos.drop(columnas, axis = 1, inplace=True)

  