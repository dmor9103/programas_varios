#   1.  Un corredor de maratón (distancia 42,195 Km) ha recorrido la carrera en 2 horas 25 minutos.
#       Se desea un algoritmo que calcule el tiempo medio en minutos por kilómetro.
#   42195 km se recorren en 2 horas con 25 minutos
#   Determinar cuantos minutos son 2h25m
min = int((2 * 60) + 25)
metros = int(42195 / min)
print("se recorre " + str(metros) + " por minuto")
