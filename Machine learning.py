import numpy as np #Para los arreglos 
import sklearn
from sklearn.datasets import load_iris # arreglos de flores de iris
from sklearn.model_selection import train_test_split # Para dividir los datos en sets de entradas y sets de entrenamiento 


iris = load_iris() # Guardamos el set de datos en una variable

# Separamos los datos por entradas de entrenamiento , Entradas de prueba y Salidas esperadas:
X_train, X_test,Y_train, Y_test = train_test_split(iris['data'],iris['target'])

from sklearn.neighbors import KNeighborsClassifier # Clasificador de vecinos cercanos

# Le decimos a nuestro clasificador que considere solamente 7 vecinos cercanos
Knn = KNeighborsClassifier(n_neighbors = 7)

# Se entrena la red con los datos separados
Knn.fit(X_train,Y_train)

# Revisamos que tanto aprendió el algoritmo
Knn.score(X_test,Y_test)

# Para probar, escribe lo siguiente
# Knn.predict([[1.2,3.4,5.6,1.1]])

# Para revisar a que tipo de flor pertenece, escribe lo siguiente
# iris.target_names

