import io

Archivo = open("Test.txt","r")
Datos = Archivo.read()
Archivo.close

Entradas_char = []

#Creamos un bucle para pasar los datos de string a char
for i in range(len(Datos)):
    Entradas_char.append(Datos[i])

# Eliminamos los saltos de linea
num_saltos = Entradas_char.count("\n")
conteo_saltos = 0
for i in range(num_saltos):
    conteo_saltos += 1
    Entradas_char.remove("\n")
    print(f"Borrando Saltos de linea: {conteo_saltos} de:{num_saltos}")

# Eliminamos los espacios en blanmco
num_blancos = Entradas_char.count(" ")
conteo_blancos = 0
for i in range(num_blancos):
    conteo_blancos += 1
    Entradas_char.remove(" ")
    print(f"BOrrando espacios en blanco: {conteo_blancos} de: {num_blancos}")