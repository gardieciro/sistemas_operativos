ganados = int(input("ingresa el número de partidos ganados: "))
empatados = int(input("ingresa el número de partidos empatados: "))
perdidos = int(input("ingresa el número de partidos perdidos: "))
puntaje = (ganados * 3) + (empatados * 1) + (perdidos * 0)
print()
print("El puntaje total del Club ABC es: ",puntaje)