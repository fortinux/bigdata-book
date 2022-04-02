#!/usr/bin/env python
# coding: utf-8

# # Big Data tema 2

# ## Procesos en Big Data 

# - Existen varias metodologías disponibles en el mercado para la recopilación, almacenamiento, consulta y visualización de datos.
# - Provienen del mundo de la minería de datos, y entre ellas se pueden mencionar KDD (*Knowledge Discovery in Databases*), SEMMA y CRISP-DM.
# - CRISP-DM (*Cross Industry Standard Process for Data Mining*) por ejemplo, es un proceso iterativo centrado en el negocio. 
# - Sus fases son: comprensión del negocio, Comprensión de los datos, Preparación de los datos, Fase de Modelado, Evaluación e Implantación.
#     - Fuente: Metodología para el Desarrollo de proyectos en Minería de Datos CRISP-DM
#     - <http://www.oldemarrodriguez.com/yahoo_site_admin/assets/docs/Documento_CRISP-DM.2385037.pdf>.

# - Para proyectos de Big Data los procesos básicamente se pueden dividir en cuatro fases: 
#     - Ingestión de datos (*Data Ingestion*).
#     - Almacenamiento de datos (*Data Storage*).
#     - Procesamiento, análisis y consulta de datos (*Data Processing / Data Query*).
#     - Visalización de datos (*Data Visualization*).

# ## Ingestión de datos

# - Obtención, procesado (separación, agrupación, filtrado) y limpieza de datos (eliminar duplicados y errores). 
# - Es el primer paso donde se obtienen los datos que provienen de varias fuentes y que irán a dispositivos de almacenamiento para su posterior acceso, uso y análisis por parte de la organización.
# - En esta etapa los datos son priorizados y categorizados.

# - Su destinación es generalmente:
#     - Un *data warehouse* (*Snowflake, Amazon Redshift, Google BigQuery, Azure Synapse*), o
#     - Un *data lake* (*Databricks*) con datos estructurados, semi estructurados y no estructurados.

# ## Cuestiones a considerar

# - Velocidad de la entrada de datos (frecuencia: *Batch, Real-Time*).
# - Volumen de los datos.
# - Variedad (formato: datos estructurados, Semi-estructurados, no estructurados).

# - Otras cuestiones a tener en cuenta son la veracidad de esos datos (si son confiables) y el valor de los mismos. 

# - La velocidad de datos se ocupa de la velocidad a la que fluyen los datos desde diferentes fuentes, como máquinas, redes, IoT, interacción humana, sitios de medios, redes sociales.
# - El movimiento de datos puede ser masivo o continuo en la ingestión de datos. 

# - El volumen de los datos gestionados puede ser enorme.
# - Los datos son generados desde diversas fuentes. 
# - Éstas pueden aumentar cada día tanto en cantidad como en volumen de datos.

# - Frecuencia de datos:
# - Los datos se pueden procesar en tiempo real o por lotes.
# - En tiempo real, el procesamiento ocurre cuando los datos se reciben al mismo tiempo que se generan.
# - Los datos por lotes se almacenan mediante un proceso por lotes fijo en algún intervalo de tiempo y luego se trasladan al flujo del proceso de administración de datos. 

# - La ingestión de datos se puede realizar utilizando formatos de distinto tipo.
#     - Datos estructurados (formato tabular). 
#     - Semi-estructurados (ficheros JSON, CSV, etc.). 
#     - No estructurados (imágenes, audio, video, etc.).

# Fuente: {cite:ps}`Dumbill2012`

# ## Buenas prácticas en ingestión de datos

# - Ancho de banda de la red:
# - El flujo de datos (*Data Pipeline*) debe poder competir con el tráfico comercial.
# - A veces el tráfico aumenta o disminuye, por lo que la escalabilidad del ancho de banda de la red es el mayor desafío del *Data Pipeline*.
# - Se requieren herramientas de ingestión de datos que permitan la limitación y compresión del ancho de banda en base a las necesidades del momento. 

# - Soporte para red no confiable:
# - La canalización en la ingestión de datos toma datos con múltiples estructuras, es decir, archivos de texto, datos de archivos tabulares, archivos XML, archivos de registro, etc. y debido a la velocidad variable de los datos que llegan, es posible que viajen a través de una red poco confiable.
# - La implementación del flujo de datos o *Data Pipeline* también debería ser capaz de soportar esto. 

# - Transmisión de datos:
# - Las mejores prácticas de ingestión de datos dependen de la necesidad empresarial, ya sea para procesar los datos por lotes, flujos o en tiempo real.
# - En ocasiones, es posible que se necesiten todos a la vez para el procesamiento a través de la canalización de ingesta de datos, por lo que las herramientas deben ser capaces de admitirlos. 

# - Tecnologías y Sistemas Heterogéneos:
# - Las herramientas para la canalización de la ingesta de datos deben poder utilizar diferentes tecnologías de fuentes de datos y diferentes sistemas operativos. 

