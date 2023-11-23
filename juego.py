from random import choice, sample

cartas = {
    chr(0x1f0a1): 11,
    chr(0x1f0a2): 2,
    chr(0x1f0a3): 3,
    chr(0x1f0a4): 4,
    chr(0x1f0a5): 5,
    chr(0x1f0a6): 6,
    chr(0x1f0a7): 7,
    chr(0x1f0a8): 8,
    chr(0x1f0a9): 9,
    chr(0x1f0aa): 10,
    chr(0x1f0ab): 10,
    chr(0x1f0ad): 10,
    chr(0x1f0ae): 10,
}

"""
Obtener valor de cada carta y crear una lista de los valores del diccionario (cartas).
"""
lista_cartas = list(cartas)
print("Puntos: {}".format(lista_cartas))

"""
Cartas jugador
"""
print("Has escogido las cartas", end=" ")
carta = choice(lista_cartas)
score = cartas[carta]
print(carta, end=" ")
carta = choice(lista_cartas)
print(carta, end=" ")
score += cartas[carta]
print(">>>>>>> Tu puntuación es:", score )

"""
Cartas banca
"""
banca = sample(lista_cartas, 2)
score_banca = sum(cartas[carta] for carta in banca)
print("La banca escoge:{} {} >>> y su puntuación es {}".format(banca[0], banca[1], score_banca))

"""
Comparar puntuaciones
"""
if score < score_banca:
    print("Banca gana")
elif score > score_banca:
    print("Ganaste!!")
elif score == score_banca:
    print("Habéis igualado puntuación")