import numpy as np #Para los arreglos 
import sklearn
from sklearn.model_selection import train_test_split # Para dividir los datos en sets de entradas y sets de entrenamiento 
from sklearn.neighbors import KNeighborsClassifier

# Para mi compuerta Xor debo crear los arreglos como los espera la clase sklearn
X_aux = [  [0,0],
           [0,1],
           [1,0],
           [1,1]];

Y_aux = [1,0,0,1]


X_train = []
Y_train = []
for i in range(800):
    for j in range(4):
        X_train.append(X_aux[j])
        Y_train.append(Y_aux[j])

# Setemos el numero de vecinos a considerar
Knn = KNeighborsClassifier(n_neighbors = 4)

Knn.fit(X_train,Y_train)

"""
Knn.predict([[1,1]])
array([1])
Knn.predict([[0,0]])
array([1])
Knn.predict([[1,0]])
array([0])
Knn.predict([[0,1]])
array([0])

"""