# - Elección del formato de datos correcto:
# - Las herramientas de ingesta de datos deben proporcionar un formato de serialización de datos, lo que significa que, dado que los datos vienen en formatos variables, los convierte a un solo formato para proporcionar una forma más fácil de comprenderlos o relacionarlos. 

# - Repositorio único:
# - El análisis crítico es más efectivo cuando se combinan datos de múltiples fuentes.
# - Para la toma de decisiones de negocio, se debe tener un repositorio único para todos los datos que llegan. 

# - Integraciones:
# - Todo el tiempo los datos siguen aumentando en el proceso de ingesta de datos, llegan datos nuevos y se modifican los datos antiguos, por lo cual a veces cada nueva integración puede tardar entre unos días y unos meses en completarse. 

# - Alta precisión:
# - La única forma de generar confianza con los datos es asegurarse de que los datos son auditables.
# - Una buena práctica que es fácil de implementar es nunca descartar entradas o formularios intermedios al modificar datos en el flujo del proceso de ingesta de datos. 

# - Latencia:
# - Cuanto más actualizados sean los datos, más ágil puede ser la toma de decisiones en la organización, pero hay un coste a considerar.
# - La extracción de datos de APIs y bases de datos en tiempo real puede ser difícil, y muchas fuentes de datos de destino, incluidos grandes almacenes de objetos como Amazon S3 y bases de datos de análisis como Amazon Redshift, están optimizadas para recibir datos en fragmentos en lugar de una secuencia. 

# - Mantener la escalabilidad:
# - La ingesta de datos se puede aumentar o disminuir durante algunos períodos de tiempo.
# - El uso y tratamiento de los datos no es uniforme.
# - Se debe hacer que la canalización sea tan escalable que pueda manejar cualquier cantidad de datos que lleguen a una velocidad variable. 

# ## Herramientas para la ingesta de datos

# - Apache Flume
#    - Un servicio distribuido, confiable y de alta disponibilidad que colecta, agrupa y mueve eficientemente grandes cantidades de logs y datos.
#    - Extraído de: <https://flume.apache.org/>.

# - Es robusto y tolerante a fallas con mecanismos de confiabilidad ajustables.
# - Cuenta también con mecanismos de conmutación por error y recuperación.
# - Utiliza un modelo de datos extensible simple que permite la aplicación analítica en línea. 

# - Un evento Flume se define como una unidad de flujo de datos que tiene una carga útil de bytes y un conjunto opcional de atributos de cadena.
# - Un agente de Flume es un proceso (JVM) que aloja los componentes a través de los cuales fluyen los eventos desde una fuente externa hasta el siguiente destino (salto). 

# - Una fuente de Flume consume eventos que le envía una fuente externa como por ej. un servidor web.
# - La fuente externa envía eventos a Flume en un formato que es reconocido por la fuente de destino de Flume. 

# - Extraído de: <https://flume.apache.org/releases/content/1.9.0/FlumeUserGuide.html>.

# - Apache Nifi
#     - Es una de las mejores herramientas de *data ingestion* del mercado. 
#     - Proveee un sistema fácil de usar, poderoso y confiable para procesar y distribuir datos.
#     - Extraído de: <https://nifi.apache.org/>.

# - Documentación: <https://nifi.apache.org/docs/nifi-docs/html/getting-started.html>.
# - Caso de uso: *Best practices and lessons learnt from Running Apache NiFi at Renault*  
# <https://fr.slideshare.net/Hadoop_Summit/best-practices-and-lessons-learnt-from-running-apache-nifi-at-renault>.

# - Apache Flink
#     - Framework utilizado para el procesamiento de flujos distribuidos (*distributed stream*) que facilita resultados precisos, aún en el caso de datos que están desordenados o que llegan con retraso en la distribución.
#     - Extraído de: <https://flink.apache.org/>.

# - Elastic Logstash
#     - Tubería (*pipeline*) de procesamiento de datos del lado del servidor de código abierto que ingiere datos de una multitud de fuentes, los transforma simultáneamente y luego los envía al reservatorio (*stash*), por ejemplo Elasticsearch. 
#     - Extraído de: <https://www.elastic.co/>.

# - Apache Beam
#     - Es un modelo de programación unificado que permite implementar trabajos de procesamiento de datos por lotes y de *streaming* en cualquier motor de ejecución.
#     - Lee los datos desde diversas fuentes, ejecuta la lógica del negocio para *batch* y *streaming*, y finalmente los deposita en las soluciones de almacenamiento disponibles.
#     - Una canalización de Beam puede ejecutarse en los sistemas de procesamiento de datos distribuidos más populares, como Spark, Flink o Samza.

# - Apache Samza 
#     - Permite crear aplicaciones con estado que procesan datos en tiempo real desde múltiples fuentes, incluido Apache Kafka.
#     - Admite opciones de implementación flexibles para ejecutarse en YARN o como una biblioteca independiente.
#     - Tutorial: <https://samza.apache.org/startup/hello-samza/1.6.0/>.
#     - Fuente: <https://samza.apache.org/>.

