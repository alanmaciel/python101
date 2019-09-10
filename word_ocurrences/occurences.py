def limpia_puntuacion(palabra, puntuacion):
    palabra_limpia = ""
    if puntuacion in palabra:
        for l in palabra:
            if not l == puntuacion:
                palabra_limpia += l
    
    else:
        palabra_limpia = palabra
    return palabra_limpia

def limpia_palabra(palabra):
        palabra = palabra.strip()
        palabra = limpia_puntuacion(palabra, ",")
        palabra = limpia_puntuacion(palabra, ".")
        palabra = limpia_puntuacion(palabra, ":")
        palabra = limpia_puntuacion(palabra, "?")
        palabra = limpia_puntuacion(palabra, "!")
        palabra = limpia_puntuacion(palabra, "'")
        palabra = limpia_puntuacion(palabra, "\"")
        palabra = limpia_puntuacion(palabra, ")")
        palabra = limpia_puntuacion(palabra, "(")
        palabra = limpia_puntuacion(palabra, "]")
        palabra = limpia_puntuacion(palabra, "[")
        palabra = palabra.lower()
        return palabra

archivo = open("/Users/alan/Desktop/pg8300.txt","r")
contador_dict = {}

for linea in archivo:
    palabras = linea.split(" ")

    for palabra in palabras:
        palabra = limpia_palabra(palabra) 

        if palabra in contador_dict.keys() and palabra != "":
            contador_dict[palabra] += 1
        else:
            contador_dict[palabra] = 1

archivo.close()

contador_dict = [(k, contador_dict[k]) for k in sorted(contador_dict, key=contador_dict.get, reverse=True)]

for key, value in contador_dict:
    print(key + " = " + str(value))

print("Palabras únicas encontradas: " + str(len(contador_dict)))