#!/usr/bin/env python
# coding: utf-8

# # Big Data tema 3

# ## Procesos en Big Data

# - Para proyectos de Big Data los procesos básicamente se pueden dividir en cuatro fases: 
#     - Ingestión de datos (*Data Ingestion*).
#     - Almacenamiento de datos (*Data Storage*).
#     - Procesamiento, análisis y consulta de datos (*Data Processing / Data Query*).
#     - Visalización de datos (*Data Visualization*).

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

# - Las consultas interactivas para el procesamiento de datos son necesarias y es una zona tradicionalmente dominada por desarrolladores expertos en SQL.
# - Con Hadoop, la ingesta de datos, el almacenamiento, el proceso y el análisis se volvieron fáciles de trabajar cuando se cuenta con una gran cantidad de datos. 

# - Para análisis fuera de línea, se utiliza un sistema de procesamiento por lotes simple. 
# - Apache Sqoop es la aplicación que se encarga de esto.
# - Transfiere eficientemente datos estructurados entre Apache Hadoop y las bases de datos relacionales.
# - Spark por otro lado, es utilizado mayoritariamente para el análisis y procesamiento de datos en tiempo real.
# - Otra herramienta pero menos utilizada es Apache Storm.
#     - Extraído de: <https://sqoop.apache.org/>.

# - KNIME hace que la comprensión de datos y el diseño de flujos de trabajo de ciencia de datos y componentes reutilizables sean accesibles para todos.
#     - <https://www.knime.com/>.
# - Apache Mahout es un framework distribuido de álgebra linear y Scala DSL matemáticamente expresivo.  
#     - <https://mahout.apache.org/>.
# - Weka 3: Machine Learning Software en Java para hacer análisis simple.
#     - <https://www.cs.waikato.ac.nz/ml/weka/>.

# - Materialize es una base de datos útil para análisis en tiempo real que ofrece actualizaciones de vista incrementales.
#     - Extraído de: <https://materialize.com/>.

# ## Apache Scoop (Attic)

# - Transfiere eficientemente datos estructurados entre Apache Hadoop y las bases de datos relacionales.
#     - Extraído de: <https://sqoop.apache.org/>.

# - Se puede usar Sqoop para importar datos desde un sistema de administración de bases de datos relacionales (RDBMS) como MySQL u Oracle o un mainframe al sistema de archivos distribuidos de Hadoop (HDFS), transformar los datos en Hadoop MapReduce y luego exportar los datos nuevamente a un RDBMS.
#     

# - Apache Sqoop también puede ser utilizado para extraer datos de Hadoop y exportarlos a almacenes de datos estructurados externos.
# - Apache Sqoop trabaja con bases de datos relacionales como Teradata, Netezza, Oracle, MySQL, Postgres, y HSQLDB.

# - Sqoop automatiza la mayor parte de este proceso, basándose en la base de datos para describir el esquema de los datos que se importarán.
# - Sqoop utiliza MapReduce para importar y exportar los datos, lo cual proporciona procesamiento en paralelo y tolerancia a fallos.

# ## Apache Spark

# - Framework de procesamiento paralelo y de código abierto para ejecutar aplicaciones de análisis de datos a gran escala en sistemas agrupados.
#     - Extraído de: <https://spark.apache.org/>.

# - También es compatible con un amplio conjunto de herramientas de alto nivel, que incluyen:
#     - Spark SQL para SQL y procesamiento de datos estructurados, 
#     - MLlib para aprendizaje automático, 
#     - GraphX para procesamiento de gráficos, y 
#     - Transmisión estructurada para procesamiento incremental y de streaming.

# - Spark SQL incluye un optimizador basado en costes, almacenamiento en columnas y generación de código para agilizar las consultas.
# - Al mismo tiempo, se escala a miles de nodos y consultas de varias horas mediante el motor Spark, que proporciona tolerancia completa a fallas en la mitad de la consulta. 

# - Se utiliza para realizar trabajos informáticos con grandes cargas de datos junto a Apache Kafka. 
# - Fue desarrollado en la University of California, Berkeley.
# - Con Spark ejecutándose en Apache Hadoop YARN, los desarrolladores pueden crear aplicaciones para explotar el poder de Spark, obtener información y enriquecer sus cargas de trabajo de ciencia de datos dentro de un único conjunto de datos compartidos en Hadoop.

# ## Apache Storm

# - Es un sistema distribuido open source para procesar datos en tiempo real durante la ingesta de datos. 
# - Es escalable, tiene tolerancia a fallos, y es fácil de configurar y operar.
# - Facilita el procesamiento confiable de flujos ilimitados de datos, haciendo para el procesamiento en tiempo real lo que Hadoop hizo para el procesamiento por lotes.
#     - Extraído de: <https://storm.apache.org/>.

