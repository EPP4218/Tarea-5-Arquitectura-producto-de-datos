"""Preprocesamiento de datos

Script creado con la finalidad de contener funciones relacionadas con el 
preprocesamiento de los datos.  

Este script se puede importar como módulo y contiene la siguiente función:

    * trans_variables_categoricas - regresa el data frame con las variables
    especificadas transformadas a variables categóricas
    
    * codificar_columnas_cat - regresa el data frame con las variables
    categóricas codificadas

    * suma_variables - regresa una columna como resultado de una suma entre
    variables específicadas del data frame

    * mult_variables - regresa una columna como resultado de una multiplicación
    entre variables específicadas del data frame.


"""


#Importar paquetes
from sklearn.preprocessing import OrdinalEncoder
from sklearn.preprocessing import LabelEncoder
import numpy as np

def trans_variables_categoricas(datos_train,datos_test,columna,categorias):
  #Definir categorías
	OE = OrdinalEncoder(categories=[categorias])
  #Aplicar la categorización a las variables especificadas
	for col in columna:
		datos_train[col]=OE.fit_transform(datos_train[[col]])
	 
		datos_test[col]=OE.transform(datos_test[[col]])


encoder = LabelEncoder()
def codificar_columnas_cat(train, test, Level_col):
  #Codificar en variables numéricas las variables categóricas
    for col in Level_col:
        train[col] = encoder.fit_transform(train[col])
        test[col]  = encoder.transform(test[col])


def suma_variables(datos, variables):
  #Definir el vector de suma inicial (cero)
  suma = np.zeros(len(datos))
  #Sumar las variables especificadas
  for i in variables:
    suma = suma+datos[i]
  return(suma)


def mult_variables(datos, variables):
  #Definir el vector de multiplicación inicial (uno)
  mult = np.ones(len(datos))
  #Multiplicar las variables especificadas
  for i in variables:
    mult = mult*datos[i]
  
  return(mult)







