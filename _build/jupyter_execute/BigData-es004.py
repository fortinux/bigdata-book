#!/usr/bin/env python
# coding: utf-8

# # Big Data tema 4

# ## Formatos de archivos para Big Data

# - Beneficios de elegir un formato apropiado de archivos:
#     - Tiempos de lectura y escritura más veloces.
#     - Se pueden dividir en múltiples discos.
#     - Compatibilidad con la evolución del esquema.
#     - Soporte de compresión.

# - Formatos de archivos optimizados para Apache Hadoop:
#     - Apache Optimized Row Columnar (ORC) <https://orc.apache.org/>
#     - Apache Parquet (almacenamiento en columnas) <https://parquet.apache.org/documentation/latest/>
#     - Apache Avro (almacenamiento en fila) <https://avro.apache.org/>
#     - Avro es popular en sistemas de streaming con Kafka y Schema Registry gracias a su rendimiento. 

# - Otros formatos de archivos:
#     - JSON <https://www.json.org/json-en.html>.
#     - CSV / TSV.
#     - XML.

# ## Bases de datos para Big Data

# ## Bases de datos NoSQL

# - Las bases de datos NoSQL, (no solo SQL) o no relacionales, se utilizan mayoritariamente para la recopilación y análisis de Big Data.
# - Permiten la organización dinámica de datos no estructurados.
# - Las bases de datos relacionales, por otro lado, tienen un diseño estructurado y tabular.

# - Bases de datos basadas en columnas están optimizadas para los trabajos analíticos intensivos de lectura.
#     - *Online Analytical Processing (OLAP)*
# - Bases de datos basadas en filas son mejores para trabajos intensivos de escritura transaccional.
#     - *Online Transactional Processing (OLTP)*

# - Existen diversos tipos de bases de datos No SQL:
#     - Bases de datos de documentos (MongoDB, Couch DB)
#     - Pares de valores (Amazon DynamoDB, Redis)
#     - Columnares (Apache Cassandra, Apache HBase)
#     - Gráficas (Neo4j, Stardog)

# ## Bases de datos de documentos

# ## MongoDB

# - Las bases de datos NoSQL, (no solo SQL) o no relacionales, se utilizan mayoritariamente para la recopilación y análisis de big data.
# - Permiten la organización dinámica de datos no estructurados.
# - Las bases de datos relacionales, por otro lado, tienen un diseño estructurado y tabular.

# - MongoDB es una base de datos distribuida de propósito general y basada en documentos.
# - Fue creada para el desarrollo de aplicaciones modernas y para la era de la nube.
# - Es una base de datos de documentos, lo que significa que almacena datos en documentos similares a JSON. 
#     - Fuente: <https://www.mongodb.com/>

# ## Versiones de MongoDB

# - MongoDB Community es la fuente disponible y la edición de uso gratuito de MongoDB.
# - MongoDB Enterprise está disponible como parte de la suscripción MongoDB Enterprise Advanced e incluye soporte integral para su implementación de MongoDB.
# - MongoDB Enterprise también agrega funciones centradas en la empresa, como compatibilidad con LDAP y Kerberos, cifrado en disco y auditoría.

# - MongoDB también ofrece Atlas, una opción de servicio alojado de MongoDB Enterprise en la nube que no requiere gastos generales de instalación y ofrece un nivel gratuito para comenzar.
# - <https://www.mongodb.com/cloud/atlas/signup>

# ## Características de MongoDB

# - Un registro en MongoDB es un documento, que es una estructura de datos compuesta por pares de campo y valor.
# - Los documentos MongoDB son similares a los objetos JSON.
# - Los valores de los campos pueden incluir otros documentos, matrices y matrices de documentos.
#     - Extraído de: MongoDB Documentation & website: <https://docs.mongodb.com/> 

# - Las ventajas de utilizar documentos son:
#      - Los documentos (es decir, los objetos) corresponden a tipos de datos nativos en muchos lenguajes de programación.
#      - Los documentos y matrices integrados reducen la necesidad de uniones costosas.
#      - El esquema dinámico admite polimorfismo fluido.

