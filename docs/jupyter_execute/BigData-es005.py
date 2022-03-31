#!/usr/bin/env python
# coding: utf-8

# # Big Data tema 5

# ## Aplicaciones para Big Data

# - Hadoop: HDFS & MapReduce
# - Apache Storm
# - Apache Spark
# - Apache Kafka

# ## Hadoop

# - El proyecto Apache™ Hadoop® desarrolla software de código abierto para computación distribuida, escalable y confiable.
#     - Extraído de: <https://hadoop.apache.org/>.

# - Es un framework para el procesamiento distribuido de grandes conjuntos de datos en grupos de computadoras que utilizan modelos de programación simples.
# - Diseñado para escalar desde servidores individuales a miles de máquinas, cada una de las cuales ofrece computación y almacenamiento locales.

# - En lugar de depender del hardware para brindar alta disponibilidad, la biblioteca en sí está diseñada para detectar y manejar fallas en la capa de la aplicación, por lo que brinda un servicio de alta disponibilidad sobre un grupo de computadoras, cada una de las cuales puede ser propensa a fallas.

# ## Módulos de Apache Hadoop 

# - Apache Hadoop cuenta con una serie de módulos que le permiten extender sus funcionalidades.
# - Los más utilizados son *Hadoop Common, HDFS, YARN y MapReduce*.

# - Hadoop Common: 
#     - Las *common utilities* que soportan los otros módulos de Hadoop.
# - Hadoop Distributed File System (HDFS™): 
#     - Un sistema de archivos distribuido que proporciona acceso de alto rendimiento a los datos de la aplicación.

# - Hadoop YARN
#     - Un framework para job scheduling y gestión de recursos de los clusters. 
#     - Tecnología de gestión de clústeres en Hadoop de segunda generación.
#     - Extraído de: <https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html>.

# - MapReduce
#     - Un sistema basado en YARN para el procesamiento en paralelo de grandes volúmenes de datos.    
#     - Este framework procesa cantidades masivas de datos no estructurados en paralelo en un clúster distribuido.
#     - Extraído de: <https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html>.

# ## Apache Hadoop YARN

# - Tecnología de gestión de clústeres en Hadoop de segunda generación.
# - La idea de YARN es dividir las funcionalidades de gestión de recursos y programación/supervisión de trabajos en demonios separados: un ResourceManager (RM) global y un ApplicationMaster (AM) por aplicación.
# - Una aplicación es un solo trabajo o un DAG de trabajos.
# - El ResourceManager y el NodeManager forman el framework de cálculo de datos. 

# - Fuente: <https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html>

# - El ResourceManager arbitra los recursos entre todas las aplicaciones del sistema.
# - El NodeManager es el agente del framework por máquina que es responsable de los contenedores, monitorea el uso de sus recursos (cpu, memoria, disco, red) e informa al ResourceManager / Scheduler. 

# - La aplicación ApplicationMaster es en efecto una biblioteca específica del framework y tiene la tarea de negociar recursos del ResourceManager y trabajar con los NodeManager(s) para ejecutar y monitorear las tareas.

# ## Apache Hadoop MapReduce

# - Es un framework de software para escribir fácilmente aplicaciones que procesan grandes cantidades de datos (conjuntos de datos de varios terabytes) en paralelo en grandes clústeres (miles de nodos) de hardware básico de manera confiable y tolerante a fallas.

# Fuente: {cite:ps}`Turkington2013`

# - Consta de un único ResourceManager maestro, un NodeManager trabajador por nodo de clúster y MRAppMaster por aplicación.
# - Las aplicaciones especifican las ubicaciones de entrada/salida y el mapa de suministro y reducen las funciones a través de implementaciones de interfaces apropiadas y/o clases abstractas.
# - Estos y otros parámetros del trabajo comprenden la configuración del trabajo.

# - El cliente de trabajo de Hadoop luego envía el trabajo (jar/ejecutable, etc.) y la configuración al ResourceManager, que entonces asume la responsabilidad de distribuir el software/configuración a los trabajadores, programar tareas y monitorearlas, proporcionando estado e información de diagnóstico al trabajo-cliente.

# - Las aplicaciones de MapReduce no necesitan estar escritas en Java.
# - Hadoop Streaming es una utilidad que permite a los usuarios crear y ejecutar trabajos con cualquier ejecutable (por ejemplo, utilidades de shell) como mapeador y/o reductor.
# - Hadoop Pipes es una API C++ compatible con SWIG para implementar aplicaciones MapReduce (no basadas en JNI™).

