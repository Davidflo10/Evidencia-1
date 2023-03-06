identificador= {}
while True:
    print("************ BIBLIOTECA X ************")
    print("             BIENVENIDO   ")
    print("este es el menu de la biblioteca X elige una de las siguientes opciones para continuar")
    print("[1] Registra un nuevo ejemplar :")
    print("[2] ver las consultas y los reportes : ")
    print("[X] salir de el menu de la biblioteca : ")
    
    eleccion=input("indique su eleccion:  ").upper()
    if eleccion == "1" :
         titulo=input("ingresa el nombre del libro:  ")
         autor=input("ingresa el nombre del autor:  ")
         genero=input("ingresa el genero del libro:   ")
         año_pub=input("ingresa el año de publicacion del libro:  ")
         isbn=input(f"ingresa el isbn de {titulo}:  ")
         fech_adq=input("ingresa la fecha de adquisicion(dd/mm/aaaa):  ") 
         if identificador :
             id1 = max(identificador) +1
         else:
             id1 = 1
         identificador[id1] = [id1,titulo,autor,genero,año_pub,isbn,fech_adq]
         print("*********ingreso generado exitosamente*********")
    elif eleccion == "2" :
        while True:
            print("*****CONSULTAS Y REPORTES*****")
            elecc=input("ELIGA UNA DE LAS SIG. OPCIONES, [1] PARA CONSULTA DE TITULO, [2] PARA REPORTES Y [X] PARA VOLVER AL MENU DE CONSULTAS Y REPORTES")
            if elecc == "1" :
                elecc_1=input("COMO DESEAS BUSCAR EL LIBRO, [1] POR TITULO, [2] POR ISBN , O DESEAS VOLVER AL MENU DE CONSULTAS Y REPORTES").upper()
                if elecc_1 == "1" :
                    print("*********************")
                    print(f"ID\tTITULO")
                    print("*********************")
                    for id1,titulo,autor,genero,año_pub,isbn,fecha_adq in identificador.values():
                        print(f"{id1:4} |{titulo:30}")
                    else:
                        print("*********************")
                        titulo_consulta=input("ingresa el nombre del titulo para consultar todos los datos del titulo ingresado  ")
                        print("*********************")
                        print(f"ID\tTITULO\t\t\tAUTOR\t\tGENERO\t\tAÑO DE PUBLICACION\tISBN\t\tFECHA DE ADQUISICIÓN")
                        for id1,titulo,autor,genero,año_pub,isbn,fecha_ad in identificador.values():
                            if titulo==titulo_consulta:
                                print(f"{id1:3}|{titulo:20}|{autor:20}|{genero:20}|{año_pub:20}|{isbn:20}|{fecha_adq:15}")
                        else:
                            print("*********************")
                if elecc_1 == "2" :
                    print("*****************")
                    print(f"ID\tISBN")
                    print("******************")
                    for id1,titulo,autor,genero,año_pub,isbn,fecha_adq in identificador.values():
                        print(f"{id1:3} | {isbn}")
                    else:
                        print("*****************")
                        isbn_consulta=input("ingresa el isbn para consultar los titulos: ")
                        print("*********************")
                        print(f"ID\tTITULO\t\t\tAUTOR\t\tGENERO\t\tAÑO DE PUBLICACION\tISBN\t\tFECHA DE ADQUISICIÓN")
                        for id1,titulo,autor,genero,año_pub,isbn,fecha_adq in identificador.values():
                            if isbn==isbn_consulta:
                                print(f"{id1:3}|{titulo:20}|{autor:20}|{genero:20}|{año_pub:20}|{isbn:20}|{fecha_adq:15}")
                            else:
                                print("********************")
                if elecc_1 == "x" :
                    break
            if elecc == "2" :
                while True:
                    print("**************************************")
                    print("*****************REPORTES*********************")
                    print("**************************************")
                    elecc_2=input("[1]catalago completo\n[2]reporte por autor\n[3]reporte por género\n[4]por año de publicación\n[5]Volver al menú de reportes\nindique la opcion deseada: ")
                    print("")

                    if elecc_2=="1":
                        print("***************************************")
                        print(f"ID\tTITULO\t\t\tAUTOR\t\tGENERO\t\tAÑO DE PUBLICACION\tISBN\t\tFECHA DE ADQUISICIÓN")
                        print("****************************************")
                        for id1,titulo,autor,genero,año_pub,isbn,fecha_adq in identificador.values():
                            print(f"{id1:3}|{titulo:20}|{autor:20}|{genero:20}|{año_pub:20}|{isbn:20}|{fecha_adq}")
                        else:
                            print("*****************************************")

                    if elecc_2 == "2" :
                        print("***************************")
                        print(f"ID\tAUTOR")
                        print("***************************")
                        for id1,titulo,autor,genero,año_pub,isbn,fecha_adq in identificador.values():
                            print(f"{id1:3}|{autor}")
                        else:
                            print("***************************")
                        autor_opcion=input(f"elija un autor para ver sus respectivos libros: ")
                        print("************************************************************************************")
                        print(f"ID\tTITULO\t\t\tAUTOR\t\tGENERO\t\tAÑO DE PUBLICACION\tISBN\t\tFECHA DE ADQUISICIÓN")
                        print("************************************************************************************")
                        for id1,titulo,autor,genero,año_pub,isbn,fecha_adq in identificador.values():
                            if autor==autor_opcion:
                                print(f"{id1:3}|{titulo:20}|{autor:20}|{genero:20}|{año_pub:20}|{isbn:20}|{fecha_adq}")
                        else:
                            print("************************************************************************************")

                    if elecc_2 == "3" :
                        print("**********************************")
                        print(f"ID\tGENERO")
                        print("**********************************")
                        for id1,titulo,autor,genero,año_pub,isbn,fecha_adq in identificador.values():
                            print(f"{id1:3}|{genero}")
                        else:
                            print("**********************************")
                        genero_opcion=input("Elija un genero para mostrar todas los ejemplares existentes: ")
                        print("**********************************")
                        print(f"ID\tTITULO\t\t\tAUTOR\t\tGENERO\t\tAÑO DE PUBLICACION\tISBN\t\tFECHA DE ADQUISICIÓN")
                        print("**********************************")
                        for id1,titulo,autor,genero,año_pub,isbn,fecha_adq in identificador.values():
                            if genero==genero_opcion:
                                print(f"{id1:3}|{titulo:20}|{autor:20}|{genero:20}|{año_pub:20}|{isbn:20}|{fecha_adq}")
                        else:
                            print("**********************************")
                    if elecc_2 == "4" :
                        print("**********************************")
                        print(f"ID\tAÑO_PUB")
                        print("**********************************")
                        for id1,titulo,autor,genero,año_pub,isbn,fecha_adq in identificador.values():
                            print(f"{id1:3}|{año_pub}")
                        else:
                            print("**********************************")
                        año_opcion=input(f"Elija el año de publicacion  para mostrar todas los ejemplares existentes: ")
                        print("**********************************")
                        print(f"ID\tTITULO\t\t\tAUTOR\t\tGENERO\t\tAÑO DE PUBLICACION\tISBN\t\tFECHA DE ADQUISICIÓN")
                        print("**********************************")
                        for id1,titulo,autor,genero,año_pub,isbn,fecha_adq in identificador.values():
                            if año_pub==año_opcion:
                                print(f"{id1:3}|{titulo:20}|{autor:20}|{genero:20}|{año_pub:20}|{isbn:20}|{fecha_adq}")
                        else:
                            print("**********************************")
                    if elecc_2 == "5" :
                        break
                if elecc == "x" :
                    break
            
                    
                        

                    



                            
                 
                 



    elif eleccion == "x".upper() :
        print("SYSTEM OFF")
        break
         
         


   