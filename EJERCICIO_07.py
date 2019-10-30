# CALCULO DE LA VELOCIDAD FINAL
velocidad_inicial_1,gravedad_1,ALTURA=0.0,0.0,0.0

# ASIGNACION DE VALORES
velocidad_inicial_1=56.3
gravedad_1=9.78
ALTURA=54

# CALCULO
import  math
velocidad_final=math.sqrt((velocidad_inicial_1**2)+2*(gravedad_1*ALTURA))

# MOSTRAR VALORES
print("La velocidad inicial del objeto es: "+str(velocidad_inicial_1))
print("La gravedad es: "+str(gravedad_1))
print("La altura es: "+str(ALTURA))
print("La velocidad final del vehiculo es: "+str(velocidad_final))