# - Fivetran es una cloud-based platform para ETL. 
#     - <https://www.fivetran.com/>.
# - Stitch Data Loader mueve más de 130 tipos de fuentes al *data warehouse*.
#     - <https://www.stitchdata.com/>.
# - Airbyte es una herramienta open-source de integración de datos. 
#     - <https://airbyte.com/>.

# ## Sistemas de mensajería

# - Apache Kafka
#     - Es una plataforma de transmisión de eventos distribuidos de código abierto utilizada por miles de empresas para canalizaciones de datos de alto rendimiento, análisis de streaming, integración de datos y aplicaciones de misión crítica.
#     - Es también un sistema de mensajería escalable que permite a los usuarios publicar y consumir grandes cantidades de mensajes en tiempo real por suscripción.
#     - Extraído de: <https://kafka.apache.org/>. 

# - La transmisión de eventos es el equivalente digital del sistema nervioso central del cuerpo humano.
# - Es la base tecnológica para el mundo 'siempre activo' donde las empresas están cada vez más definidas por software y automatizadas, y donde el usuario de software es más software (Inteligencia Artificial). 

# - Técnicamente hablando, la transmisión de eventos es la práctica de capturar datos en tiempo real de fuentes de eventos como bases de datos, sensores, dispositivos móviles, servicios en la nube y aplicaciones de software en forma de flujos de eventos; almacenar estos flujos de eventos de forma duradera para su posterior recuperación; manipular, procesar y reaccionar a los flujos de eventos en tiempo real y retrospectivamente; y enrutar los flujos de eventos a diferentes tecnologías de destino según sea necesario.

# - La version comercial de Apache Kafka es Confluent <https://www.confluent.io/es-es/>.
# - Otro *broker* de mensajería es RabbitMQ <https://www.rabbitmq.com/>.

# - Apache ActiveMQ
#     - Es el sistema de mensajería multi protocolo open source más popular del mercado. 
#     - Se conecta a clientes escritos en JavaScript, C, C++, Python, .Net, y más.
#     - Integra aplicaciones multiplataforma utilizando el protocolo AMQP. 
#     - Intercambia mensajes mediante STOMP sobre *websockets*, gestiona dispositivos IoT con MQTT. 
#     - Soporta la infraestructura JMS (*Java Message Service*). 

# - Fuente: <https://activemq.apache.org/>

# - Apache Pulsar
#     - Apache Pulsar es una plataforma de eventos distribuidos cloud similar a Kafka originalmente creada por Yahoo!
#     - <https://pulsar.apache.org/>.
#     - La versión comercial de sus creadores es StreamNative <https://streamnative.io/>.

# - Pub/Sub
#     - Es un sistema de mensajería que combina la escalabilidad horizontal de Apache Kafka y Pulsar con funciones del middleware como colas y filtros de mensajes no entregados de Apache ActiveMQ y RabbitMQ.
#     - Se complementa con Dataflow, que controla la anulación de mensajes duplicados, el procesamiento “solo una vez” y generación de marcas de agua a partir de eventos con marcas de tiempo. 
#     - Para usar Dataflow se escribe la canalización con el SDK de Apache Beam y luego se ejecuta.
#     - <https://cloud.google.com/pubsub/docs/overview>

# ## Problemas en la ingesta de datos

# - Cuando existen numerosas fuentes de Big Data con diferentes formatos, el mayor desafío para el negocio es ingerir datos a una velocidad razonable y procesarlos de manera eficiente.
# - De esta manera los datos pueden priorizarse y en consecuencia mejorar la toma de decisiones de negocio. 

# - Las fuentes de datos, las herramientas de ingestión de datos y las aplicaciones de consumo evolucionan permanentemente durante el proceso de ingestión de datos.
# - Los datos pueden modificar sus atributos sin previo aviso independientemente de la aplicación utilizada. 

# - Detección y captura de datos modificados: esta tarea es difícil, no solo por la naturaleza semiestructurada o no estructurada de los datos.
# - También lo es por tratar con baja latencia (una red informática que está optimizada para procesar un volumen muy alto de mensajes de datos con un retraso mínimo).
# - Estas redes están diseñadas para admitir operaciones que requieren acceso casi en tiempo real a datos que cambian rápidamente. 

# ## Modelo semántico de datos (SDM) 

# - El modelo semántico de datos (SDM) también cambia con el tiempo.
# - Se necesita un modelo de datos (*DM*) en el que se incluya información semántica.
# - Un *DM* que incluya la capacidad de expresar e intercambiar información permite a las partes interpretar el significado (semántica) de las instancias. 

# - Extraído de: Semantic Data Model: <https://es.wikipedia.org/wiki/Modelo_sem%C3%A1ntico_de_datos>.

# - En un modelo semántico los hechos generalmente se expresan mediante relaciones binarias entre elementos de datos, mientras que las relaciones de orden superior se expresan como colecciones de relaciones binarias.
# - Típicamente las relaciones binarias tienen la forma de ternas: Objeto-<Tipo de Relación>-Objeto. 
# - Por ejemplo: La Torre Eiffel `<se encuentra en>` París. 