# - Entradas y salidas:
# - El framework MapReduce opera exclusivamente en pares <clave, valor>, es decir, el framework ve la entrada del trabajo como un conjunto de pares <clave, valor> y produce un conjunto de pares <clave, valor> como la salida de el trabajo, posiblemente de diferentes tipos.

# - Tipos de entradas y salidas de un MapReduce job:
# 
#     `(input) <k1, v1> -> map -> <k2, v2> -> combine -> <k2, v2> -> reduce -> <k3, v3> (output)`

# ## Sistema de ficheros HDFS

# - HDFS es un sistema de ficheros basado en Java que provee almacenamiento confiable y escalable.
# - Fue diseñado para abarcar grandes grupos de servidores básicos (commodity servers).
# - HDFS contiene una gran cantidad de datos y proporciona un acceso a los mismos de manera sencilla y fácil.
#     - Extraído de: <https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html>. 

# - HDFS proporciona acceso de alto rendimiento a los datos de la aplicación y es adecuado para aplicaciones que tienen grandes conjuntos de datos.
# - HDFS relaja algunos requisitos de POSIX para permitir el acceso de transmisión a los datos del sistema de archivos.
# - HDFS se creó originalmente como infraestructura para el proyecto de motor de búsqueda web Apache Nutch.

# - Supuestos y objetivos de HDFS:
# - La falla de hardware es la norma y no la excepción, por lo que la detección de fallas y la recuperación rápida y automática de ellas es un objetivo arquitectónico central de HDFS.
# - Las aplicaciones que se ejecutan en HDFS necesitan acceso de transmisión a sus conjuntos de datos. 
# - HDFS está diseñado más para el procesamiento por lotes que para el uso interactivo por parte de los usuarios.

# - Las aplicaciones que se ejecutan en HDFS tienen grandes conjuntos de datos.
# - Las aplicaciones HDFS necesitan un modelo de acceso de escritura única, lectura múltiple para archivos, lo que permite un acceso de datos de alto rendimiento. 
# - Una aplicación MapReduce o una aplicación de rastreo web encaja perfectamente con este modelo.

# - Mover computación es más barato que mover datos. 
# - HDFS proporciona interfaces para que las aplicaciones se muevan más cerca de donde se encuentran los datos.
# - Portabilidad a través de plataformas heterogéneas de hardware y software.

# ## Características de HDFS

# - Para almacenar una inmensa cantidad de datos, los ficheros son guardados en varias máquinas. 
# - Estos ficheros son guardados de forma redundante para poder rescatar el sistema en caso de pérdida de datos a causa de fallos.

# - HDFS también proporciona la disponibilidad de aplicaciones para procesamiento en paralelo durante el paso de *Data ingestion*. 
# - HDFS fue construido para soportar aplicaciones con grandes conjuntos de datos, incluyendo ficheros con *terabytes* de tamaño.

# - Utiliza una arquitectura maestro/esclavo, en la que cada clúster consta de un solo NameNode que administra las operaciones del sistema de archivos y admite DataNodes que administran el almacenamiento de datos en nodos de cómputo individuales. 

# - Cuando HDFS toma datos, divide la información en partes separadas y las distribuye a diferentes nodos en un clúster, lo que permite el procesamiento paralelo. 
# - El sistema de archivos en Ingestión de datos también copia cada pieza de datos varias veces y distribuye las copias a nodos individuales, colocando al menos una copia en un rack de servidor diferente. 

# ## Proyectos relacionados con Apache Hadoop

# - Ambari™: una herramienta basada en web para aprovisionar, administrar y monitorear clústeres de Apache Hadoop.
# - Avro™: Un sistema de serialización de datos.
# - Cassandra™: una base de datos multimaestro escalable sin puntos únicos de falla.
# - Chukwa™: un sistema de recopilación de datos para gestionar grandes sistemas distribuidos.
# - HBase™: una base de datos distribuida escalable que admite el almacenamiento de datos estructurados para tablas grandes.
# - Hive™: una infraestructura de almacenamiento de datos que proporciona resúmenes de datos y consultas ad hoc.
# - Mahout™: una biblioteca escalable de aprendizaje automático y minería de datos.

# - Ozone™: un almacén de objetos escalable, redundante y distribuido para Hadoop.
# - Pig™: un lenguaje de flujo de datos de alto nivel y un marco de ejecución para computación paralela.
# - Spark™: un motor de cómputo rápido y general para datos de Hadoop. .
# - Submarine: una plataforma de IA unificada que permite a los ingenieros y científicos de datos ejecutar cargas de trabajo de ML y DL en un clúster distribuido.
# - Tez™: un marco de programación de flujo de datos generalizado, basado en Hadoop YARN, que proporciona un motor potente y flexible para ejecutar un DAG arbitrario de tareas para procesar datos tanto para casos de uso por lotes como interactivos. Tez está siendo adoptado por Hive™, Pig™ y otros marcos en el ecosistema de Hadoop, y también por otro software comercial (por ejemplo, herramientas ETL), para reemplazar a Hadoop™ MapReduce como el motor de ejecución subyacente.
# - ZooKeeper™: un servicio de coordinación de alto rendimiento para aplicaciones distribuidas.

