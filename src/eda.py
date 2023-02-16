
"""Análisis exploratorio de datos

Script creado con la finalidad de contener funciones relacionadas con el 
análisis exploratorio de datos (realización de gráficas).  

Este script se puede importar como módulo y contiene la siguiente función:

    * grafica_na - regresa una gráfica de calor para conocer los valores nulos 
    cada variable
    
    * grafica_barras - regresa una gráfica de barras para conocer el número de 
    observaciones para cada categoría de una variable

    * grafica_histograma - regresa un histograma para conocer la distribución de
    una variable continua. 

    * grafica_violin - regresa un gráfico de violines para conocer la relación
    entre una distribución continua y una categórica.

    * grafica_dispersion - regresa un gráfico de dispersión para conocer la 
    relación de dos variables continuas.

"""



#Improtar paquetes
import seaborn as sns
from matplotlib import pyplot as plt
import warnings


def grafica_na(datos):
  #Definir tamaño de la gráfica
	fig, ax = plt.subplots(figsize=(25,10))
  #Graficar observaciones nulas por variables
	sns.heatmap(data=datos.isnull(), yticklabels = False, ax=ax)
  

def grafica_barras(variable):
  #Definir tamaño de la gráfica
  fig, ax = plt.subplots(figsize=(25,10))
  #Hacer gráfica de barras
  sns.countplot(x = variable)
  #Colocar malla en la gráfica
  plt.grid()
  #Escribir título en la gráfica
  plt.title("Gráfica de barras", fontsize=30)
  #Imprimir gráfica
  plt.show()


def grafica_histograma(variable):
  #Definir tamaño de la gráfica
  fig, ax = plt.subplots(figsize=(25,10))
  #Graficar histograma
  sns.histplot(x = variable, kde=True, ax=ax )
  #Colocar malla en la gráfica
  plt.grid()
  #Escribir título en la gráfica
  plt.title("Histograma", fontsize=30)
  #Imprimir gráfica
  plt.show()


def grafica_violin(variable1,variable2):
  #Definir tamaño de la gráfica
  fig, ax = plt.subplots(figsize=(25,10))
  #Hacer gráfica de violines
  sns.violinplot(x=variable1,y=variable2,ax=ax)
  #Colocar malla en la gráfica
  plt.grid()
  #Escribir título en la gráfica
  plt.title("Gráfica de violines", fontsize=30)
  #Imprimir gráfica
  plt.show()

def grafica_dispersion(variable1,variable2):
  #Definir tamaño de la gráfica
  fig, ax = plt.subplots(figsize=(25,10))
  #Hacer gráfico de dispersión
  sns.scatterplot(x=variable1,y=variable2,palette='deep')
  #Colocar malla en la gráfica
  plt.grid()
  #Escribir título en la gráfica
  plt.title("Gráfico de dispersión", fontsize=30)
  #Imprimir gráfica
  plt.show()