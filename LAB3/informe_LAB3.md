# Redes-before MD

## 1)

**Explicación de OSPF:**

OSPF (Open Shortest Path First) es un protocolo de enrutamiento dinámico interior (IGP) basado en el algoritmo de estado de enlace (link-state), que permite a los routers intercambiar información sobre la topología de la red para construir una visión completa del entorno. OSPF utiliza el algoritmo de Dijkstra para calcular la ruta más corta (menor costo) desde un router a todos los demás dispositivos en la red.

OSPF es un protocolo estándar abierto, definido por la IETF (RFC 2328), y soporta características avanzadas como la división de la red en áreas jerárquicas (ej: backbone y áreas internas), balanceo de carga sobre múltiples rutas, detección rápida de cambios en la red y soporte para autenticación y VLSM (subredes de longitud variable).

**Clases de redes:**

En el direccionamiento IPv4 tradicional, se usaban clases de red para dividir el espacio de direcciones IP. Aunque el uso actual favorece CIDR (Classless Inter-Domain Routing), es útil entender las clases para diseñar esquemas de direccionamiento como pide el TP.

| Clase | Rango de IPs                | Bits de Red | Bits de Host | Uso común                              |
| ----- | --------------------------- | ----------- | ------------ | -------------------------------------- |
| A     | 0.0.0.0 - 127.255.255.255   | 8           | 24           | Grandes redes                          |
| B     | 128.0.0.0 - 191.255.255.255 | 16          | 16           | Redes medianas                         |
| C     | 192.0.0.0 - 223.255.255.255 | 24          | 8            | Pequeñas redes o enlaces punto a punto |

En este trabajo, se propone usar clase A o B para redes de hosts (mayor cantidad de dispositivos) y una clase C para los enlaces entre routers (usualmente punto a punto).

**Algoritmo de "shortest path":**

El algoritmo de Dijkstra, también conocido como SPF (Shortest Path First), es el más utilizado en OSPF. Este algoritmo asigna un costo a cada enlace (puede estar basado en ancho de banda, latencia, etc.), luego calcula la ruta de menor costo acumulado desde el router origen a todos los destinos y por último genera una tabla de rutas óptimas que el router utilizará para reenviar paquetes.

**Aplicación de la teoría de grafos:**

La teoría de grafos es fundamental para entender cómo funcionan las redes modernas, ya que una red puede modelarse como un grafo dirigido o no dirigido, donde los nodos representan routers u otros dispositivos y las aristas representan enlaces físicos o lógicos, con un peso/costo asociado.

En OSPF, cada router construye su propia visión del grafo completo usando información del protocolo (LSAs – Link State Advertisements) donde luego, con este grafo, el protocolo OSPF ejecuta el algoritmo de Dijkstra para construir el SPT (Shortest Path Tree) con el propio router como raíz y se deriva la tabla de enrutamiento que define hacia dónde reenviar paquetes para cada destino.

De esta manera, la teoría de grafos no solo sirve para representar la red, sino que es clave en la operación del protocolo OSPF al construir rutas eficientes y adaptarse rápidamente a cambios topológicos.

## 2)

La topología sobre la cual se trabajó fue la siguiente:  

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-13-30.png>)

  **Figura 1: Red**

</div>

A continuación se muestra el esquema de direccionamiento IP de la red. Se utilizó una segmentación clase A para las conexiones PC-Routers (subnet mask de 8 bits) y una segmentación clase C para las conexiones entre routers (subnet mask de 24 bits).  

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-14-34.png>)

  **Figura 2: Tabla de direccionamiento IP**

</div>

## 3)

En la siguiente secuencia de capturas, se testea la conectividad entre todas las PCs.

### PC0

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-16-19.png>)

  **Figura 3:** Testeo de conectividad hacia las otras computadoras en la misma red que PC0

  ![alt text](<img/Screenshot from 2025-04-23 19-18-29.png>)

  **Figura 4:** Testeo de conectividad hacia las computadoras en las redes 15.0.0.0/8 y 16.0.0.0/8

</div>

### PC1

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-19-31.png>)

  **Figura 5:** Testeo de conectividad hacia las otras computadoras en la misma red que PC1

  ![alt text](<img/Screenshot from 2025-04-23 19-20-03.png>)

  **Figura 6:** Testeo de conectividad hacia las computadoras en las redes 15.0.0.0/8 y 16.0.0.0/8

</div>

### PC2

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-22-22.png>)

  **Figura 7:** Testeo de conectividad hacia las otras computadoras en la misma red que PC2  

  ![alt text](<img/Screenshot from 2025-04-23 19-23-19.png>)

  **Figura 8:** Testeo de conectividad hacia las computadoras en las redes 15.0.0.0/8 y 16.0.0.0/8

</div>

### PC3

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-25-27.png>)

  **Figura 9:** Testeo de conectividad hacia las computadoras en la red 14.0.0.0/8 

  ![alt text](<img/Screenshot from 2025-04-23 19-26-03.png>)

  **Figura 10:** Testeo de conectividad hacia la computadora en la red 16.0.0.0/8 (PC4)

</div>