# ## Tutorial Apache Hadoop

# - Instalación de Hadoop en CentOS 8
# - Fuente: <https://fortinux.com/linux-2-tutoriales/hadoop-installation-centos8/#more-1750>

# ## Apache Spark

# - Framework de procesamiento paralelo y de código abierto para ejecutar aplicaciones de análisis de datos a gran escala en sistemas agrupados.
# - Proporciona APIs de alto nivel en Java, Scala, Python y R, y un motor optimizado que soporta grafos de ejecución general.
#     - Extraído de: <https://spark.apache.org/>.

# - También es compatible con un amplio conjunto de herramientas de alto nivel, que incluyen Spark SQL para SQL y procesamiento de datos estructurados, MLlib para aprendizaje automático, GraphX para procesamiento de gráficos y transmisión estructurada para procesamiento incremental y de streaming.

# - Spark SQL incluye un optimizador basado en costes, almacenamiento en columnas y generación de código para agilizar las consultas.
# - Al mismo tiempo, se escala a miles de nodos y consultas de varias horas mediante el motor Spark, que proporciona tolerancia completa a fallas en la mitad de la consulta. 

# - Facilidad de uso: Es posible escribir aplicaciones rápidamente en Java, Scala, Python, R y SQL.
# - Spark ofrece más de 80 operadores de alto nivel que facilitan la creación de aplicaciones paralelas.
# - Además se puede usar de forma interactiva desde los shells de Scala, Python, R y SQL.

# - Velocidad: Se ejecutan cargas de trabajo 100 veces más rápidas.
# - Apache Spark logra un alto rendimiento tanto para datos por lotes como en streaming, utilizando un programador DAG de última generación, un optimizador de consultas y un motor de ejecución física.

# - Se ejecuta en todas partes: Se puede ejecutar Spark utilizando su modo de clúster independiente, en EC2, en Hadoop YARN, en Mesos o en Kubernetes.
# - Se acceden a los datos en HDFS, Alluxio, Apache Cassandra, Apache HBase, Apache Hive y cientos de otras fuentes de datos.

# ## Características de Apache Spark

# - La máquina en la que se ejecuta la aplicación Spark (*Spark Context*) se denomina nodo de controlador (*driver node*), que ejecuta varias operaciones paralelas en los nodos de trabajo del clúster.

# - Spark utiliza el concepto de un conjunto de datos distribuido resiliente (RDD), que representa una colección de objetos de solo lectura particionados en un conjunto de máquinas que se pueden reconstruir si se pierde una partición.

# - La seguridad en Spark está DESACTIVADA de forma predeterminada.
# - Esto podría significar que se es vulnerable a un ataque por defecto.
# - Es necesario leer la documentación sobre seguridad antes de descargar y ejecutar Spark.

# ## Casos de uso de Spark

# - Se utiliza para realizar trabajos informáticos con grandes cargas de datos junto a Apache Kafka. 
# - Fue desarrollado en la University of California, Berkeley.

# - Con Spark ejecutándose en Apache Hadoop YARN, los desarrolladores pueden crear aplicaciones para explotar el poder de Spark, obtener información y enriquecer sus cargas de trabajo de ciencia de datos dentro de un único conjunto de datos compartidos en Hadoop.

# - Monitoramento del tránsito automotor utilizando IoT, Kafka y Spark Streaming.

# ## Apache Storm

# - Es un sistema distribuido open source para procesar datos en tiempo real durante la ingesta de datos. 
# - Es escalable, tiene tolerancia a fallos, y es fácil de configurar y operar.
# - Facilita el procesamiento confiable de flujos ilimitados de datos, haciendo para el procesamiento en tiempo real lo que Hadoop hizo para el procesamiento por lotes.
#     - Extraído de: <https://storm.apache.org/>.

# - No existe ningún truco que convierta a Hadoop en un sistema en tiempo real.
# - El procesamiento de datos en tiempo real tiene un conjunto de requisitos fundamentalmente diferente al procesamiento por lotes.
# - Apache Storm agrega a Hadoop esta funcionalidad de manera sencilla.

