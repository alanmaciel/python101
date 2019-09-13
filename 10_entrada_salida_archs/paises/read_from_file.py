archivo = open("/Users/alan/Dropbox/python_101/pyhton101/10_entrada_salida_archs/paises/paises.txt", "r")

personas = {}

for linea in archivo:
  print(linea.split(","))
  #print(line.strip().split(","))


archivo.close()

# ===================

for line in archivo:
  registro = linea.strip();