# - Según el conocido trabajo seminal de Smith y Smith (1977), tres abstracciones son muy importantes para el modelado de datos:
#      - Clasificación: modelo instancia_de_relaciones.
#      - Agregación: modelo tiene_relaciones.
#      - Generalización: modelo es_unas_relaciones. 

# - Extraído de: Semantic Data Modelling: <http://www.jhterbekke.net/SemanticDataModeling.html>.

# - Integridad de datos: las especificaciones del modelo de datos implican la validez de ciertas reglas de integridad.
# - Relatividad: cada atributo en una definición de tipo está relacionado con uno y solo un tipo con el mismo nombre, mientras que cada tipo puede corresponder con varios atributos en otros tipos.
# - Convertibilidad: Cada definición de tipo es única: no hay definiciones de tipo que lleven el mismo nombre o la misma colección de atributos. 

# In[1]:


database warehouse.

base description (A16).
type product kind (A8) = description.

base color (A10).
base stock (I8).
base price (R4,2).
type product (I7) = description, color, stock, price, product kind.

base company name (A20).
base address (A20).
base zip (A6).
base city (A16).
type supplier (A8) = company name, address, zip, city.

type purchased product (A9) = supplier, product, price.

…

base prepaid (R4,2).
type sale (A7) = sold product, quantity, price, customer, date, prepaid.

end.


# - Artículo Semantic (Big) Data Analysis: An Extensive Literature Review.
#     - <https://latamt.ieeer9.org/index.php/transactions/article/download/673/207>.

# ## Almacenamiento de datos (Data Storage)

# - El almacenamiento se convierte en un desafío cuando el tamaño de los datos es muy grande. 
# - Varias posibles soluciones pueden ayudar a resolver este problema.
# - Encontrar la solución de almacenamiento más eficiente es el objetivo de este paso.

# - Se necesitan diferentes tipos de bases de datos para manejar las diferentes variedades de datos, pero el uso de las mismas crea una sobrecarga en el sistema.
# - Es por este motivo que hay un nuevo concepto en el mundo de las bases de datos: la persistencia políglota. Es la idea de usar múltiples bases de datos para impulsar una sola aplicación.
#     - <https://en.wikipedia.org/wiki/Polyglot_persistence>

# - La persistencia políglota es la forma de compartir o dividir los datos en múltiples bases de datos y aprovechar su poder juntas.
#      - Relacionales
#      - No SQL
#      - Gráficas
#      - En memoria 

# - Polyglot Persistance tiene tiempos de respuesta más rápidos.
# - Las bases de datos NoSQL escalan bien cuando se modelan correctamente para los datos que se desean almacenar.
# - La experiencia de usuario es mejor cuando se aprovecha el poder de múltiples bases de datos al mismo tiempo.
# - Por ejemplo, si desea buscar productos en una aplicación de comercio electrónico, se utiliza ElasticSearch, que devuelve los resultados en función de la relevancia, lo que MongoDB no puede hacer fácilmente. 

# - Como contrapartida, tiene como desventaja la necesidad de contratar personal especializado para la integración de las bases de datos y una mayor cantidad de recursos de almacenamiento.

# ## Herramientas de almacenamiento para Big Data

# - HDFS : Hadoop Distributed File System.
# - Ozone: Un *object store* para Hadoop, la próxima generación de HDFS.
# - GlusterFS: Sistema de archivos distribuido confiable.
# - Ceph: Proporciona almacenamiento de objetos, bloques y sistemas de archivos en un solo clúster.
# - Cloud storage: Amazon S3 Storage Service, IBM Cloud Object Storage, Azure Blob Storage, Google Cloud Storage.

# ## HDFS

# - HDFS es un sistema de ficheros basado en Java que provee almacenamiento confiable y escalable.
# - Fue diseñado para abarcar grandes grupos de servidores básicos (commodity servers).
# - HDFS contiene una gran cantidad de datos y proporciona un acceso a los mismos de manera sencilla y fácil.
#     - Extraído de: <https://hadoop.apache.org/docs/current/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html>.

# - Para almacenar una inmensa cantidad de datos, los ficheros son guardados en varias máquinas. 
# - Estos ficheros son guardados de forma redundante para poder rescatar el sistema en caso de pérdida de datos a causa de fallos.

# - HDFS también proporciona la disponibilidad de aplicaciones para procesamiento en paralelo durante el paso de ingestión de datos. 
# - HDFS fue construido para soportar aplicaciones con grandes conjuntos de datos, incluyendo ficheros con terabytes de tamaño.

# - Utiliza una arquitectura maestro/esclavo, en la que cada clúster consta de un solo *Namenode* que administra las operaciones del sistema de archivos y admite *Datanodes* que administran el almacenamiento de datos en nodos de cómputo individuales. 

