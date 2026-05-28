def letrasNumeros(a):
    
    if a.count("A")==1:
        return 0
    elif a.count("B")==1:
        return 1
    elif a.count("C")==1:
        return 2
    elif a.count("D")==1:
        return 3
    elif a.count("E")==1:
        return 4
    elif a.count("F")==1:
        return 5
    elif a.count("G")==1:
        return 6
    elif a.count("H")==1:
        return 7
    elif a.count("I")==1:
        return 8
    elif a.count("J")==1:
        return 9
a=""
numeros=0
a=input("Elija el asiento").upper()
letras=letrasNumeros(a)
print(letras)
numeros=a.replace("A","").replace("B","").replace("C","").replace("D","").replace("E","").replace("F","").replace("G","").replace("H","").replace("I","").replace("J","")
print(numeros)
numeros=int(numeros)
# Abrir el archivo y leer su contenido
with open("recursos\mapa_evento[EVT-1002].txt","r") as archivo:
    # Leer todas las líneas y eliminar saltos de línea
    lineas = archivo.readlines()

# Convertir cada línea en una lista de enteros
matriz = [list(map(str,linea.strip().split(','))) for linea in lineas]

# Mostrar la matriz
for fila in matriz:
    print(fila)
if matriz[letras][numeros-1]=="X":
    print("Asiento ocupado, elija otro. ")
                
else:
    pass





matriz[letras][numeros-1]="X"
for fila in matriz:
    print(fila)
with open("recursos/mapa_evento[EVT-1002].txt", "w") as archivo:
    for fila in matriz:
        # Convertir cada elemento a string y unirlos con comas
        linea = ",".join(map(str, fila))
        archivo.write(linea + "\n")