# - No existe ningún truco que convierta a Hadoop en un sistema en tiempo real.
# - El procesamiento de datos en tiempo real tiene un conjunto de requisitos fundamentalmente diferente al procesamiento por lotes.
# - Apache Storm agrega a Hadoop esta funcionalidad de manera sencilla.

# - Casos de uso:
#     - Análisis en tiempo real
#     - Aprendizaje automático
#     - Monitoreo continuo de operaciones
#     - RPC distribuido, ETL, y más.

# ## Storm vs. Spark

# | Situation | Spark | Storm |
# |------- | ---------------- | -------- | 			
# | Stream processing | Batch processing | Micro-batch processing |
# | Latency | Latency of a few seconds | Latency of milliseconds |
# | Multi-language support | Lesser language support | Multiple language support |
# | Languages | Java – Scala | Java – Scala – Clojure |
# | Stream sources | HDFS | Spout |
# | Resource management | Yarn, Mesos | Yarn, Mesos |
# | Provisioning | Basic using Ganglia | Apache Ambari |
# | Messaging | Netty, Akka | ZeroMQ, Netty |

# ## Apache Impala

# - Impala eleva el nivel de rendimiento de las consultas SQL en Apache Hadoop al mismo tiempo que conserva una experiencia de usuario familiar.
# - Con Impala, se puede consultar datos, ya sea que estén almacenados en HDFS o Apache HBase, incluidas las funciones SELECT, JOIN y agregadas, en tiempo real. 
#     - Extraído de: <https://impala.apache.org/>.

# - Impala utiliza los mismos metadatos, sintaxis SQL (Hive SQL), controlador ODBC e interfaz de usuario (Hue Beeswax) que Apache Hive, lo que proporciona una plataforma familiar y unificada para consultas en tiempo real o por lotes.
# - Los usuarios de Hive pueden utilizar Impala con algunos pocos ajustes.

# ## Apache Kudu

# - Apache Kudu es un motor de almacenamiento columnar open source para datos estructurados.
# - Está diseñado y optimizado para análisis de big data en datos que cambian rápidamente o para un rendimiento rápido en consultas analíticas - OLAP. 
# - Es distribuido, permite varios tipos de partición de datos y carga compartida en varios servidores. 
# - Es parte del ecosistema Hadoop y se integra con frameworks de procesamiento de datos como Spark, Impala y MapReduce.
#     - <https://kudu.apache.org/>

# ## Apache Hive

# - Apache Hive es una infraestructura de almacenamiento de datos construida sobre Apache Hadoop para proporcionar resúmenes de datos, consultas ad-hoc y análisis de grandes conjuntos de datos.
# - Los analistas de datos usan Hive para consultar, resumir, explorar y analizar esos datos, y luego convertirlos en información empresarial procesable. 
#     - Fuente: <https://hive.apache.org/>.

# - El software de almacenamiento de datos Apache Hive facilita la lectura, escritura y administración de grandes conjuntos de datos que residen en almacenamiento distribuido mediante SQL.
# - La estructura se puede proyectar sobre los datos que ya están almacenados.
# - Se proporciona una herramienta de línea de comandos y un controlador JDBC para conectar a los usuarios a Hive.
# - Proporciona un mecanismo para la estructura del proyecto de ingesta de datos en los datos de Hadoop y para consultar esos datos mediante con un lenguaje tipo SQL llamado HiveQL (HQL). 

# ## Apache Drill

# - Es un motor SQL para Hadoop, NoSQL y almacenamiento en la nube.
# - Soporta variadas bases de datos NoSQL y sistemas de ficheros:
# - HBase, MongoDB, HDFS, Amazon S3, Azure Blob Storage, Google Cloud Storage, NAS y ficheros locales.
# - Una única consulta puede obtener datos de múltiples bases de datos.
#     - Fuente: <https://drill.apache.org/>

# ## Presto

# - Motor SQL desarrollado por Facebook para análisis ad-hoc e informes rápidos.
# - Es un motor de consulta SQL distribuido de código abierto que ejecuta consultas analíticas interactivas en fuentes de datos de todos los tamaños, desde gigabytes hasta petabytes.
#     - Fuente: <https://prestodb.io/>

# - Facebook usa Presto para consultas interactivas en varios almacenes de datos internos, incluido su almacén de datos de 300 PB. 
# - Más de 1000 empleados de Facebook usan Presto diariamente para ejecutar más de 30000 consultas que, en total, escanean más de un petabyte por día.

# ## Trino

