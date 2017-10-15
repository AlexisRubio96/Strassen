import csv
#***********************************************************************************************************************
# Se trabaja con la primer matriz --> Matriz_A_16_2_4.csv
#***********************************************************************************************************************

with open('Matriz_A_16_2_4.csv','r') as archivo:

# Lectura de archivo
# Se abre el archivo
    r = csv.reader(archivo)

# Se lee el archivo completo para conocer la dimension de la matriz
# Se crea la matriz
# Esto se puede optimizar si solo se lee la primer linea, debido a que la matriz es
# cuadrada conociendo el len() del primer renglon podemos saber cuantos renglones y columnas necesitamos
    for x in r:
        matrizA = []
        for i in range(len(x)):
            matrizA.append([])
            for j in range(len(x)):
                matrizA[i].append(None)


archivo.close

# Matriz vacia
print matrizA

# Longitud de la matriz nxn = longitud
# Esta longitud sirve para las dos matrices que se multiplicaran
longitud = len(matrizA[0])

# Se vuelve a abrir el archivo para llenar la matriz
with open('Matriz_A_16_2_4.csv','r') as archivo:
    r = csv.reader(archivo)
    i = 0

    # Se llena la matriz A
    for x in r:
        for j in range(longitud):
            matrizA[i][j] = int(x[j])
        i+=1

archivo.close
# Matriz llena
print matrizA

# Se crea la matriz B, tiene la misma dimension que la matriz A, solo hay que cambiar valores
matrizB = matrizA


#***********************************************************************************************************************
# Se trabaja con la segunda matriz --> Matriz_B_16_2_4.csv
#***********************************************************************************************************************

with open('Matriz_B_16_2_4.csv','r') as archivo:
    r = csv.reader(archivo)
    i = 0

    # Se llena la matriz B
    for x in r:
        for j in range(longitud):
            matrizB[i][j] = int(x[j])
        i+=1

# Se tienen listas las matrices a multiplicas --> matrizA y matrizB
print matrizB

# Se crea la matriz C, tiene la misma dimension que la matriz A, matriz B. La matriz C es nuestra matriz resultante
matrizC = matrizB

for i in range(longitud):
    for j in range(longitud):
        for k in range(longitud):
            matrizC[i][k] = matrizC[i][k] + (matrizA[i][j] * matrizB[j][k])


print matrizC