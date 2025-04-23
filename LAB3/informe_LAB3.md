# Redes-before MD

## 2)

La topología sobre la cual se trabajó fue la siguiente:  

![alt text](<Screenshot from 2025-04-23 19-13-30.png>)
**Figura 1: Red**

A continuación se muestra el esquema de direccionamiento IP de la red. Se utilizó una segmentación clase A para las conexiones PC-Routers (subnet mask de 8 bits) y una segmentación clase C para las conexiones entre routers (subnet mask de 24 bits).  

![alt text](<Screenshot from 2025-04-23 19-14-34.png>)

**Figura 2: Tabla de direccionamiento IP**

## 3)

En la siguiente secuencia de capturas, se testea la conectividad entre todas las PCs.

### PC0

![alt text](<Screenshot from 2025-04-23 19-16-19.png>)

**Figura 3:** Testeo de conectividad hacia las otras computadoras en la misma red que PC0  

![alt text](<Screenshot from 2025-04-23 19-18-29.png>)

**Figura 4:** Testeo de conectividad hacia las computadoras en las redes 15.0.0.0/8 y 16.0.0.0/8

### PC1

![alt text](<Screenshot from 2025-04-23 19-19-31.png>)

**Figura 5:** Testeo de conectividad hacia las otras computadoras en la misma red que PC1

![alt text](<Screenshot from 2025-04-23 19-20-03.png>)

**Figura 6:** Testeo de conectividad hacia las computadoras en las redes 15.0.0.0/8 y 16.0.0.0/8

### PC2

![alt text](<Screenshot from 2025-04-23 19-22-22.png>)

**Figura 7:** Testeo de conectividad hacia las otras computadoras en la misma red que PC2  

![alt text](<Screenshot from 2025-04-23 19-23-19.png>)

**Figura 8:** Testeo de conectividad hacia las computadoras en las redes 15.0.0.0/8 y 16.0.0.0/8

### PC3

![alt text](<Screenshot from 2025-04-23 19-25-27.png>)

**Figura 9:** Testeo de conectividad hacia las computadoras en la red 14.0.0.0/8 

![alt text](<Screenshot from 2025-04-23 19-26-03.png>)

**Figura 10:** Testeo de conectividad hacia la computadora en la red 16.0.0.0/8 (PC4)

### PC4

![alt text](<Screenshot from 2025-04-23 19-27-59.png>)

**Figura 11:** Testeo de conectividad hacia las computadoras en la red 14.0.0.0/8  

![alt text](<Screenshot from 2025-04-23 19-28-43.png>)

**Figura 12:** Testeo de conectividad hacia la computadora en la red 15.0.0.0/8 (PC3)

---

Se puede verificar en las siguientes imágenes que las tablas de routing poseen rutas OSPF:

### Router0

![alt text](<Screenshot from 2025-04-23 19-29-19.png>)

**Figura 13:** Rutas OSPF del Router0

### Router1

![alt text](<Screenshot from 2025-04-23 19-29-56.png>)

**Figura 14:** Rutas OSPF del Router1


### Router2


![alt text](<Screenshot from 2025-04-23 19-30-49.png>)

**Figura 15:** Rutas OSPF del Router2

### Router3

![alt text](<Screenshot from 2025-04-23 19-31-13.png>)

**Figura 16:** Rutas OSPF del Router3

### Router4

![alt text](<Screenshot from 2025-04-23 19-32-25.png>)

**Figura 17:** Rutas OSPF del Router4

## 4)

Hay 5 mensajes OSPF que se pueden enviar por la red (en orden):

**Hello**: Permite descubrir y mantener relaciones con routers vecinos. Se envían de manera periódica. Si los paquetes Hello se detienen, el vecino se considera inactivo después de que expire el Temporizador de inactividad.

![alt text](<Screenshot from 2025-04-23 19-32-46.png>)

  **Figura 18:** Mensaje OSPF Hello

**Database Description (DBD)**: Resumen de los contenidos de la LSDB (link-state database) del router. Se utiliza para determinar si los vecinos están sincronizados.

**Link-State Request (LSR) Packet**: Se envía en respuesta a las DBD si un router solicita información más detallada.

**Link State Update (LSU)**: Contiene uno o más Link State Advertisements (LSAs). Contiene información topológica tales como enlaces del router, redes, costos, etc. Puede enviarse como respuesta a los LSA o cuando se produce un cambio en la red.

![alt text](<Screenshot from 2025-04-23 19-33-17.png>)

  **Figura 19:** Mensaje OSPF Link State Update

**Link State Acknowledgment (LSA)**: Enviado para confirmar la recepción de LSUs.

![alt text](<Screenshot from 2025-04-23 19-33-52.png>)

  **Figura 20:** Mensaje OSPF Link State Acknowledgment