# - MongoDB almacena documentos en colecciones.
# - Las colecciones son análogas a las tablas en las bases de datos relacionales.

# - Además de las colecciones, MongoDB admite:
#      - Vistas de solo lectura (a partir de MongoDB 3.4).
#      - Vistas materializadas bajo demanda (a partir de MongoDB 4.2).

# ## Principales funcionalidades

# - Alto rendimiento
#      - MongoDB proporciona persistencia de datos de alto rendimiento.
#      - La compatibilidad con modelos de datos integrados reduce la actividad de E/S en el sistema de base de datos.
#      - Los índices admiten consultas más rápidas y pueden incluir claves de documentos incrustados y matrices.

# - Lenguaje de consulta enriquecido
#      - MongoDB admite un lenguaje de consulta enriquecido para admitir operaciones de lectura y escritura (CRUD), así como:
#          - Agregación de datos.
#          - Búsqueda de Texto y Consultas Geoespaciales.

# - Alta disponibilidad
#      - La función de replicación de MongoDB, denominada conjunto de réplicas (*replica set*), proporciona:
#          - Conmutación por error automática.
#          - Redundancia de datos. 

# - Escalabilidad Horizontal
#      - MongoDB proporciona escalabilidad horizontal como parte de su funcionalidad principal:
#          - La fragmentación (*sharding*) distribuye datos a través de un grupo de máquinas.
#          - A partir de 3.4, MongoDB admite la creación de zonas de datos basadas en la clave del fragmento (*shard*).
#          - En un clúster equilibrado, MongoDB dirige las lecturas y escrituras de una zona solo a los fragmentos dentro de la zona.

# - Soporte para Múltiples Motores de Almacenamiento
#      - MongoDB admite múltiples motores de almacenamiento:
#          - Motor de almacenamiento *WiredTiger* (incluida la compatibilidad con el cifrado en reposo).
#          - Motor de almacenamiento en memoria.
#          - Además, MongoDB proporciona una API de motor de almacenamiento conectable que permite a terceros desarrollar motores de almacenamiento para MongoDB.

# ## Tutorial MongoDB

# - Crear una cuenta gratuita en:
#     - MongoDB Atlas: <https://account.mongodb.com/account/login?>.
#     - <https://docs.atlas.mongodb.com/tutorial/deploy-free-tier-cluster/>.

# ## Bases de datos con pares de valores

# ## Redis

# - Redis es un almacén de estructura de datos en memoria (*in-memory data structure store*) de código abierto (con licencia BSD), que se utiliza como base de datos, caché y agente de mensajes. 
#     - Fuente: <https://redislabs.com/>.

# - Su estructura de datos soporta:
# - Cadenas, hashes, listas, conjuntos, conjuntos ordenados con consultas de rango, mapas de bits, hiperloglogs, índices geoespaciales con consultas de radio y flujos.

# - Tiene replicación integrada, secuencias de comandos Lua, LRU eviction, transacciones y diferentes niveles de persistencia en disco.
# - Proporciona alta disponibilidad a través de Redis Sentinel.
# - Particionamiento automático con Redis Cluster.

# - Redis Enterprise:
# - Es una sólida plataforma de base de datos en memoria creada por las mismas personas que desarrollan Redis de código abierto.
#     - Fuente: <https://redislabs.com/redis-enterprise-software/overview/>.

# - Agrega muchas capacidades de nivel empresarial, que incluyen:
#      - Escalado lineal a cientos de millones de operaciones por segundo.
#      - Distribución global Activo-Activo con latencia local.
#      - Redis en Flash para admitir grandes conjuntos de datos y minimizar los costos de infraestructura.
#      - 99,999% de tiempo de actividad.

# - Redis Enterprise está disponible como software y como servicio de nube alojado.
# - Se puede ejecutar Redis Enterprise Software (RS) en un centro de datos local o en plataformas de nube.
# - RS también funciona con varios sistemas de orquestación de contenedores, como Kubernetes.
# - Para desarrollo y pruebas, también se puede ejecutar RS usando contenedores Docker. 

