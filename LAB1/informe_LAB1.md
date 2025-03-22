

<div style="text-align: center;">
 

# Trabajo Práctico N°1 Redes de Computadoras,FCEFyN-UNC #
## Fecha de entrega: 27/03/2025 ##

</div>


ctrl+shift+v to visualize preview 

## Profesores: ##
  -Santiago Martin Henn
  -Francisco Nicolas Oliva Cuneo

## Nombre del Grupo: ##
 “Redes,Sudor y Lágrimas” 

## Integrantes: ##
- Badariotti, Juan Miguel - 42260003
- Cáceres, Juan Manuel - 
- Erlicher, Ezequiel - 42051917
- Dallari,

<div style="text-align: center;"> 

# Parte I - Configuración y Análisis de tráfico IPv4/IPv6 #
</div>

<div style="text-align: center;"> 

# Parte II - Configuración y Análisis de tráfico IPv4/IPv6 #
</div>

## a y b) Conexión al switch y modificación de contraseñas 

En primera instancia se configura la contraseña para acceder al modo usuario tal como se muestra en la siguiente imagen


![alt text](image-1.png)

Posteriormente, se configuran las contraseñas para acceder el modo priviledged

![alt text](image.png)

una vez configuradas se ve como al reingresar al switch se solicitan ambas
contraseñas

![alt text](image-2.png)


## c) Conexión de 2 computadoras y testeo de conectividad

Se conectan 2 computadoras al switch mediante cables Ethernet (RJ45) y se configuraron las siguientes direcciones IP en cada una:

#image 1

#image 2

una vez configuradas las IP's, se testeo la conectividad entre ambas mediante comandos PING:

#image 3


## d) Configuración de un puerto en modo mirroring y monitoreo de tráfico


Se establecen los puerto 3 y 9 como puertos source donde se conectan posteriormente las computadoras. El puerto a donde se conecta la computadora que va a interceptar el tráfico 
es el 6
![alt text](image-4.png)