# - Cuando HDFS toma datos, divide la información en partes separadas y las distribuye a diferentes nodos en un clúster, lo que permite el procesamiento paralelo. 
# - El sistema de archivos en Ingestión de datos también copia cada pieza de datos varias veces y distribuye las copias a nodos individuales, colocando al menos una copia en un rack de servidor diferente. 

# ## Apache Ozone

# - Ozone es un *object store* escalable, redundante, y distribuído para Hadoop. 
# - Además de escalar a billones de objetos de cualquier tamaño, Ozone puede trabajar puede funcionar de manera efectiva en entornos en contenedores como Kubernetes y YARN.
#     - Extraído de: <https://ozone.apache.org/>. 

# - Aplicaciones que utilizan frameworks como Apache Spark, YARN y Hive trabajan de forma nativa sin modificaciones.
# - Ozone está construido en una capa de almacenamiento en bloques altamente disponible y replicada llamada *Hadoop Distributed Data Store (HDDS)*.
# - Ozone viene un una biblioteca cliente para Java, soporte para el protocolo S3, y una interfaz de línea de comandos.

# - Ozone consta de volúmenes, cubos (*buckets*) y claves:
#     - Los volúmenes son similares a las cuentas de usuario. Solo los administradores pueden crear o eliminar volúmenes.
#     - Los cubos son similares a los directorios. Un cubo puede contener cualquier cantidad de claves, pero los cubos no pueden contener otros cubos.
#     - Las claves son similares a los archivos. 

# ## GlusterFS

# - Gluster es un sistema de ficheros en red escalable libre y de fuente abierta.
#     - Extraído de: <https://docs.gluster.org/en/latest/> | <https://www.gluster.org/>

# - Los sistemas de almacenamiento de escalamiento horizontal basados en GlusterFS son adecuados para datos no estructurados, como documentos, imágenes, archivos de audio y video, y archivos de registro. 
# - Con esto, podemos crear grandes soluciones de almacenamiento distribuido para transmisión de medios, análisis de datos, ingesta de datos y otras tareas intensivas en datos y ancho de banda.

# - La arquitectura GlusterFS agrega recursos informáticos, de almacenamiento y de E/S en un espacio de nombres global.
# - Cada servidor más el almacenamiento básico adjunto (configurado como almacenamiento adjunto directo, JBOD o utilizando una red de área de almacenamiento) se considera un nodo.
#      - Extraído de: <https://en.wikipedia.org/wiki/Gluster>. 

# - La capacidad se escala agregando nodos adicionales o agregando almacenamiento adicional a cada nodo.
# - El rendimiento aumenta al implementar el almacenamiento entre más nodos.
# - La alta disponibilidad se logra mediante la replicación de datos de *n* vías entre nodos.

# ## Ceph

# - La base de Ceph es el *Reliable Autonomic Distributed Object Store (RADOS)*
# - Proporciona a las aplicaciones almacenamiento de objetos, bloques y sistemas de archivos en un solo clúster de almacenamiento unificado.
# - Esto lo hace altamente confiable y fácil de gestionar.
#     - Extraído de: <https://ceph.io/>

# - El algoritmo CRUSH de Ceph libera a los clústeres de almacenamiento de las limitaciones de escalabilidad y rendimiento impuestas por el mapeo de tablas de datos centralizados.
# - Replica y reequilibra los datos dentro del clúster de forma dinámica, eliminando esta tediosa tarea para los administradores, al tiempo que ofrece escalabilidad infinita y alto rendimiento.

# - Recursos:
#     - Democratising Data Storage. DIGITAL REPORT 2021:
#     - <https://ceph.io/assets/pdfs/report-dec2021.pdf>.
#     - Ceph Quickstart: <https://rook.io/docs/rook/v1.8/quickstart.html>.

# ## Amazon Services

# - Amazon Simple Storage Service (Amazon S3) es un almacenamiento de objetos con una interfaz web simple que permite almacenar y recuparar cualquier volumen de datos desde cualquier lugar en Internet.
# - Está diseñado para entregar un 99.999% de durabilidad y escalar a más de trillones de objetos en todo el mundo.
#     - Extraído de: <https://aws.amazon.com/free/storage/s3/>.

# - Amazon Redshift es un servicio de *data warehouse* en la nube.
# - Utiliza SQL para analizar datos estructurados y semiestructurados en almacenamientos de datos, bases de datos operativas y lagos de datos, con hardware y machine learning diseñado por AWS.  
# - Redshift permite guardar los resultados de las consultas en el *S3 data lake* utilizando formatos abiertos como Apache Parquet para su posterior análisis con Amazon EMR, Amazon Athena, y Amazon SageMaker.
#     - Extraído de: Amazon Redshift <https://aws.amazon.com/redshift/>

# - Todos los servicios de Amazon para análisis en Amazon:
#     - <https://aws.amazon.com/es/big-data/datalakes-and-analytics/>

# ## Microsoft Azure Data Lake Store

# - Lago de datos seguro y escalable de forma masiva para sus cargas de trabajo de análisis de alto rendimiento.
# - Fuente: <https://azure.microsoft.com/es-es/services/storage/data-lake-storage/>.
# - Soluciones en Big Data: <https://azure.microsoft.com/es-es/solutions/big-data/>.

