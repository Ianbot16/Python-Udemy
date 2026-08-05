"""
Ejercicio 5:
Crear una lista con el contenido de esta tabla:
Accion           Aventura    Deportes           Estrategia
GTA               Zelda       FIFA             Age of Empires
Metroid Prime     Mario       Need for Speed     Starcraft
Pubg              Crash       PES               Command and Conquer

Mostrar está información ordenada

"""

tabla=[
    {
        "Categoria":"Accion",
        "Juegos":["GTA","Metroid Prime","Pubg"]
    },
    {
        "Categoria":"Aventura",
        "Juegos":["Zelda","Mario","Crash"]
    },
    {
        "Categoria":"Deportes",
        "Juegos":["FIFA","Need for Speed","PES"]
    },
    {
        "Categoria":"Estrategia",
        "Juegos":["Age of Empires","Starcraft","Command and Conquer"]
    }
]

for categoria in tabla:
    print(f"------------{categoria['Categoria']}------------")
    for juego in categoria["Juegos"]:
        print(juego)