archivo = open("/Users/alan/Dropbox/python_101/pyhton101/10_entrada_salida_archs/paises/paises.txt", "r")

for linea in archivo:
  print(linea.strip())

archivo.close