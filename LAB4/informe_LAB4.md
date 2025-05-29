<div style="text-align: center;">
 

# Trabajo Práctico N°4 Redes de Computadoras,FCEFyN-UNC #
## Fecha de entrega: -/05/2025 ##

</div>

## Profesores: ##
- Santiago Martin Henn
- Francisco Nicolas Oliva Cuneo

## Nombre del Grupo: ##
 **“Redes,Sudor y Lágrimas”** 

## Integrantes: ##
- Badariotti, Juan Miguel - 42260003
- Cáceres, Juan Manuel - 41411969
- Erlicher, Ezequiel - 42051917
- Dallari, Giuliano - 42642389

## PARTE I: Integración de conceptos, actividades online e investigación ##


## PARTE II: Simulaciones y análisis ##

Se construyo la siguiente topología conformada por dos AS en Packet Tracer: 65001 Y 65002

![alt text](Network_topology.jpeg)


Se establecen las rutas BGP en ambos routers con los siguientes comandos:

`router bgp [AS_NAME]`

`bgp log-neighbor-changes`

`neighbor [AS_next_hop] remote-as [neighborAS_name]`

`network [network_address] mask [mask]`

con la ayuda del comando `show ip bgp summary`, se verifica que se hallan establecido correctamente:

![alt text](<summary BGP Router 0.jpeg>)

![alt text](<summary BGP Router 1.jpeg>)


Testeo de conectividad de PC1 a las PCs del AS 65002
![alt text](<ping  PC1 a PC2 y PC3.jpeg>)

Testeo de conectividad de PC2 a las PCs del AS 65001
![alt text](<Ping PC2 a PC0 y PC1.jpeg>)