# - Microsoft Azure Data Lake Analytics
# - Servicio de análisis en la nube para desarrollar y ejecutar fácilmente programas de procesamiento y transformación de petabytes de datos en paralelo de forma masiva con los lenguajes U-SQL, R, Python y .NET. 
# - Sin infraestructura para administrar, se procesan los datos a petición, escalando las unidades de análisis de forma instantánea.
# - Fuente: <https://azure.microsoft.com/es-es/services/data-lake-analytics/#overview>.

# ## Google BigQuery

# - Almacén de datos multinube de alta escalabilidad, rentable y sin servidor.
#     - <https://cloud.google.com/bigquery>.

# - Google Cloud Smart Analytics Platform:
# - Es una plataforma de analíticas flexible, abierta y segura que ayuda a convertirse en una organización basada en la inteligencia. 
# - Se basa en décadas de innovación de Google en el sector de la inteligencia artificial y en el desarrollo de servicios a escala de Internet. 
#     - Extraído de <https://cloud.google.com/solutions/smart-analytics>.

# ## Databricks

# - Fundada en 2013 por los creadores originales de Apache Spark, Delta Lake y MLflow, Databricks reúne ingeniería de datos, ciencia y análisis en una plataforma abierta y unificada para que los equipos de datos puedan colaborar e innovar más rápido. 
# - Está alojada en Microsoft Azure.
#     - Fuente: <https://databricks.com/>.

# ## Snowflake

# - Permite acceder, integrar y analizar datos de manera fácil y segura con una escalabilidad casi infinita, habilitada automáticamente o sobre la marcha.
# - Está alojada en Amazon AWS.
#     - Fuente: <https://www.snowflake.com/>.

# ## NoSQL databases

# - Las bases de datos NoSQL, (no solo SQL) o no relacionales, se utilizan mayoritariamente para la recopilación y análisis de Big Data.
# - Permiten la organización dinámica de datos no estructurados.
# - Las bases de datos relacionales, por otro lado, tienen un diseño estructurado y tabular.

# - Existen diversos tipos de bases de datos No SQL:
#     - Bases de datos de documentos (MongoDB, Couch DB)
#     - Pares de valores (Amazon DynamoDB, Redis)
#     - Columnares (Apache Cassandra, Apache HBase)
#     - Gráficas (Neo4j, Stardog)

# ## Bases de datos de documentos

# ## MongoDB

# - MongoDB es una base de datos distribuida de propósito general, basada en documentos, creada para desarrolladores de aplicaciones modernas y para la era de la nube.
# - MongoDB es una base de datos de documentos, lo que significa que almacena datos en documentos similares a JSON. 
#     - Fuente: <https://www.mongodb.com/>.

# ## Apache CouchDB

# - Apache CouchDB es una base de datos NoSQL orientada a documentos de código abierto, implementada en Erlang.
# - CouchDB usa múltiples formatos y protocolos para almacenar, transferir y procesar sus datos.
# - Utiliza JSON para almacenar datos, JavaScript como lenguaje de consulta usando MapReduce, y HTTP para una API. 

# - El protocolo *Couch Replication* permite que los datos fluyan sin problemas entre los clústeres de servidores y los teléfonos móviles / navegadores web.
#     - Fuente: <https://couchdb.apache.org/>.

# ## Couchbase

# - Couchbase es una base de datos en la nube NoSQL distribuida.
# - Ofrece versatilidad, rendimiento, escalabilidad y un valor financiero inigualables en implementaciones informáticas en la nube, en las instalaciones híbridas, en la nube distribuida y en edge computing.
#     - Fuente: <https://couchbase.com/>.

# ## Bases de datos con pares de valores

# ## Redis database

# - Redis es un almacén de estructura de datos en memoria de código abierto (con licencia BSD), que se utiliza como base de datos, caché y agente de mensajes.
#     - Fuente: <https://redislabs.com/>.

# ## Bases de datos columnares

# ## Apache Cassandra

# - Apache Cassandra es una base de datos distribuida NoSQL de código abierto.
# - La escalabilidad lineal y la tolerancia a fallas comprobada en hardware básico o infraestructura en la nube la convierten en la plataforma perfecta para datos de misión crítica.
# - El soporte de Cassandra para la replicación en múltiples centros de datos es el mejor en su clase, lo que proporciona una latencia más baja para sus usuarios. 
#     - Fuente: <https://cassandra.apache.org/>.

# ## Apache HBase

# - Es una base de datos distribuida no relacional open source modelada en base al artículo científico *Google's Bigtable: A Distributed Storage System for Structured Data* de Chang et al.

# - Así como Bigtable aprovecha el almacenamiento de datos distribuido proporcionado por el sistema de archivos de Google, Apache HBase proporciona capacidades similares a las de Bigtable junto con Hadoop y HDFS.
#     - Extraído de: Apache HBase Docs & website: <https://hbase.apache.com/>. 