# - Redis Enterprise Software facilita la ejecución de Redis a escala.
# - Se puede usar un único clúster empresarial de Redis para aprovisionar tantas bases de datos de Redis como se necesitan, y cada una de estas bases de datos se puede ajustar y escalar de forma independiente.
# - Además, Redis Enterprise admite muchas funciones de seguridad empresarial, incluido el control de acceso basado en funciones.

# ## Arquitectura de Redis 

# - Bases de datos Redis replicadas Activo-Activo (CRDB).
# - Proporciona replicación de base de datos global y distribuida geográficamente con escrituras locales sin conflictos.
# - Esto simplifica enormemente el desarrollo de aplicaciones distribuidas globalmente.
# - Las bases de datos activas-activas distribuidas geográficamente combinan tipos de datos replicados sin conflictos con tipos de datos Redis para proporcionar una resolución automática de conflictos basada en la semántica de cada tipo de datos.

# - Redis en flash:
# - Ayuda a ahorrar costes para bases de datos Redis extra grandes.
# - Las bases de datos Redis estándar mantienen todos sus datos en RAM
# - Las DB Redis on Flash (RoF) distribuyen datos a través de RAM y memoria flash dedicada (SSD).
# - Esto reduce los costes y mantiene un rendimiento similar al de las DB completamente basadas en RAM.
#     - Fuente: <https://redislabs.com/redis-enterprise/technology/redis-on-flash/>.

# - Con RS, un conjunto de datos puede crecer más allá del tamaño del nodo más grande del clúster y ser procesado por cualquier cantidad de núcleos.
# - Al particionar el conjunto de datos en varios nodos mediante una política de fragmentación, RS supera las limitaciones de memoria de un solo nodo y las limitaciones de rendimiento de un solo núcleo.
# - Se puede escalar dinámicamente las bases de datos de Redis aumentando los límites de memoria o aumentando la cantidad de fragmentos, todo usando la interfaz de usuario integrada.

# - Además de replicar una base de datos dentro del mismo centro de datos, también se puede replicar un conjunto de datos entre centros de datos y entre regiones.
# - Esto proporciona alta disponibilidad, recuperación ante desastres y mejoras de rendimiento para aplicaciones distribuidas globalmente.

# - Si un nodo falla, los datos se entregan sin problemas desde un nodo de reemplazo en el clúster sin intervención humana.
# - Redis Enterprise puede manejar automáticamente fallas de nodos, fallas de procesos de Redis y fallas de proxy.
# - La conmutación por error generalmente se completa en unos pocos segundos.

# - RS permite el uso de Redis AOF (*Append-Only File*) cada segundo o en cada escritura, o instantáneas (RDB) del conjunto de datos cada 1, 6 o 12 horas para almacenamiento persistente.
# - Además, se puede hacer una copia de seguridad del conjunto de datos periódicamente o bajo demanda en un servidor FTP, almacenamiento en red o servicio de almacenamiento en la nube.

# - Las solicitudes son procesadas por múltiples núcleos para garantizar el mejor rendimiento.
# - Se pueden ejecutar varias bases de datos en un único clúster empresarial de Redis.
# - Cada base de datos se ejecuta con sus propios procesos dedicados sin bloqueo.

# - Un clúster de Redis Enterprise se compone de nodos idénticos que se implementan dentro de un centro de datos o se extienden a través de zonas de disponibilidad local.
# - La arquitectura de Redis Enterprise se compone de una ruta de administración y una ruta de acceso a los datos.

# - La ruta de administración incluye el administrador de clústeres, el proxy y la interfaz de usuario/API REST segura para la administración programática.
# - En resumen, el administrador de clústeres es responsable de orquestar el clúster, colocar fragmentos de bases de datos y detectar y mitigar fallas.
# - El proxy por otro lado ayuda a escalar la gestión de conexiones.

# - La ruta de acceso a datos se compone de fragmentos (*shards*) de Redis maestros y esclavos.
# - Los clientes realizan operaciones de datos en el fragmento maestro.
# - Los fragmentos maestros mantienen fragmentos esclavos mediante la replicación en memoria para la protección contra fallas que pueden hacer que el fragmento maestro sea inaccesible.