# - Apache Storm en YARN es poderoso para escenarios que requieren análisis en tiempo real, aprendizaje automático (ML) y monitoreo continuo de operaciones.

# - Casos de uso:
#     - Análisis en tiempo real
#     - Aprendizaje automático
#     - Monitoreo continuo de operaciones
#     - RPC distribuido, ETL, y más.

# ## Características de Apache Storm

# - Es rápido: un *benchmark* registró más de un millón de tuplas procesadas por segundo por nodo.
# - Es escalable, tolerante a fallas, garantiza que los datos serán procesados y es fácil de configurar y operar.

# - Se integra con las tecnologías de colas (*queueing*) y bases de datos que ya se utilizan.
# - Una topología de Apache Storm consume flujos de datos y procesa esos flujos de formas arbitrariamente complejas, repartiendo los flujos entre cada etapa del cálculo según sea necesario.

# - Storm se puede utilizar para:
#      - Procesamiento de mensajes y actualización de bases de datos (stream processing).
#      - Consulta continua sobre flujos de datos y transmisión de los resultados a los clientes (computación continua).
#      - Paralelizar una consulta intensa como una consulta de búsqueda sobre la marcha (RPC distribuido), y más.

# - Escalable: Storm se escala a cantidades masivas de mensajes por segundo.
# - Para escalar una topología, todo lo que se tiene que hacer es agregar máquinas y aumentar la configuración de paralelismo de la topología.

# - Como ejemplo de la escala de Storm, una de las aplicaciones iniciales de Storm procesó 1000000 de mensajes por segundo en un clúster de 10 nodos, incluidos cientos de llamadas a la base de datos por segundo como parte de la topología.
# - El uso de Zookeeper por parte de Storm para la coordinación de clústeres lo hace escalar a tamaños de clúster mucho más grandes.

# - Garantías de no pérdida de datos: un sistema en tiempo real debe tener fuertes garantías de que los datos se procesarán con éxito.
# - Un sistema que distribuye datos tiene un conjunto muy limitado de casos de uso.
# - Storm garantiza que todos los mensajes serán procesados, y esto contrasta directamente con otros sistemas como S4.

# - Extremadamente robusto: a diferencia de sistemas como Hadoop, que son conocidos por ser difíciles de administrar, los clústeres de Storm simplemente funcionan.
# - Es un objetivo explícito del proyecto Storm hacer que la experiencia del usuario al administrar los clústeres de Storm sea lo menos dolorosa posible.

# - Tolerante a fallas: si hay fallas durante la ejecución de cálculos, Storm reasignará las tareas según sea necesario.
# - Storm se asegura de que un cómputo pueda ejecutarse para siempre (o hasta que éste se elimine).

# - Independiente del lenguaje de programación: el procesamiento en tiempo real robusto y escalable no debe limitarse a una sola plataforma.
# - Las topologías y los componentes de procesamiento de Storm se pueden definir en cualquier idioma, lo que hace que Storm sea accesible para casi cualquier persona.

# ## Storm vs. Spark

# | Situación | Spark | Storm |
# |------- | ---------------- | -------- | 			
# | Stream processing | Batch processing | Micro-batch processing |
# | Latency | Latency of a few seconds | Latency of milliseconds |
# | Multi-language support | Lesser language support | Multiple language support |
# | Languages | Java – Scala | Java – Scala – Clojure |
# | Stream sources | HDFS | Spout |
# | Resource management | Yarn, Mesos | Yarn, Mesos |
# | Provisioning | Basic using Ganglia | Apache Ambari |
# | Messaging | Netty, Akka | ZeroMQ, Netty |

# ## Apache Kafka

# - Apache Kafka es una plataforma de transmisión de eventos distribuidos de código abierto utilizada por miles de empresas para canalizaciones de datos de alto rendimiento, análisis de streaming, integración de datos y aplicaciones de misión crítica.
# - Es un sistema de mensajería escalable que permite a los usuarios publicar y consumir grandes cantidades de mensajes en tiempo real por suscripción.
#     - Extraído de: <https://kafka.apache.org/>. 

# ## Características de Apache Kafka

# - Alto rendimiento: 
#     - Entregue mensajes con un rendimiento limitado de la red utilizando un grupo de máquinas (cluster) con una latencia de tan solo 2 ms.

# - Escalable
#      - Es posible escalar clústeres de producción con hasta mil brokers, billones de mensajes por día, petabytes de datos, cientos de miles de particiones.
#      - También expandir y contraer elásticamente el almacenamiento y procesamiento.

# - Almacenamiento permanente
#      - Almacene flujos de datos de forma segura en un clúster distribuido, duradero y tolerante a fallas.