# - Trino es un motor de consulta SQL distribuido diseñado para consultar grandes conjuntos de datos distribuidos en una o más fuentes de datos heterogéneas.
# - Son los fundadores del proyecto Presto que tuvieron que cambiarle el nombre por cuestiones legales.
#     - Fuente: <https://trino.io/>

# ## Apache Hadoop YARN

# - Tecnología de gestión de clústeres en Hadoop de segunda generación.
# - La idea de YARN es dividir las funcionalidades de gestión de recursos y programación/supervisión de trabajos en servicios separados: un *ResourceManager* (RM) global y un *ApplicationMaster* (AM) por aplicación.
# - Una aplicación es un solo trabajo o un DAG de trabajos.
# - El *ResourceManager* y el *NodeManager* forman el framework de cálculo de datos. 

# - Fuente: <https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html>.

# - El *ResourceManager* arbitra los recursos entre todas las aplicaciones del sistema.
# - El *NodeManager* es el agente del framework por máquina que es responsable de los contenedores, monitorea el uso de sus recursos (cpu, memoria, disco, red) e informa al *ResourceManager/Scheduler*. 

# - La aplicación *ApplicationMaster* es en efecto una biblioteca específica del framework y tiene la tarea de negociar recursos del *ResourceManager* y trabajar con el/los *NodeManager(s)* para ejecutar y monitorear las tareas. 

# ## Otras herramientas

# - Vertica es un almacén de datos (*data warehouse*) de análisis unificado.
# - Ha sido diseñado para ofrecer velocidad, escalabilidad y aprendizaje automático integrado para cargas de trabajo analíticamente intensivas.
#     - Extraído de <https://www.vertica.com/landing-page/start-your-free-trial-today/>.

# - Hue es un asistente open source de SQL para bases de datos y *data warehouses*.
#     - Fuente: <https://gethue.com/>.

# ## Perfilado de datos y linaje

# - Perfilado de datos y linaje (*data profiling and lineage*) son técnicas que permiten identificar la calidad de los datos y su ciclo de vida durante las varias fases que percorren. 
# - Es importante capturar los metadatos en cada paso del proceso para que puedan ser utilizados posteriormente para verificación y personalización.
# - Algunas aplicacione disponibles: Talend, Hive, Pig.

# - Talend Data Fabric es un conjunto de aplicaciones nativas de la nube que lidera la industria en integración y gestión de datos:
#     - Identifica elementos de datos.
#     - Realiza un seguimiento hasta el origen de los datos.
#     - Combina fuentes de datos y enlaces a los mismos.
#     - Crea un mapa para cada sistema y un mapa maestro de la imagen completa. 
#     - Extraído de: <https://www.talend.com/>.

# - OpenLineage es un framework open source para la recopilación y el análisis del linaje de datos
# - Permite una recopilación consistente de metadatos de linaje, creando una comprensión más profunda de cómo se producen y utilizan los datos. 
#     - Extraído de: <https://openlineage.io/>.

# ## Calidad de los datos

# - La ingesta de datos se considera de alta calidad si cumple con las necesidades comerciales y satisface el uso previsto, de modo que sea útil para tomar decisiones de negocio con éxito.
# - Por lo tanto, es un paso importante entender la dimensión de mayor interés e implementar métodos para lograrla.  

# ## Limpieza de datos

# - La limpieza de datos (*data cleansing*) significa implementar varias soluciones para corregir datos incorrectos o corruptos. 

# ## Prevención y pérdida de datos 

# - Deben existir políticas para asegurarse de que se resuelvan las lagunas en la pérdida de datos.
# - La identificación de dicha pérdida de datos necesita un control cuidadoso y procesos de evaluación de la calidad en el flujo del proceso de ingesta de datos. 

# ## Big Data Visualization

# - La fase de visualización o presentación es donde los usuarios pueden sentir el VALOR de los DATOS. 
# - La visualización de hallazgos ayuda a tomar mejores decisiones de negocios.
# - Aquí se generan informes por tipo de audiencia (comerciales, marketing, estrategia, técnicos, etc).

# - Si bien está diseñado para manejar y almacenar grandes volúmenes de datos, Hadoop y otras herramientas no tienen disposiciones integradas para la visualización de datos y la distribución de información, lo que no permite que los usuarios finales del negocio puedan consumir fácilmente esos datos en la canalización de ingesta de datos. 

# - Los paneles personalizados son útiles para crear vistas generales únicas que presentan los datos de manera diferente.
# - Puede mostrar la información de la aplicación web y móvil, la información del servidor, los datos de métricas personalizadas y los datos de métricas de complementos, todo en un único tablero personalizado.
# - Los paneles en tiempo real guardan, comparten y comunican información.
# - Ayuda a los usuarios a generar preguntas al revelar la profundidad, el rango y el contenido de los almacenes de datos.

