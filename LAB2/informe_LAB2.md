
## 1)

La topología sobre la cual se trabajó en los apartados de este trabajo práctico fue similar a la siguiente:

![alt text](<img/Screenshot from 2025-04-16 17-55-34.png>)

En primera instancia, se realizaron pings para verificar la conexión entre computadoras conectadas a la subred `192.168.1.x`. Las computadoras de esta red poseían las IP’s `192.168.1.27` y `192.168.1.20` respectivamente.

![alt text](<img/WhatsApp Image 2025-04-17 at 16.35.29(2).jpeg>)

**Figura 1**: configuración de la dirección IP `192.168.1.27` de forma manual junto con la máscara de red y la default gateway.

![alt text](<img/WhatsApp Image 2025-04-17 at 16.35.29-1.jpeg>)

**Figura 2**: ping desde `192.168.1.27` a `192.168.1.20` (misma subred y switch).

Posteriormente, se probó conexión desde la misma computadora hacia otra subred, concretamente, la `34.27.143.x`.

![alt text](<img/WhatsApp Image 2025-04-17 at 16.35.30.jpeg>)

**Figura 3**: Envío de paquetes ICMP desde `192.168.1.27` a `34.27.143.1` (distinta subred y mismo switch).

---

## 2)

A continuación, se listan algunos de los principales **flags** que se utilizan para configurar diversos parámetros a la hora de testear una red con el software `iperf3`.

- `-s`, `--server`: Ejecuta iPerf en modo servidor. (Esto solo permite una conexión iPerf a la vez).

- `-c`, `--client host`: Ejecuta iPerf en modo cliente, conectándose a un servidor iPerf que se ejecuta en el host.

- `-p`, `--port n`: El puerto del servidor donde el servidor escucha y al que se conecta el cliente. Debe ser el mismo tanto para el cliente como para el servidor. El valor predeterminado es 5201.

- `-u`, `--udp`: Establece que la prueba se haga con el protocolo UDP (TCP es el protocolo por defecto).

- `-l`, `--len #[KM]`: Se especifica la longitud de los búferes para escritura o lectura. iPerf funciona escribiendo una matriz de `len` bytes varias veces. El valor predeterminado es 8 KB para TCP y 1470 bytes para UDP.

- `-t`, `--time n`: El tiempo en segundos para la transmisión. iPerf normalmente funciona enviando repetidamente una matriz de `len` bytes durante `time` segundos. El valor predeterminado es 10 segundos.

- `-b`, `--bandwidth n[KM]`: Setea el ancho de banda objetivo en `n` bits/s (predeterminado: 1 Mbit/s para UDP, ilimitado para TCP). Si hay varios streams (indicador `-P`), el límite de ancho de banda se aplica por separado a cada stream. También se puede agregar un símbolo "/" y un número al especificador de ancho de banda. Esto se denomina "modo ráfaga". Enviará la cantidad de paquetes indicada sin pausas, incluso si se excede temporalmente el límite de ancho de banda especificado.

- `-i`, `--interval n`: Establece el intervalo en segundos entre los informes periódicos de ancho de banda, fluctuación y pérdida. Si es distinto de cero, se genera un informe cada `interval` segundos del ancho de banda desde el último informe. Si es cero, no se imprimen informes periódicos. El valor predeterminado es cero.

## 3)

### Prueba de la red mediante el programa `iperf3`

En esta etapa realizamos una prueba de comunicación en la red creada entre el switch y las computadoras conectadas a él mediante el cableado ethernet, utilizando los comandos disponibles del programa `iperf3`.

El programa `iperf3` sirve para medir el rendimiento de la red, es decir, que nos permite hacer pruebas de velocidad y ancho de banda entre dos dispositivos conectados a través de una red.

Sus funciones para lo cual se puede utilizar son para medir el ancho de banda real entre dos puntos, diagnosticar cuellos de botella en la red, evaluar la latencia o jitter en conexiones UDP, comparar el rendimiento de diferentes interfaces de red (como Ethernet vs Wi-Fi) o tambien verificar la calidad de una red antes de desplegar aplicaciones críticas, entre otros.

Su funcionamiento necesita minimamente de dos computadoras, una que actúe como servidor y otra como cliente, donde el cliente realizará acciones para llevar a cabo las pruebas. En nuestro caso la red se compone de 3 computadoras donde la computadora servidor posee la IP `192.168.1.27` y la computadora cliente la IP `192.168.1.11`.

La computadora servidor ejecuta el comando `iperf3 -s` que hace que se inicie el programa `iperf3` en modo servidor y queda en escucha de los comandos que ejecuten los clientes.

### Prueba 1:

Para la primera prueba ejecutamos en el cliente el comando `iperf3 -c 192.168.1.27`, que se utiliza para lanzar una prueba de velocidad desde la computadora cliente hacia la computadora servidor.

![alt text](<img/iperf-client-1.png>)

Cada linea representa un intervalo de 1 segundo y muestra los datos que fueron transferidos durante ese lapso de tiempo.