# ## Bases de datos gráficas

# ## Amazon Neptune

# - Amazon Neptune es un motor de base de datos de gráficos de alto rendimiento optimizado para almacenar miles de millones de relaciones y consultar el gráfico con una latencia de milisegundos. 
# - Admite los modelos de gráficos populares Property Graph y Resource Description Framework (RDF) del W3C, así como sus lenguajes de consulta asociados, Apache TinkerPop Gremlin y SPARQL.
#     - Fuente: <https://aws.amazon.com/es/nosql/graph/>.
#     - <https://aws.amazon.com/es/neptune/>.

# ## Stardog

# - Stardog es la única plataforma de gráficos que conecta datos en la capa de cómputo en lugar de la capa de almacenamiento. 
# - No se necesita migrar las bases de datos ni copiarlas. 
# - Los conectores facilitan la virtualización de datos en Stardog y consultan los datos conectados mediante aplicaciones, herramientas de BI y más. 
#     - Fuente: <https://www.stardog.com/>.

# - Cómo funcionan los gráficos de conocimiento: 
#     - <https://www.stardog.com/knowledge-graph/>.
# - Tutorial Stardog:
#     - <https://www.stardog.com/tutorials/getting-started-1>.

# ## Neo4j

# - Neo4j permite construir aplicaciones y flujos de trabajos de ML.
# - Almacena y administra datos manteniendo relaciones que brindan consultas veloces, un contexto más profundo para el análisis y un modelo de datos modificable sin complicaciones.
#     - Fuente: <https://neo4j.com/>.

# ## Procesamiento, análisis y consulta de datos 

# - Los datos recolectados en la fase anterior serán procesados en este paso. 
# - Aquí, el sistema de procesamiento de canalización de datos enruta los datos a un destino diferente, clasifica el flujo de datos y es el primer punto donde puede tener lugar el análisis.
# - Esta es la capa donde las consultas (*queries*) y el proceso analítico activo se ejecutan.

# - Para ello, los analistas emplean diferentes herramientas y estrategias como, por ejemplo:
#     - Modelado estadístico
#     - Algoritmos
#     - Inteligencia artificial (AI)
#     - Minería de datos
#     - Aprendizaje automático (ML)

# - Para análisis fuera de línea, se utiliza un sistema de procesamiento por lotes simple. 
# - Apache Sqoop es la aplicación que se encarga de esto.
# - Transfiere eficientemente datos estructurados entre Apache Hadoop y las bases de datos relacionales.
# - Spark por otro lado, es utilizado mayoritariamente para el análisis y procesamiento de datos en tiempo real.
# - Otra herramienta conocida pero menos utilizada es Apache Storm.
#     - Extraído de: <https://sqoop.apache.org/>.

# - KNIME hace que la comprensión de datos y el diseño de flujos de trabajo de ciencia de datos y componentes reutilizables sean accesibles para todos.
#     - <https://www.knime.com/>.
# - Apache Mahout es un framework distribuido de álgebra linear y Scala DSL matemáticamente expresivo.  
#     - <https://mahout.apache.org/>.
# - Weka 3: Machine Learning Software en Java para hacer análisis simple.
#     - <https://www.cs.waikato.ac.nz/ml/weka/>.

# ## Apache Sqoop (in the Attic) 

# - Transfiere eficientemente datos estructurados entre Apache Hadoop y las bases de datos relacionales.
#     - Extraído de: <https://sqoop.apache.org/>.

# - Se puede usar Sqoop para importar datos desde un sistema de administración de bases de datos relacionales (RDBMS) como MySQL, Oracle, o un mainframe al sistema de archivos distribuidos de Hadoop (HDFS), transformar los datos utilizando Hadoop MapReduce, y luego exportar los datos nuevamente a un RDBMS.

# ## Apache Spark

# - Framework de procesamiento paralelo y de código abierto para ejecutar aplicaciones de análisis de datos a gran escala en sistemas agrupados.
#     - Extraído de: <https://spark.apache.org/>.

# - Se utiliza para realizar trabajos informáticos con grandes cargas de datos junto a Apache Kafka. 
# - Fue desarrollado en la University of California, Berkeley.
# - Con Spark ejecutándose en Apache Hadoop YARN, los desarrolladores pueden crear aplicaciones para explotar el poder de Spark, obtener información y enriquecer sus cargas de trabajo de ciencia de datos dentro de un único conjunto de datos compartidos en Hadoop.

# ## Apache Storm

# - Es un sistema distribuido open source para procesar datos en tiempo real durante la ingesta de datos. 
# - Es escalable, tiene tolerancia a fallos, y es fácil de configurar y operar.
# - Facilita el procesamiento confiable de flujos ilimitados de datos, haciendo para el procesamiento en tiempo real lo que Hadoop hizo para el procesamiento por lotes.
#     - Extraído de: <https://storm.apache.org/>.

# - Casos de uso:
#     - Análisis en tiempo real
#     - Aprendizaje automático
#     - Monitoreo continuo de operaciones
#     - RPC distribuido, ETL, y más.