# - Redis Enterprise utiliza la replicación en memoria para mantener réplicas maestras y esclavas.
# - Viene con varios *watchdogs* que detectan y protegen contra varios tipos de fallas.
# - En las fallas en nodo, red, y fallas de proceso que hacen que la réplica maestra sea inaccesible; promueve automáticamente la réplica esclava para que sea una réplica maestra y redirige la conexión del cliente de forma transparente a la nueva réplica maestra.

# - Además de la replicación dentro del clúster, Redis Enterprise también tiene una replicación basada en WAN integrada para implementaciones de Redis en varios centros de datos.
# - Los mecanismos de replicación basados en WAN en Redis Enterprise están diseñados para proteger contra fallas totales del centro de datos o de redes más amplias.

# - Cada clúster de Redis Enterprise puede contener varias bases de datos.
# - En Redis, las bases de datos representan datos que pertenecen a una sola aplicación, inquilino (*tenant*) o microservicio.
# - Redis Enterprise está diseñado para escalar a cientos de bases de datos por clúster para proporcionar modelos de tenencia múltiple flexibles y eficientes.

# - Cada base de datos puede contener pocos o muchos fragmentos (*shards*) de Redis.
# - La fragmentación es transparente para las aplicaciones de Redis.
# - Shards maestros en las base de datos procesan operaciones de datos para un subconjunto dado de claves.
# - La cantidad de shards por base de datos es configurable y depende de las necesidades de rendimiento de las aplicaciones.

# - Las bases de datos en Redis Enterprise se pueden volver a dividir en más fragmentos de Redis para escalar el rendimiento mientras se mantienen latencias de menos de un milisegundo.
# - La fragmentación se realiza sin tiempo de inactividad.

# - En Redis Enterprise, cada base de datos tiene una cuota de RAM.
# - La cuota no puede exceder los límites de la RAM disponible en el nodo.
# - Sin embargo, con Redis Enterprise Flash, la memoria RAM se extiende a la unidad flash local (SATA, SSD NVMe, etc.).

# - La cuota total de la base de datos puede aprovechar tanto la memoria RAM como la unidad flash.
# - El administrador puede elegir la relación RAM vs Flash y ajustarla en cualquier momento durante la vida útil de la base de datos sin tiempo de inactividad.

# - Con Redis en Flash, en lugar de almacenar todas las claves y datos para un fragmento determinado en la RAM,  se envían a flash los valores a los que se accede con menos frecuencia.
# - Si las aplicaciones necesitan acceder a un valor que está en flash, Redis Enterprise trae automáticamente el valor a la RAM.

# - Dependiendo del hardware flash en uso, las aplicaciones experimentan una latencia ligeramente más alta al devolver valores a la RAM desde flash.
# - Sin embargo, los accesos posteriores al mismo valor son rápidos, una vez que el valor está en la RAM.

# - Redis Enterprise tiene dos opciones de durabilidad:
#      - Durabilidad basada en disco.
#      - Durabilidad basada en replicación.

# - Durabilidad basada en disco:
#      - Redis Enterprise aún mantiene una copia duradera en el disco.
#      - Al igual que los sistemas basados en disco, esta ruta de E/S se coloca en un dispositivo de almacenamiento conectado a la red más lento y duradero.
#      - Las bases de datos de Redis brindan opciones ajustables para mantener esta copia duradera y mantenerla actualizada con escrituras periódicas frecuentes hasta cada operación de escritura.

# - Durabilidad basada en replicación:
#      - Redis Enterprise también mantiene una réplica, un fragmento esclavo, para mayor durabilidad.
#      - Esta durabilidad replicada protege contra fallas de nodo, rack o de zona.
#      - La durabilidad replicada proporciona un mejor rendimiento de escritura sobre las escrituras de almacenamiento conectado a la red.

# - Esto significa que bajo una interrupción no planificada, es más probable que la réplica esté más actualizada en comparación con la copia duradera en el disco.
# - Para aprovechar al máximo la durabilidad replicada, Redis proporciona el comando WAIT.