El resúmen final nos indica los MB de datos que fueron eviados y los MB que fueron recibidos, además de que indica que Retr=0 informando que no hubo retransmiciones perdidas, y que la velocidad de transmicion de estos datos fue de 94.5 Mb/s, por lo que podemos inferir que se utilizó una velocidad de 100Mb/s en la red ethernet.

Podemos decir que la red está funcionando correctamente, no existe perdida de paquetes y el rendimiento es estable.

### Prueba 2:

En la segunda prueba se ejecutó el comando `iperf3 -c 192.168.1.27 -u` desde el cliente, que se utiliza para realizar la misma prueba que antes, pero con UDP en vez de TCP.

Esta prueba es útil para probar latencia, jitter y perdida de paquetes, útil en casos de VoIP, streaming, y casos similares.

![alt text](<img/iperf-client-2.png>)

Cada linea muestra los resultados en intervalos de tiempo de 1 segundo, indicando los datos transferidos, la velocidad de transferencia y el número de datagramas UDP enviados.

Como se puede ver se enviaron en promedio entre 90-91 datagramas de entre 127-129 KB por intervalo de tiempo a una velocidad de 1.05 Mb/s, y en el global se enviaron 1.25 MB en 10 segundos a 1.05 Mb/s con un jitter de 0.084 ms y no se perdio ningun paquete.

Con estos resultados podemos decir que la red en UDP funciona tambien correctamente, con bajo jitter, cero peridas y rendimiento constante.

### Prueba 3:

En la siguiente prueba se ejecuta el comando `iperf3 -c 192.168.1.27 -M 1400`, que con estos argumentos nos permite ajustar la prueba para definir el tamaño del TCP Maximum Segment Size o MSS en 1400 bytes, lo que puede ser útil para probar el comportamiento en redes que realizan fragmentación de paquetes.

![alt text](<img/iperf-client-3.png>)

Nuevamente cada linea indica la información de datos transmitidos en cada intervalo de tiempo de 1 segundo, y, por ejemplo, en el lapso de tiempo entre 0 y 1 segundo se transifirieron 11.4 MB a 95.4 Mb/s, y en todos los intervalos se muestra una velocidad constante tipica de una red ethernet de 100 Mb/s.

La prueba duró 10 segundos, el cambio de MSS a 1400 bytes no afecto la comunicación y la red sigue siendo estable.

### Prueba 4:

En esta prueba siguiente se ejecuta el comando `iperf3 -c 192.168.1.27 -u -l 1400` para realizar la prueba con UDP modificando el tamaño del datagrama a 1400 bytes, que es cercano al tamaño de datagrama típico MTU de ethernet (1500 bytes), por lo que es una buena forma de probar transmiciones sin fragmentación de datos.

![alt text](<img/iperf-client-4.png>)

Nuevamente cada linea indica lo ocurrido en intervalos de tiempo de 1 segundo, pudiendo observar cuanto se transfirió, a que velocidad y la cantidad de paquetes UDP enviados.

Se enviaron de manera constante entre 93-94 datagramas por segundo de 129 KB a una velocidad promedio de 1.05 Mb/s y se puede observar un jitter muy bajo sin perdida de paquetes, por lo que la red es confiable.

### Prueba 5:

Esta prueba siguiente ejecuta el comando `iperf3 -c 192.168.1.27 -t 30` que realiza lo mismo que la prueba número 1 que se realizó al principio, pero con 30 intervalos de tiempo de 1 segundo.

![alt text](<img/iperf-client-5.png>)

Nuevamente podemos decir que al extender la prueba no existen problemas de congestión ni problemas de comunicación en la red.

### Prueba 6:

Aquí realizamos el comando `iperf3 -c 192.168.1.27 -u -b 5M` que es para utilizar el protocolo UDP en vez de TCP y establecer el ancho de banda objetivo en 5 Mb/s.

![alt text](<img/iperf-client-6.png>)

En cada intervalo de tiempo podemos ver que los datos enviados son entre 609-611 KB, a una tasa de envio de 5 Mb/s, y que al final la transferencia total fue de 5.96 MB en 10 segundos a una velocidad sostenida de 5 Mb/s, con nula perdida de paquetes y nuevamente jitter muy bajo.

### Prueba 7:

En esta última prueba se ejecutó el comando `iperf3 -c 192.168.1.20` que al igual que en la prueba 1 realiza una bprueba básica de ancho de banda y latencias, pero al haber cambiado el servidor, retesteamos la conexión para asegurar que funciona correctamente.

![alt text](<img/iperf-client-7-server_change.png>)

Dado los resultados obtenidos se concluye que la conexión es exitosa y que esta correctamente establecida.


---

## 5)

### Prueba 1:
![Prueba 1 - Servidor remoto](<img/Imagen de WhatsApp 2025-04-14 a las 17.07.59_46d3976b.jpg>)

### Prueba 2:
![Prueba 2 - Servidor remoto](<img/Imagen de WhatsApp 2025-04-14 a las 17.07.59_109a5f85.jpg>)