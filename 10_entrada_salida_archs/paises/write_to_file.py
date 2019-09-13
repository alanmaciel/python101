archivo = open("/Users/alan/Dropbox/python_101/pyhton101/10_entrada_salida_archs/paises/datos.txt", "w")

while True:
  persona = input("Nombre de la persona: ")
  
  if persona == "salir":
    print("Adios")
    break
  else:
    datos = input("Datos de " + persona + ": ")
    archivo.write( persona + ", " + datos + "\n")

archivo.close()

