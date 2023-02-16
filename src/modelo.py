"""Modelo

Script creado con la finalidad de contener funciones relacionadas con el modelo
que se evalúa.  

Este script se puede importar como módulo y contiene la siguiente función:

    * modelo_bosques_aleatorios - regresa un modelo de regresión basado en 
    bosques aleatorios. 
    
    * ajuste_modelo_bosques_aleatorio - regresa el ajuste del modelo de 
    regresión

    * metrica - regresa el valor de la métrica de la suma del cuadrado de 
    los residuales.

    * estimacion - regresa e imprime una tabla con los resultados de las
    estimaciones.


"""


#Importar paquetes
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
import numpy as np
import pandas as pd

def modelo_bosques_aleatorios(nodos_maximos):
  #Definir modelo de regresión
	modelo = RandomForestRegressor(max_leaf_nodes=nodos_maximos,)
	return(modelo)


def ajuste_modelo_bosques_aleatorio(datos_train, modelo, variable_y):
  #Definir variable dependiente y datos de entrenamiento.
	y = datos_train[variable_y]
	X = datos_train.drop([variable_y], axis = 1)
  #Ajustar el modelo
	fit = modelo.fit(X,y)
	return(fit)

def metrica(modelo,datos_train, variable_y):
  #Definir variable dependiente y datos de entrenamiento.
	y = datos_train[variable_y]
	X = datos_train.drop([variable_y], axis = 1)
  #Calcular la métrica a evaluar
	score = cross_val_score(modelo, X, y, cv=10)
	return(score.mean())	


def estimacion(modelo, datos_test, ids):
  #Obtener las predicciones del modelo 
  precio = modelo.predict(datos_test)
  #Crear una tabla con los resultados
  submission = pd.DataFrame({
    "Id": ids,
    "precio_venta": precio})
  #Imprimir la tabla en csv
  submission.to_csv("Resultados/estimaciones_precios.csv")

  return(submission)


	

	

	