# - WAIT se asegura de que una escritura pueda esperar el reconocimiento hasta que varias réplicas confirmen esa escritura.
# - Esto garantiza que una escritura confirmada con WAIT en las réplicas sea duradera incluso si un nodo se incendia y nunca más vuelve al clúster.

# ## Tutorial Redis

# - Free plan 30MB: <https://redis.com/redis-enterprise-cloud/pricing/>.
# - Free plan 5MB: <https://redistogo.com/>.
# - Tutorial: <https://try.redis.io/>.

# ## Bases de datos columnares

# ## Apache Cassandra

# - Apache Cassandra es una base de datos distribuida NoSQL de código abierto.
# - La escalabilidad lineal y la tolerancia a fallas comprobada en hardware básico o infraestructura en la nube la convierten en la plataforma perfecta para datos de misión crítica.
#     - Extraído de: <https://cassandra.apache.org/_/index.html>.

# - Híbrida
# - La arquitectura sin servidor maestro y la baja latencia significan que Cassandra resistirá una interrupción completa del centro de datos sin pérdida de datos, en nubes públicas o privadas, o en las instalaciones.

# - Tolerante a fallos
# - El soporte de Cassandra para la replicación en varios centros de datos es el mejor de su clase, lo que proporciona una latencia más baja para sus usuarios y la tranquilidad de saber que puede sobrevivir a las interrupciones regionales.
# - Los nodos con fallas se pueden reemplazar sin tiempo de inactividad.

# - Centrada en la calidad
# - Para garantizar la confiabilidad y la estabilidad, Cassandra se prueba en clústeres de hasta 1,000 nodos y con cientos de casos de uso y esquemas del mundo real probados con pruebas de reproducción, fuzz, basadas en propiedades, inyección de fallas y de rendimiento.

# - Desempeño
# - Cassandra supera sistemáticamente a las populares alternativas de NoSQL en pruebas comparativas y aplicaciones reales, principalmente debido a las elecciones de arquitectura tomadas.
# - <https://vldb.org/pvldb/vol5/p1724_tilmannrabl_vldb2012.pdf>.
# 

# - Cassandra transmite datos entre nodos durante las operaciones de escalado, como agregar un nuevo nodo o centro de datos durante las horas pico de tráfico.
# - Zero Copy Streaming lo hace hasta 5 veces más rápido sin *vnodes* para una arquitectura más elástica, especialmente en entornos de nube y Kubernetes.

# - Distribuida
# - Cassandra es adecuada para aplicaciones que no pueden darse el lujo de perder datos, incluso cuando un centro de datos completo deja de funcionar.
# - No hay puntos únicos de falla. No hay cuellos de botella en la red. Todos los nodos del clúster son idénticos.

# - Opciones
# - Se puede elegir entre replicación síncrona o asíncrona para cada actualización. Las operaciones asincrónicas de alta disponibilidad se optimizan con funciones como *Hinted Handoff* y *Read Repair*.
# - La función de registro de auditoría para operadores rastrea la actividad DML, DDL y DCL con un impacto mínimo en el rendimiento normal de la carga de trabajo, mientras que *fqltool* permite la captura y reproducción de cargas de trabajo de producción para su análisis.

# ## Tutorial Cassandra 

# - Se utilizará una imagen de Docker con Cassandra para realizar el tutorial
# - <https://cassandra.apache.org/_/quickstart.html>

# ## Apache HBase

# - Es una base de datos distribuida no relacional open source modelada en base al artículo científico Google's Bigtable: A Distributed Storage System for Structured Data de Chang et al.

# - Así como Bigtable aprovecha el almacenamiento de datos distribuido proporcionado por el sistema de archivos de Google, Apache HBase proporciona capacidades similares a las de Bigtable junto con Hadoop y HDFS.

# - Extraído de: Apache HBase Docs & website: <https://hbase.apache.com/>. 

