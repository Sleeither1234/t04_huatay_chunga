# CALCULO DE LA ALTURA DE UN EDIFICIO
velocidad_inicial,tiempo,gravedad=0.0,0.0,0.0

# ASIGANACION DE VALORES
velocidad_inicial=34
tiempo=6
gravedad=9.18

# CALCULO
haltura=velocidad_inicial*tiempo+(gravedad*(tiempo**2))/2

# MOSTRAR VALORES
print("La velocidad inicial del objeto es: "+str(velocidad_inicial))
print("El tiempo de caida del objeto es: "+str(tiempo))
print("La gravedad con la que cae el objeto es: "+str(gravedad))
print("La altura del edificio es: "+str(haltura))
