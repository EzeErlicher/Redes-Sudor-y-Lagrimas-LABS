

## 1)

La topología sobre la cual se trabajó en los apartados de este trabajo práctico fue similar a la siguiente:

![alt text](<Screenshot from 2025-04-16 17-55-34.png>)

En primera instancia, se realizaron pings para verificar la conexión entre computadoras conectadas a la subred `192.168.1.x`. Las computadoras de esta red poseían las IP’s `192.168.1.27` y `192.168.1.20` respectivamente.


![alt text](<WhatsApp Image 2025-04-17 at 16.35.29(2).jpeg>)


**Figura 1**: configuración de la dirección IP `192.168.1.27` de forma manual junto con la máscara de red y la default gateway.


![alt text](<WhatsApp Image 2025-04-17 at 16.35.29-1.jpeg>)

**Figura 2**: ping desde `192.168.1.27` a `192.168.1.20` (misma subred y switch).

Posteriormente, se probó conexión desde la misma computadora hacia otra subred, concretamente, la `34.27.143.x`.


![alt text](<WhatsApp Image 2025-04-17 at 16.35.30.jpeg>)

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