# ## Visualización de datos (Big Data Visualization)

# - La fase de visualización o presentación es donde los usuarios pueden sentir el VALOR de los DATOS. 
# - La visualización de hallazgos ayuda a tomar mejores decisiones de negocios.
# - Aquí se generan informes por tipo de audiencia (comerciales, marketing, estrategia, técnicos, etc).

# ## Elastic Stack

# - Elasticsearch es el componente central de Elastic Stack, un conjunto de herramientas de código abierto para la ingesta, el enriquecimiento, el almacenamiento, el análisis y la visualización de datos.
# - El ELK Stack se compone de las aplicaciones Elasticsearch, Logstash, Kibana, y Beats.
# - Actualmente se lo conoce como Elastic Stack, nombre que le permite agregar nuevas funcionalidades.
# - Kibana es la interfaz de usuario gratuita y abierta que permite visualizar los datos.

# - Fuente: <https://www.elastic.co/what-is/elasticsearch>.

# - Casos de uso:
#     - Búsqueda de aplicaciones
#     - Búsqueda de sitio web
#     - Búsqueda Empresarial
#     - Logging y analíticas de log
#     - Métricas de infraestructura y monitoreo de contenedores
#     - Monitoreo de rendimiento de aplicaciones
#     - Análisis y visualización de datos geoespaciales
#     - Analítica de Seguridad
#     - Analítica de Negocios

# ## Salesforce, Google y Microsoft

# - Otras herramientas de modelización y visualización de datos son las proporcionadas por Salesforce, Google y Microsoft.
# - Salesforce adquirió Tableau y google hizo lo mismo con Looker en 2019.
# - La reciente integración entre estos productos le permitirán al usuario modelar datos con LookML y usar Tableau, o Looker para explorar ese modelo.

# - <https://looker.com/google-cloud>.
# - <https://www.tableau.com/>.

# - Microsoft cuenta por su parte con PowerBI.
#     - <https://powerbi.microsoft.com/es-es/>.

# ## Monitoreo de datos

# - El seguimiento continuo de los datos es una parte importante de los mecanismos de gobernanza.
# - Apache Flume es útil para procesar datos de registro.
# - Apache Storm se utiliza para el monitoreo de operaciones.
# - Apache Spark sirve para transmisión de datos, procesamiento de gráficos y aprendizaje automático.
# - El monitoreo puede ocurrir en el paso de almacenamiento de datos.

# ## Herramientas para Big Data

# ## Apache Mesos

# - Un núcleo (*kernel*) de sistemas distribuidos.
# - Mesos está construido usando los mismos principios que el *kernel* de Linux, solo que en un nivel diferente de abstracción.
# - abstrae la CPU, la memoria, el almacenamiento y otros recursos informáticos de las máquinas (físicas o virtuales), lo que permite que los sistemas distribuidos elásticos y tolerantes a fallas se construyan fácilmente y se ejecuten de manera efectiva.

# - El *kernel* de Mesos se ejecuta en todas las máquinas y proporciona aplicaciones (p. ej., Hadoop, Spark, Kafka, Elasticsearch) y una API para la gestión y programación de recursos para todo el centro de datos y entornos de nube.
#     - Extraído de: <https://mesos.apache.org/>.

# ## Apache Zookeeper

# - ZooKeeper es un servicio centralizado para mantener la información de configuración, nombrar, brindar sincronización distribuida y servicios grupales.
#     - Extraído de: <https://zookeeper.apache.org/>. 

# ## Apache Ambari (in the Attic) 

# - El proyecto Apache Ambari tiene como objetivo simplificar la administración de Hadoop mediante el desarrollo de software para el aprovisionamiento, la administración y el monitoreo de clústeres de Apache Hadoop.
# - Ambari proporciona una interfaz de usuario web de administración de Hadoop intuitiva y fácil de usar respaldada por sus API RESTful. 
#     - Extraído de: <https://ambari.apache.org/>. 

# ## Apache Ranger

# - Apache Ranger™ es un framework para habilitar, monitorear y administrar la seguridad integral de los datos en toda la plataforma Hadoop.
#     - Extraído de: <https://ranger.apache.org/>. 

# ## Apache Sentry

# - Apache Sentry™ es un sistema para hacer cumplir la autorización detallada basada en roles para datos y metadatos almacenados en un clúster de Hadoop.
#     - Extraído de: <https://sentry.apache.org/>. 

# ## Apache Airflow

# - Apache Airflow es una plataforma que permite crear, programar temporalmente, y monitorar flujos de trabajo utilizando Python como lenguaje.
# - Automatiza la ingestas de datos, acciones de mantenimiento periódicas y realiza tareas de administración.
#     - Extraído de: <https://airflow.apache.org/>. 

# - Un flujo de trabajo de ejemplo puede ser:
#     - Obtener datos de una base de datos relacional como PosgreSQL para enviarlos a Kafka. 
#     - Transformar los datos con Apache Spark y finalmente enviar un mensaje de finalización.
