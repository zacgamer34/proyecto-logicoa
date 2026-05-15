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
    selecionEvento=""
    eventoselecionado=""
    datosEvento=""
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
    eventos=""
#proceso
    
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
    
    
    selecionEvento=input("desea ver la lista de eventos\nsi \nno").upper()
    
    if selecionEvento=="SI":
        archivoEventos=open("recursos/eventos.txt", "r")
        
        eventos=archivoEventos.read()
    
    print(eventos)
    while True:
        eventoselecionado=input(f"a que evento desea registrarse :{nombre}\n las opciones. pueden ser numeradas de [1-3]en el orden mostrado en pantalla\nseleccion: ")
        if 1<=eventoselecionado <=3:
            eventoselecionado=int(eventoselecionado)
            break
        else:
            print("fuera de rango disponible porfavor vuelva a intentarlos")
            
        
        if eventos==1:
            datosEvento=open()
            

except Exception as e:
    print(F"error general del sistema->{e}")

finally:
    archivoUsuarios.close
    archivoEventos.close