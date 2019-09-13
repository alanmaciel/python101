archivo = open("/Users/alan/Dropbox/python_101/pyhton101/10_entrada_salida_archs/paises/paises.txt", "r")

paises = []

for linea in archivo:
  paises.append(linea)

archivo.close()

print(paises)
print(len(paises))

for pais in paises:
  if pais[0] == "M":
    print(pais)

