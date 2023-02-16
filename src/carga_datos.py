
"""Lectura de datos

Script creado con la finalidad de contener funciones relacionadas con la 
descarga de datos en csv ya sean de entrenamiento o de prueba. 

Este script se puede importar como módulo y contiene la siguiente función:

    *obtener_datos - regresa la tabla descargada de un csv

"""


#Importar paquetes 
import pandas as pd
import os



def obtener_datos(str):
  '''Descargar tabla de la información de una base de datos en csv.

  Params:
    str (str): Nombre si es una base de entrenamiento (train) o prueba (test)

  Returns:
    Un dataframe con la infromación de la tabla descargada
  '''
 
  #Desarga de datos dependiendo si son los datos de entrenamiento o de prueba
  absolute_path = os.path.abspath('')
  if str == "train":
      data = pd.read_csv( os.path.join(absolute_path, "data/train.csv"))
  elif str == "test":
      data = pd.read_csv(os.path.join(absolute_path, "data/test.csv"))
  else: 
      data = "No valido: Poner test o train"
  return data