# - Alta disponibilidad
#      - Estire los clústeres de manera eficiente sobre las zonas de disponibilidad o conecte clústeres separados en regiones geográficas.

# - Procesamiento de flujo incorporado
#      - Procese secuencias de eventos con uniones, agregaciones, filtros, transformaciones y más, utilizando el procesamiento solo una vez con el tiempo de evento.

# - Conéctese a casi cualquier cosa
#      - La interfaz *Connect* lista para usar de Kafka se integra con cientos de orígenes de eventos y receptores de eventos, incluidos PostgreSQL, JMS, Elasticsearch, AWS S3 y más.

# - Bibliotecas de clientes
#      - Posibilidad de Leer, escribir y procesar flujos de eventos en una amplia gama de lenguajes de programación.

# - Herramientas de código abierto para grandes ecosistemas
#      - Gran ecosistema de herramientas de código abierto: existe una amplia gama de herramientas impulsadas por la comunidad.

# ## Transmisión de eventos

# - La transmisión de eventos es el equivalente digital del sistema nervioso central del cuerpo humano.
# - Es la base tecnológica para el mundo 'siempre activo' donde las empresas están cada vez más definidas por software y automatizadas, y donde el usuario de software es más software (Inteligencia Artificial).

# - Técnicamente hablando, la transmisión de eventos es la práctica de capturar datos en tiempo real de fuentes de eventos como bases de datos, sensores, dispositivos móviles, servicios en la nube y aplicaciones de software en forma de flujos de eventos; almacenar estos flujos de eventos de forma duradera para su posterior recuperación; manipular, procesar y reaccionar a los flujos de eventos en tiempo real y retrospectivamente; y enrutar los flujos de eventos a diferentes tecnologías de destino según sea necesario.

# - La transmisión de eventos garantiza un flujo continuo y una interpretación de los datos para que la información correcta esté en el lugar correcto, en el momento correcto. 

# - Kafka combina tres capacidades clave para que pueda implementar sus casos de uso para la transmisión de eventos de extremo a extremo con una única solución exitosamente testeada.

# - Para publicar (escribir) y suscribirse a (leer) flujos de eventos, incluida la importación/exportación continua de sus datos desde otros sistemas.
# - Para almacenar secuencias de eventos de forma duradera y fiable durante el tiempo que desee.
# - Procesar flujos de eventos a medida que ocurren o retrospectivamente.

# - Toda esta funcionalidad se proporciona de forma distribuida, altamente escalable, elástica, tolerante a fallos y segura.
# - Kafka se puede implementar en hardware básico, máquinas virtuales y contenedores, tanto en las instalaciones propias como en la nube.
# - Es posible elegir entre la autogestión de los entornos Kafka y el uso de servicios totalmente gestionados ofrecidos por una variedad de proveedores.

# ## Procesos de Apache Kafka

# - Kafka se ejecuta como un clúster de uno o más servidores que pueden abarcar varios centros de datos o regiones de la nube.
# - Algunos de estos servidores forman la capa de almacenamiento, llamados intermediarios (*brokers*). 

# - Clientes: le permiten escribir aplicaciones distribuidas y microservicios que leen, escriben y procesan flujos de eventos en paralelo, a escala y con tolerancia a fallas, incluso en el caso de problemas de red o fallas de máquinas.

# - Un evento registra el hecho de que "algo pasó" en el mundo o en el negocio.
# - También se le llama registro o mensaje en la documentación.
# - Cuando lee o escribe datos en Kafka, lo hace en forma de eventos.
# - Conceptualmente, un evento tiene una clave, un valor, una marca de tiempo, y encabezados de metadatos opcionales.

# - Los productores son aquellas aplicaciones cliente que publican (escriben) eventos en Kafka, y los consumidores son los que se suscriben (leen y procesan) estos eventos.

# - Los eventos se organizan y almacenan de forma duradera en temas (*topics*).
# - Muy simplificado, un tema es similar a una carpeta en un sistema de archivos, y los eventos son los archivos en esa carpeta.
# - Un nombre de tema de ejemplo podría ser "pagos".

# - Los temas están particionados, lo que significa que un tema se distribuye en varios "cubos" (*buckets*) ubicados en diferentes *brokers* de Kafka.
# - Esta ubicación distribuida de los datos es muy importante para la escalabilidad porque permite que las aplicaciones cliente lean y escriban los datos desde/hacia muchos *brokers* al mismo tiempo.

# ## Tutorial Apache Kafka 

# - Descargar e instalar Kafka en una máquina virtual
# - <https://kafka.apache.org/quickstart>.
