#!/usr/local/bin/python
# -*- coding: utf-8 -*-

capitales_dict = {
    "Aguascalientes" : "Aguascalientes",
    "Baja California" : "Mexicali",
    "Baja California Sur" : "La Paz",
    "Campeche" : "Campeche",
    "Chihuahua" : "Chihuahua",
    "Chiapas" : "Tuxtla Gutiérrez",
    "Coahuila" : "Saltillo",
    "Colima" : "Colima",
    "Durango" : "Victoria",
    "Guanajuato" : "Guanajuato",
    "Guerrero" : "Chilpancingo",
    "Hidalgo" : "Pachuca",
    "Jalisco" : "Guadalajara",
    "México" : "Toluca",
    "Michoacán" : "Morelia",
    "Morelos" : "Cuernavaca",
    "Nayarit" : "Tepic",
    "Nuevo León" : "Monterrey",
    "Oaxaca" : "Oaxaca",
    "Puebla" : "Puebla",
    "Querétaro" : "Querétaro",
    "Quintana Roo" : "Chetumal",
    "San Luis Potosí" : "San Luis Potosí",
    "Sinaloa" : "Culiacán",
    "Sonora" : "Hermosillo",
    "Tabasco" : "Villahermosa",
    "Tamaulipas" : "Ciudad Victoria",
    "Tlaxcala" : "Tlaxcala",
    "Veracruz" : "Xalapa",
    "Yucatán" : "Mérida",
    "Zacatecas" : "Zacatecas"
}

import random

estados = list(capitales_dict.keys())
#for i in [1,2,3,4,5]:

while True:
    estado = random.choice(estados)
    capital = capitales_dict[estado]
    respuesta = input("Cual es la capital de " + estado + "? ")

    if respuesta == "salir":
        break
    elif respuesta == capital:
        print("Respuesta correcta! " + "\N{Sports Medal}") 
    else:
        print("Respuesta incorrecta. La capital de " + estado + " es " + capital + "\N{grinning face}" + ".")

print("Adios")