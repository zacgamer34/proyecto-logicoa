#apartado importaciones
#apartado funciones
#apartado principal
try:
#datos de entrada
    archivoUsuarios=""
    archivoEventos=""
    archivoMapa=""
    archivoPrecios=""
    datosLogin=""
#datos de salida
#variables adicionales
    datosLoginSeparados=""
    id=""
    nombre=""
    usuariosSeparados=""
    contenido_clientes=""
    nombreArchivo=""
    idArchivo=""
    validacionUsuario=bool
#proceso
    while True:
        #el dato entra
        datosLogin=input("ingrese su nombre y su id[separados por: |]\n: ")
        #se procesa
        datosLoginSeparados=datosLogin.replace(" ","").replace("\t","").replace("\n","").split("|")
        
        nombre=datosLoginSeparados[0]
        id=datosLoginSeparados[1]
        
        
        #abrimos el archivo y lo leemos
        archivoUsuarios=open("recursos/clientes.txt", "r")
        archivoUsuarios.readline()
        validacionUsuario=False
        #entra al ciclo y se separa
        for login in archivoUsuarios:
            contenido_clientes=login.replace("\t","").replace(" ","").replace("\n","").split("|")
            
            nombreArchivo=contenido_clientes[0]
            idArchivo=contenido_clientes[1]
            
            if nombre==nombreArchivo and id==idArchivo:
                print(f"bienvenido:{nombre}")
                validacionUsuario=True
                break
        
        if not validacionUsuario:
            print("usuario o id invalidos")
    
    

except Exception as e:
    print(F"error general del sistema->{e}")

finally:
    archivoUsuarios.close