# - Se utiliza Apache HBase cuando se necesita acceso de lectura/escritura aleatorio y en tiempo real a Big Data.
# - El objetivo de HBase es el alojamiento de tablas muy grandes:
#      - Miles de millones de filas por millones de columnas.
#      - Utilizando clusters con hardware de bajo coste.

# - BerkeleyDB es un ejemplo de una base de datos NoSQL local, mientras que HBase es en gran medida una base de datos distribuida.
# - Técnicamente hablando, HBase es más un "almacén de datos" que una "base de datos" porque carece de muchas de las funciones que se encuentran en un RDBMS, como columnas escritas, índices secundarios, activadores y lenguajes de consulta avanzados, etc.

# - HBase tiene muchas características que admiten escalado tanto lineal como modular.
# - Los clústeres de HBase se expanden agregando *Region Servers* que están alojados en servidores con hardware de bajo coste.
# - Si un clúster se expande de 10 a 20 *Region Servers*, por ejemplo, se duplica tanto en términos de almacenamiento como de capacidad de procesamiento.

# ## Características de HBase 

# - Lecturas/escrituras consistentes: HBase no es un DataStore "eventualmente consistente". Esto lo hace muy adecuado para tareas como la agregación de contadores de alta velocidad.
# - Fragmentación automática: las tablas de HBase se distribuyen en el clúster a través de regiones, y las regiones se dividen y redistribuyen automáticamente a medida que aumentan los datos.

# - Conmutación por error automática de *Region Server*
# - Integración de Hadoop/HDFS: HBase es compatible con HDFS de fábrica como su sistema de archivos distribuido.
# - MapReduce: HBase admite procesamiento en paralelo masivo a través de MapReduce para usar HBase como fuente y receptor.

# - API de cliente de Java: HBase admite una API de Java fácil de usar para el acceso programático.
# - API Thrift/REST: HBase también es compatible con Thrift y REST para front-ends que no son de Java.
# - Block Cache y Bloom Filters: HBase admite *Block Cache* y *Bloom Filters* para la optimización de consultas de gran volumen.
# - Gestión operativa: HBase proporciona páginas web integradas para obtener información operativa y métricas JMX.

# - HBase, se basa en HDFS y proporciona búsquedas rápidas de registros (y actualizaciones) para tablas grandes.
# - Esto a veces puede ser un punto de confusión conceptual.
# - HBase coloca internamente sus datos en "StoreFiles" indexados que existen en HDFS para búsquedas de alta velocidad.

# ## Usos de Apache HBase

# - HDFS es un sistema de archivos distribuido muy adecuado para el almacenamiento de archivos de gran tamaño.
# - Su documentación establece que, sin embargo, no es un sistema de archivos de propósito general y no proporciona búsquedas rápidas de registros individuales en archivos.

# - Si se tienen cientos de millones o miles de millones de filas, HBase es un buen candidato.
# - Si solo se tienen unos pocos miles/millones de filas, entonces usar un RDBMS tradicional podría ser una mejor opción debido al hecho de que todos los datos pueden terminar en un solo nodo (o dos) y el resto del clúster puede estar sentado inactivo.

# - Una aplicación construida contra un RDBMS no se puede "portar" a HBase simplemente cambiando un controlador JDBC, por ejemplo.
# - Considere pasar de un RDBMS a HBase como un rediseño completo en lugar de un puerto.

# ## Requisitos de Apache HBase

# - Asegurarse de tener suficiente hardware.
# - HDFS no funciona bien con menos de 5 DataNodes (debido a cosas como la replicación de bloques de HDFS que tiene un valor predeterminado de 3), más un NameNode.
# - HBase puede funcionar bastante bien de forma independiente en una computadora portátil, pero esto debe considerarse solo como una configuración de desarrollo.

# - Tutorial: <https://hbase.apache.org/book.html#quickstart>.

# ## Bases de datos gráficas

# ## Neo4j

# - Neo4j permite construir aplicaciones y flujos de trabajos de ML.
# - Almacena y administra datos manteniendo relaciones que brindan consultas veloces, un contexto más profundo para el análisis y un modelo de datos modificable sin complicaciones.
#     - Fuente: <https://neo4j.com/>.
