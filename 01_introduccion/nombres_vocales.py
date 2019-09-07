nombres = ['ana', 'veronica', 'hugo', 'paco', 'luis', 'oscar']

nombres_con_vocales = []

for nombre in nombres:
    if nombre[0] in ["a", "e", "i", "o", "u"]:
        nombres_con_vocales.append(nombre)

print(nombres_con_vocales)