frase = """
esta es una linea
esta es otra
y otra mas
"""

frase.upper()

long_frase = len(frase)
indice_mitad_frase = long_frase/2
indice_entero = int(indice_mitad_frase)

primer_mitad = frase[0:indice_entero]


primer_mitad = frase[:int(len(frase)/2)]
print(primer_mitad)