# - Los paneles de visualización de datos siempre cambian a medida que llegan nuevos datos.
# - Los tableros pueden contener múltiples visualizaciones de múltiples conexiones una al lado de la otra.
# - Se pueden crear, editar, filtrar y eliminar tableros rápidamente y moverlos y cambiar su tamaño y luego compartirlos o integrarlos en su aplicación web.
# - Se puede exportar un tablero como una imagen o utilizando una configuración de archivo tipo JSON. 

# ## Elasticsearch

# - Elasticsearch es un motor de análisis y búsqueda de código abierto distribuido para todo tipo de datos, incluidos textuales, numéricos, geoespaciales, estructurados y no estructurados.
# - Elasticsearch se basa en Apache Lucene y fue lanzado por primera vez en 2010 por Elasticsearch N.V. (ahora conocido como Elastic). 
#     - Extraído de: <https://www.elastic.co/>.

# ## Apache Lucene

# - Lucene Core es una biblioteca de Java que proporciona potentes funciones de indexación y búsqueda, así como funciones de corrección ortográfica, resaltado de aciertos y análisis/tokenización avanzados.
# - El subproyecto PyLucene proporciona enlaces de Python para Lucene Core. 
#     - Extraído de: <https://lucene.apache.org/>.

# ## Apache Solr

# - Solr es un servidor de búsqueda de alto rendimiento creado con Lucene Core.
# - Solr es altamente escalable y proporciona indexación, búsqueda y análisis distribuidos totalmente tolerantes a fallas.
# - Expone las características de Lucene a través de interfaces JSON/HTTP fáciles de usar o clientes nativos para Java y otros lenguajes. 
#     - Extraído de: <https://lucene.apache.org/>.

# ## Elastic Stack

# - Conocido por sus API REST simples, naturaleza distribuida, velocidad y escalabilidad, Elasticsearch es el componente central de Elastic Stack, un conjunto de herramientas de código abierto para la ingesta, el enriquecimiento, el almacenamiento, el análisis y la visualización de datos.
# - El ELK Stack se compone de las aplicaciones Elasticsearch, Logstash, Kibana, y Beats.
# - Actualmente se lo conoce como Elastic Stack, nombre que le permite agregar nuevas funcionalidades.

# - Beats 8.0
# - Elasticsearch 8.0
# - Kibana 8.0
# - Logstash 8.0

# - Extraído de: <https://www.elastic.co/what-is/elasticsearch>.

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

# ## Kibana

# - Kibana es una herramienta de visualización y gestión de datos para Elasticsearch que brinda histogramas en tiempo real, gráficos circulares y mapas. 
# - Kibana también incluye aplicaciones avanzadas, como Canvas, que permite a los usuarios crear infografías dinámicas personalizadas con base en sus datos, y Elastic Maps para visualizar los datos geoespaciales.

# ## Salesforce, Google y Microsoft  

# - Otras herramientas de modelización y visualización de datos son las proporcionadas por Salesforce, Google y Microsoft.
# - Salesforce adquirió Tableau y google hizo lo mismo con Looker en 2019.
# - La reciente integración entre estos productos le permitirán al usuario modelar datos con LookML y usar Tableau, o Looker para explorar ese modelo.

# - Tableau es una plataforma de análisis de datos que puede ser implementada en la nube, localmente o integrada de forma nativa con Salesforce CRM. 
# - Contiene capacidades de IA/ML completamente integradas, gobernanza y gestión de datos, narración visual y colaboración.
#     - Extraído de: <https://www.tableau.com/>.

# - Google Looker conecta, analiza, y visualiza datos en ambientes multicloud. 
# - Looker puede facilitar la creación de una plataforma de exploración de datos que facilite el acceso a datos de una manera significativa e intuitiva para la organización.
# - Fuente: <https://looker.com/google-cloud>.

# - Microsoft cuenta por su parte con PowerBI.
# - PowerBI se conecta a las fuentes de datos, los modela y presenta en paneles con facilidad.
# - Permite obtener respuestas rápidas y con tecnología de IA a preguntas empresariales.
#     - Fuente: <https://powerbi.microsoft.com/es-es/>.

# ## Monitoreo de datos

# - El seguimiento continuo de los datos es una parte importante de los mecanismos de gobernanza.
# - Apache Flume es útil para procesar datos de registro.
# - Apache Storm se utiliza para el monitoreo de operaciones
# - Apache Spark sirve para transmisión de datos, procesamiento de gráficos y aprendizaje automático.
# - El monitoreo puede ocurrir en el paso de almacenamiento de datos.