### PC4

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-27-59.png>)

  **Figura 11:** Testeo de conectividad hacia las computadoras en la red 14.0.0.0/8  

  ![alt text](<img/Screenshot from 2025-04-23 19-28-43.png>)

  **Figura 12:** Testeo de conectividad hacia la computadora en la red 15.0.0.0/8 (PC3)

</div>

---

Se puede verificar en las siguientes imágenes que las tablas de routing poseen rutas OSPF:

### Router0

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-29-19.png>)

  **Figura 13:** Rutas OSPF del Router0

</div>

### Router1

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-29-56.png>)

  **Figura 14:** Rutas OSPF del Router1

</div>

### Router2

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-30-49.png>)

  **Figura 15:** Rutas OSPF del Router2

</div>

### Router3

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-31-13.png>)

  **Figura 16:** Rutas OSPF del Router3

</div>

### Router4

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-32-25.png>)

  **Figura 17:** Rutas OSPF del Router4

</div>

## 4)

Hay 5 mensajes OSPF que se pueden enviar por la red (en orden):

**Hello**: Permite descubrir y mantener relaciones con routers vecinos. Se envían de manera periódica. Si los paquetes Hello se detienen, el vecino se considera inactivo después de que expire el Temporizador de inactividad.

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-32-46.png>)

  **Figura 18:** Mensaje OSPF Hello

</div>

**Database Description (DBD)**: Resumen de los contenidos de la LSDB (link-state database) del router. Se utiliza para determinar si los vecinos están sincronizados.

**Link-State Request (LSR) Packet**: Se envía en respuesta a las DBD si un router solicita información más detallada.

**Link State Update (LSU)**: Contiene uno o más Link State Advertisements (LSAs). Contiene información topológica tales como enlaces del router, redes, costos, etc. Puede enviarse como respuesta a los LSA o cuando se produce un cambio en la red.

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-33-17.png>)

  **Figura 19:** Mensaje OSPF Link State Update

</div>

**Link State Acknowledgment (LSA)**: Enviado para confirmar la recepción de LSUs.

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-23 19-33-52.png>)

  **Figura 20:** Mensaje OSPF Link State Acknowledgment

</div>

## 8) Costo de ospf:

El camino sin modificación de los costos desde H1 a H4 es:

<div align="center">

  ![alt text](<img/image.png>)

</div>

Al aumentar el costo del camino entre R3 y R4 forzamos que vaya por R5

<div align="center">

  ![alt text](<img/image-1.png>)

  ![alt text](<img/image-2.png>)

</div>

Y la vuelta de H4 a H2:

<div align="center">

  ![alt text](<img/image-3.png>)

</div>

## 9) Redistribuir una ruta OSPF predeterminada:

a) Para configurar una dirección de loopback en R1 para simular un enlace a un proveedor de servicios de Internet (ISP) corrimos los siguientes códigos:

Router(config)# interface loopback0

Router(config-if)# ip address 127.0.0.1 255.0.0.0

Router(config-if)# no shutdown

Router(config-if)# exit

b) Para configurar una ruta estática predeterminada en el router R1 e incluirla en las actualizaciones de OSPF, lanzamos los siguientes códigos en el CLI del router 1

<div align="center">

  ![alt text](<img/image-4.png>)

</div>

## 10) Impacto de la caída en una de las interfaces de R2:

Al caerse una de las interfaces, el protocolo OSPF “aprende” de esa modificación y actualiza las tablas de enrutamiento que correspondan. Por ejemplo, la tabla de enrutamiento de R3 con todas las interfaces de R2 levantadas es

<div align="center">

  ![alt text](<img/image-5.png>)

</div>

Al bajar la interfaz R2-S1, el router R3 actualiza automáticamente su tabla de enrutamiento quedando de la siguiente manera

<div align="center">

  ![alt text](<img/image-6.png>)

</div>

## 11) Es lo mismo la tabla RIB (Routing Information Base) y FIB (Forwarding Information Base)?:

La respuesta es no, dado que la tabla RIB no es lo mismo que la tabla FIB aunque están estrechamente relacionadas y ambas son fundamentales para el funcionamiento del enrutamiento.

Para la tabla RIB podemos decir que es una base de datos lógica que contiene todas las rutas aprendidas por el router a través de distintos protocolos de enrutamiento (como OSPF, RIP, BGP), rutas estáticas y rutas conectadas directamente. Mantiene múltiples rutas hacia un mismo destino, incluso si no todas serán utilizadas y OSPF y otros protocolos escriben sus rutas en esta tabla.

En cambio la tabla FIB, es la tabla que realmente se usa para reenviar paquetes en tiempo real y contiene solo las mejores rutas seleccionadas por la RIB para cada destino. Está optimizada para el rendimiento, y generalmente es gestionada por el hardware del router (por ejemplo, ASICs en routers Cisco).

Como ejemplo, utilizaremos el Router 3 de la simulación para ejecutar el comando 'show ip route' y ver las tablas como justificación.

<div align="center">

  ![alt text](<img/Screenshot from 2025-04-25 12-02-58.png>)

</div>

Aunque 'show ip route' muestra la RIB, también indica qué ruta está siendo usada activamente, es decir, lo que terminó en la FIB. En la mayoría de los entornos educativos, la FIB es simplemente el subconjunto activo de la RIB.
