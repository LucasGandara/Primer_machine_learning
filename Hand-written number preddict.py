import sklearn
from sklearn.model_selection import train_test_split # Para dividir los datos en sets de entradas y sets de entrenamiento 
from sklearn.neighbors import KNeighborsClassifier
import io # Con esto se abre los datos de block de notas

# Lectura de archivos de entrenamiento
Archivo_entrenamiento = open("Train_formateado.txt","r") # Leemos el archivo con los datos de entrenamiento
Datos_training = Archivo_entrenamiento.read() # Leemos los datos 
Archivo_entrenamiento.close() # Cerramos el archivo abierto

# Lectura de archivos de testeo
Archivo_testeo = open("Test_formateado.txt","r") # Abrimos el archivo con los datos de testeo
Datos_testeo = Archivo_testeo.read() # Leemos los datos
Archivo_testeo.close() # Cerramos el archivo avierto

""" Para los datos de entrenamiento """
Entradas_training_char = []

print(f"Leyendo datos de entrenamiento... son: {len(Datos_training)}")
for i in range(len(Datos_training)):
    Entradas_training_char.append(float(Datos_training[i]))

del Datos_training 

X_train = []
Y_train = []

contador = 0
conteo_dato = 0

for i in range(1934):
    aux = []
    conteo_dato += 1
    print(f"obteniendo dato de entrenamiento: {conteo_dato}")
    for j in range(1024):
        aux.append(Entradas_training_char[contador])
        contador += 1
    X_train.append(aux)
    Y_train.append(Entradas_training_char[contador])
    contador += 1

""" Pa los datos de testeo  """
Entradas_testing_char = []

print(f"Leyendo datos de testeo... son: {len(Datos_testeo)}")
for i in range(len(Datos_testeo)):
    Entradas_testing_char.append(float(Datos_testeo[i]))

del Datos_testeo
    
X_test = []
Y_test = []

contador = 0
conteo_dato = 0
for i in range(1797):
    aux = []
    conteo_dato += 1
    print(f"Obteniendo dato de entrenamiento: {conteo_dato}")
    for j in range(1024):
        aux.append(Entradas_testing_char[contador])
        contador += 1
    X_test.append(aux)
    Y_test.append(Entradas_testing_char[contador])
    contador += 1

# Seteamos el número de vecinos a considerar
Knn = KNeighborsClassifier(n_neighbors = 10)

# Entrenamos
error = 0.4
contador_epoca = 0
while error >= 0.4:
    contador_epoca += 1
    print(f"Entrenando epoca: {contador_epoca}")
    Knn.fit(X_train,Y_train)
    error = 0.3

Knn.predict([X_test[2]])
Knn.predict([X_train[5]])
Knn.predict([X_test[4]])
Knn.predict([X_test[8]])