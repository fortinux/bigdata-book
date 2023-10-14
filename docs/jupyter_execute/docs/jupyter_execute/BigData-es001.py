#!/usr/bin/env python
# coding: utf-8

# # Big Data tema 1

# ## Big Data y el análisis de datos

# - ¿Cómo puede el análisis de datos y Big Data ayudar a mi organización?
# - ¿Cómo extraigo información valiosa e *insights* sobre las tendencias, correlaciones y patrones que existen en Big Data?

# - En el pasado solo las grandes organizaciones podían aprovecharse de Big Data. 
#     - Walmart, Google, agentes financieros especializados. 
# - Actualmente con Hadoop, hardware de bajo coste (*commodity*) con el kernel de Linux y el *cloud computing*, casi cualquier organización se lo puede permitir.

# - Hay una revolución de datos
# - Los datos que se generan el mundo aumentan anualmente un 40%.
# - Para 2025 se crearán más de 180 zetabytes.
#     - Fuente: <https://es.statista.com/>.

# - IDC predice que la Global Datasphere crecerá desde los 33 Zettabytes en 2018 hasta los 175 Zettabytes en 2025.
#     - Fuente: The Digitization of the World – From Edge to Core. IDC White Paper. Doc# US44413318. Noviembre 2018.

# - En 2025, cada persona conectada en el mundo interactuará dejando su huella digital unas 4900 veces por día - eso significa una interacción cada 18 segundos.
# - "El mundo guiado por los datos va a estar siempre activo, siempre haciendo el seguimiento de todo, siempre monitorando, siempre escuchando y siempre viendo - porque va a estar siempre aprendiendo."
#     - Fuente: The Digitization of the World – From Edge to Core. IDC White Paper. Doc# US44413318. Noviembre 2018.

# ## El mercado del Big Data

# - El mercado global de Big Data y análisis de negocios ha crecido saludablemente durante los últimos años.
# - 122 billones de dolares estadounidenses de ingresos a nivel global en 2015, hasta los estimados 189 billones de dólares estadounidenses en 2019.
# - IDC proyecta que los ingresos crecerán hasta los 274 billones de dólares estadounidenses en 2022.
#     - Fuente: PCMag. <https://www.pcmag.com/news/the-big-data-market-is-set-to-skyrocket-by-2022>. Junio 2019.

# - Snowflake tiene una capitalización de mercado de 69 billones de dólares estadounidenses.
# - Palantir a su vez alcanzó los 22 billones de dólares estadounidenses en 2019 (40 B. en 2022).
# - Datadog era una empresa de 12 billones de dólares estadounidenses (25 B. en 2022)
#     - Fuente: Matt Turck. 
#     - <https://mattturck.com/data2020/>. Septiembre, 2020. 
#     - <https://mattturck.com/madindex/>. Septiembre. 2021.

# ## Big Data en España

# - *El 11,1% de las empresas españolas de más de 10 empleados hizo análisis basado en Big Data en el último año y nueve meses o “período pandémico” (2020/2021). Son 2 puntos porcentuales más que en el período previo, de relativa calma económica (2018/2019).*
# - Fuente: [IT User](https://www.ituser.es/opinion/2021/10/20202021-digitalizacion-en-espana-big-data-pymes-y-liderazgo-femenino).

# - *El salto más fuerte ha sido el del porcentaje de empresas españolas que han pasado a emplear Internet de las Cosas (IoT) en 2018/2019 (16,8%) al período actual 2020/2021 (27,7%): un salto de +10,9% a favor de IoT.*

# - *La tecnología menos utilizada es la Inteligencia Artificial (IA), por un 8,3% de empresas en el período pandémico de 2020/2021.*

# ## Tendencias en Big Data

# - Operacionalización del Big Data.
# - Menos unicornios en el mundo de los datos y el AI.
# - Mayor alineación entre la analítica tradicional con ML y la analítica AI.
#     - Fuente: Infoworks.io <https://www.infoworks.io/big-data-trends/>. Octubre 2019.

# - De Hadoop a servicios cloud a Kubernetes + Snowflake.
# - Gobernanza de Datos, catalogación, y la cada vez más importante gestión de datos.
# - El aumento de stacks específicos para la infraestructura de AI (“MLOps”, “AIOps”).
#     - Fuente: Mattturck.com. <https://mattturck.com/data2020/>. Septiembre, 2019.

# - ETL vs ELT.
# - Automación de la ingeniería de datos.
# - Alza de la importancia del analista de datos.
# - Unión de los Data lakes y los data warehouses.
# - Boom de plataformas para ciencia de datos y machine learning (DSML).
# - GAFAM, Uber, Lyft, etc. se han convertido completamente en organizaciones AI.
# - Alza de NLP, una rama de la AI focalizada en entender el lenguaje natural.
#     - Fuente: Mattturck.com. <https://mattturck.com/data2020/>. Septiembre, 2019.

# ## 2021 Machine Learning, AI and Data (MAD) Landscape

# - Toda empresa es una empresa de datos (GAFAM)
# - Almacenes de datos (*datawarehouses*) y lagos (*data lakes*)
# - Consolidación vs malla de datos (*data mesh*): el futuro es híbrido
# - <https://martinfowler.com/articles/data-monolith-to-mesh.html>
# - DataOps
# - Real time (Confluent/Kafka, Storm, Flink, Materialize, AWS Kinesis)
# - Capa de métricas (Metric stores)
# - Reverse ETL
# - Compartir datos con partners, proveedores y clientes

# - Predicciones ML e inteligencia artificial:
#     - Feature Stores (variables o atributos en ML)
#     - ModelOps: modelos de operaciones para AI incluyendo ML 
#     - Generación de contenido por AI (Synthesia, Sonantic)
#     - <https://www.messimessages.com/>

# - Stack chino de AI: plan de supremacía para el 2030 
# - Wu Dao 2.0 es una IA multimodal que tiene 1,75 billones de parámetros, 10 veces la cantidad de GPT-3, lo que lo convierte en el sistema de lenguaje de IA más grande hasta la fecha. Sus capacidades incluyen el manejo de NLP y reconocimiento de imágenes.
#     - Fuente: <https://mattturck.com/data2021/>

# ## Definición de Big Data

# - Big data son activos de datos de gran volumen, alta velocidad y/o gran variedad que exigen formas innovadoras y rentables de procesamiento de la información que permiten una mejor comprensión, toma de decisiones y automatización de procesos.
#     - Fuente: Gartner’s Glossary. <https://www.gartner.com/en/information-technology/glossary/big-data>.

# ## 3 V de Big Data

# - Volumen: 
#     - Procesamiento de grandes volúmenes de baja densidad de datos no estructurados. 
#     - Datos de valor desconocido algunas veces, pero que pueden llegar a ser cientos de terabytes o petabytes de tamaño. 

# - Velocidad: 
#     - Velocidad es la tasa por la cual los datos son recibidos y (tal vez) manipulados.

# - Variedad: 
#     - Varios tipos de datos no estructurados y semiestructurados que están disponibles para ser tratados como texto, audio, video, IoT data, etc.

# Fuente: {cite:ps}`Curry2021`

# ## Otras V del Big Data

# - Valor: 
#     - Los datos tienen un valor intrínseco. Pero no tienen ninguna utilidad hasta que ese valor no sea descubierto.
# - Veracidad: 
#     - Si los datos son confiables y hasta que punto.

# - Fuente: What is Big Data?. Oracle. <https://www.oracle.com/big-data/what-is-big-data.html>.

# ## Tipos de datos

# - Datos estructurados: 
#     - Datos que están guardados en bases de datos relacionales. 
# - Datos no estructurados: 
#     - Ejemplos incluyen texto, video, audio, actividad en el smartphone, actividad en las redes sociales, imágenes satelitales, imágenes de vigilancia.
# - Datos semiestructurados: 
#     - Los documentos de bases de datos NoSQL son considerados semiestructurados porque contienen palabras claves que pueden ser usadas para procesarlos.

# Fuente: {cite:ps}`Skiena2017`.

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

# ## Benificios aportados por el Big Data

# - La importancia de la analítica de big data ha aumentado junto con la variedad de datos no estructurados que pueden ser analizados para obtener información: 
#     - Contenido de las redes sociales, textos, clickstream data. 
#     - Sensores del Internet de las cosas (IoT).

# - Reducción de costes.
# - Descubrir maneras más eficientes de hacer negocios.
# - Mejor toma de decisiones.
# - Crear nuevos productos y servicios que el cliente quiere y necesita.

# - Fuente: What is Big Data?. Oracle. <https://www.oracle.com/big-data/what-is-big-data.html>.

# ## Historia del Big Data

# - Los grandes data sets comenzaron en los '60 y '70 del siglo pasado con los primeros centros de datos y el desarrollo de las bases de datos relacionales (lenguaje SQL).

# - Inmon acuñó el término *data warehousing* promoviendo la construcción, uso y mantenimiento de *data warehouses* para el almacenamiento de datos. 
# - Escribió el libro "Building the Data Warehouse" (1992, con ediciones posteriores) y "DW 2.0: The Architecture for the Next Generation of Data Warehousing" (2008).
#     - Fuente: Wikipedia. <https://en.wikipedia.org/wiki/Bill_Inmon>. 

# - Hoy se cuenta con la escalabilidad y elasticidad de *cloud data warehouses* y *data lakes*:
#     - Snowflake (*cloud data warehouse*).
#     - Databricks (*data lakes*).
#     - Amazon Redshift / EMR.
#     - Google BigQuery / Dataproc.
#     - Azure SQL Data Warehouse (SQL DW) / HD Insights.

# ## Data Lakes - Data Warehouses

# - *Data lakes* son grandes repositorios de datos sin procesar en una variedad de formatos, que son de bajo coste y escalables pero que en principio no soportan transacciones, calidad de datos, etc. (ML)
# - *Data warehouses* por otro lado, contienen datos estructurados y capacidad de realizar transacciones y gobernanza.  (BI)

# ## Nuevo paradigma

# - En 2005, la cantidad de datos que generaban Facebook, Google, y otros servicos online era enorme.
# - Para analizarlos, en 2006 algunos ingenieros de Yahoo crearon Hadoop lanzándolo como un projecto Apache open source. 
# - El framework de procesamiento distribuído hizo posible ejecutar aplicaciones big data en una plataforma clusterizada con harware de bajo coste. 
# - Por ese entonces las bases de datos NoSQL también comenzaron a popularizarse.

# ## Hadoop y Spark

# - El desarrollo de frameworks open-source, como Hadoop y Spark, fue esencial para el crecimiento de Big Data ya que permitieron trabajar más dinámicamente junto con un almacenamiento de grandes volúmenes de datos más económico.

# - Actualmente los proveedores de plataformas en la nube permiten a cualquier organización montar una estructura para análisis con Hadoop o con herramientas propias, e utilizarla bajo demanda.

# - Forbes' Big data landscape: <http://www.forbes.com/sites/davefeinleib/2012/06/19/the-big-data-landscape/>.
# - Matt Tuck's Data & AI landscape 2019: <https://mattturck.com/data2019>.
# - Matt Tuck's Data & AI landscape 2021: <https://mattturck.com/data2021/>.

# ## Casos de uso de Big Data

# - Agricultura 
#     - Seguimiento de cultivos
#     - Optimización de equipamiento 
#     - Agricultura de precisión

# - Telecomunicaciones 
#     - Predicción del *churn* 
#     - Optimización de la red 
#     - Segmentación

# - Utilidad pública (*utilities*) 
#     - Predicción del *churn* 
#     - Optimización de la red 
#     - Personalización de tarifas

# - Fuente: Databench Europe <https://www.databench.eu/>

# - Industria de la aviación
#     - Las líneas aéreas colectan una gran cantidad de datos como preferencias de vuelos de los clientes, control del tráfico aéreo, gestión de equipajes, mantenimiento de las aeronaves, rutas de vuelo, y más.
#     - Big data provee nuevas perspectivas para optimizar las operaciones y brindar un mejor servicio al cliente.

# - Sector bancario
#     - La inmensa cantidad de datos estructurados y no estructurados que las instituciones financieras obtienen les permiten tomar decisiones más certeras.
#     - Ellas también pueden prevenir fraudes utilizando big data analytics.

# - Sector de la salud
#     - Investigadores intercambian gran cantidad de datos de manera nunca antes vista y cooperan para entender COVID-19 y desarrollar un modelo para tratar las enfermedades más allá de la pandemia del coronavirus.

# - Fuente: Big Data and Collaboration Seek to Fight COVID-19.     
# https://www.the-scientist.com/news-opinion/big-data-and-collaboration-seek-to-fight-covid-19-67759

# - Sector manufacturero
#     - Big data analytics le permite a la industria entender mejor como su propia cadena de valor funciona. 
#     - Es usado también para el mantenimiento preventivo del equipamiento industrial.
#     - La industria 4.0 tiende al uso intensivo de IA en todos sus procesos.

# - Fuente: BCG. <https://www.bcg.com/publications/2016/leaning-manufacturing-operations-factory-of-future.aspx>

# - Venta minorista
#     - Con big data analytics, los vendedores minoristas pueden entender mejor las preferencias y el comportamiento de sus clientes, sus hábitos de compra; y predecir tendencias.

# - Ciencia
#     - *Los investigadores de todas las disciplinas consideran que la capacidad recién descubierta de vincular y cruzar datos de diversas fuentes mejora la precisión y el poder predictivo de los hallazgos científicos y ayuda a identificar futuras direcciones de investigación, lo que en última instancia proporciona un punto de partida novedoso para la investigación empírica.*

# - Fuente: Leonelli, Sabina, "Scientific Research and Big Data", The Stanford Encyclopedia of Philosophy (Summer 2020 Edition), Edward N. Zalta (ed.), URL = <https://plato.stanford.edu/archives/sum2020/entries/science-big-data/>. 

# - *Cuando comencé a contratar Ph.D. estudiantes hace 15 años, eran completamente laboratorios húmedos,* dice Corcoran. *Ahora, cuando los reclutamos, lo primero que buscamos es si pueden hacer frente a análisis bioinformáticos complejos*.
# - Para ser un biólogo, hoy en día, se necesita tener conocimientos de estadística y programación.
# - Se necesita saber trabajar con algoritmos.

# - Fuente: Phys.org. How big data is changing science. <https://phys.org/news/2018-10-big-science.html/>

# ## Buenas prácticas para Big Data

# - Big data analytics utiliza datos tanto de fuentes internas como externas.
# - Los datos deben ser estar organizados y gestionados para obtener un óptimo rendimiento.

# - Bases de datos basadas en columnas están optimizadas para los trabajos analíticos intensivos de lectura.
# - Bases de datos basadas en filas son mejores para trabajos intensivos de escritura transaccional.

# - Para el análisis de big data en tiempo real, se utiliza un motor de procesamiento de flujo de datos como Spark a través de un almacén de datos (*data warehouse*).
# - Para los datos sin procesar (*data lake*) se utiliza Hadoop y su HDFS (*Hadoop Distributed File System*).

# - Alinear Big Data con los objetivos específicos del negocio.
# - Aliviar la escasez de habilidades con estándares y gobernanza.
# - Optimizar la transferencia de conocimiento mediante un centro de excelencia.

# - Lo mejor es alinear datos no estructurados con estructurados.
# - Planificar su estructura de Big Data para el rendimiento.
# - Alinear con el modelo de operaciones cloud.

# - Fuente: What is Big Data?. Oracle. <https://www.oracle.com/big-data/what-is-big-data.html>.

# ## Serie ISO/IEC 20547

# - La serie ISO/IEC 20547 está destinada a proporcionar a los usuarios un enfoque estandarizado para desarrollar e implementar arquitecturas de big data y proporcionar referencias para enfoques.
# - El vocabulario y los conceptos comunes están descritos en ISO/IEC 20546.
# - Getting big on data <https://www.iso.org/news/ref2578.html>.

# ## NIST Big Data Interoperability Framework

# - Para avanzar en el progreso de Big Data, el Grupo de Trabajo Público de Big Data del NIST (NBD-PWG) trabaja para desarrollar un consenso sobre conceptos importantes y fundamentales relacionados con Big Data.
# - NIST Big Data Interoperability Framework: Volume 1, Definitions. Version 3.
# - <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1500-1r2.pdf>.

# - NIST Big Data Interoperability Framework: Volume 9, Adoption and Modernization. Version 3.
# - <https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.1500-10r1.pdf>

# ## Tipos de análisis de datos en Big Data

# - Análisis descriptivo: Provee nuevas perspectivas en datos históricos.
# - Análisis predictivo: Provee nuevas perspectivas en datos futuros.
# - Análisis prescriptivo: Provee informes analíticos con recomendaciones para el futuro.

# ## Análisis descriptivo

# - Data mining: Se utiliza para filtrar conjuntos de datos en busca de patrones y relaciones.

# - ¿Qué hay en los datos?
#     - Asociación.
#     - Análisis exploratorio.
#     - Segmentación.
#     - Clustering (no supervisado): agrupar los datos en categorías basadas en alguna medida de similitud o distancia.
#     - Reducción de la dimensión: proceso de reducción del número de variables aleatorias que se tratan.

# ## Análisis predictivo

# - Construir modelos para prever el comportamiento del cliente.
# - ¿Cuál será la salida de una nueva entrada?
#     - Regresión logística: predice el resultado de una variable categórica en función de las variables independientes.
#     - Análisis de varianza y covarianza.
#     - Métodos bayesianos.
#     - Elección de un modelos: Comparar, validar y elegir modelos.

# - Clasificación estadística (aprendizaje supervisado): identificar a que conjunto de categorías pertenece una nueva observación. 
#     - Discriminante.
#     - Redes neuronales.
#     - Árboles de decisión.

# - Biblioteca para Python: <https://scikit-learn.org/stable/>.
# - Knime: <https://www.knime.com/>.
# - Lenguaje R: <https://www.r-project.org/>.

# ## Análisis prescriptivo

# - ¿Qué acción se debe tomar en base a estos datos?
#     - Optimización: estudio de desafíos en los que es posible construir modelos matemáticos para representarlos.
#     - Inferencia causal: estudio de sistemas donde se sospecha que la medida de una variable afecta la medida de otra.

# - Machine learning: 
#     - Programación de algoritmos para analizar grandes volúmenes de datos.
# - Deep learning: 
#     - Algorimos que pueden determinar la precisión de una predicción por sí mismos.

# ## Big Data analytics y Business Intelligence

# - Business Intelligence se basa en datos estructurados en un data warehouse y puede mostrar qué y dónde ocurrió un evento.
# - El análisis de Big Data utiliza conjuntos de datos estructurados y no estructurados encontrando relaciones mientras explica por qué sucedieron los eventos.
# - También puede predecir si un evento volverá a ocurrir.

# ## Fuentes libres de datos

# - <https://www.data.gov/>
# - <https://www.census.gov/data.html>
# - <https://data.gov.uk/>
# - <http://data.europa.eu/euodp/en/data/>
# - <https://developers.facebook.com/docs/graph-api>
# - <https://www.healthdata.gov/>
# - <http://content.digital.nhs.uk/home>
# - <https://trends.google.com/trends/explore>
# - <https://www.google.com/finance>
# - <http://aws.amazon.com/datasets/>

# ## Herramientas para Big Data

# ## Apache Hadoop

# - El proyecto Apache™ Hadoop® desarrolla software de código abierto para computación distribuida, escalable y confiable.

# - Extraído de: Apache Hadoop Docs & website: <https://hadoop.apache.org/>. 

# - Es un framework para el procesamiento distribuido de grandes conjuntos de datos en grupos de computadoras que utilizan modelos de programación simples.
# - Diseñado para escalar desde servidores individuales a miles de máquinas, cada una de las cuales ofrece computación y almacenamiento locales.

# - En lugar de depender del hardware para brindar alta disponibilidad, la biblioteca en sí está diseñada para detectar y manejar fallas en la capa de la aplicación, por lo que brinda un servicio de alta disponibilidad sobre un grupo de computadoras, cada una de las cuales puede ser propensa a fallas.

# Fuente: {cite:ps}`Turkington2013`

# ## Módulos de Apache Hadoop

# - Apache Hadoop cuenta con una serie de módulos que le permiten extender sus funcionalidades.
# - Los más utilizados son *Hadoop Common, HDFS, YARN y MapReduce*.

# - Hadoop Common: 
#     - Las *common utilities* que soportan los otros módulos de Hadoop.
# - Hadoop Distributed File System (HDFS™): 
#     - Un sistema de archivos distribuido que proporciona acceso de alto rendimiento a los datos de la aplicación.
#     - <https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-hdfs/HdfsDesign.html/>.

# - Hadoop YARN
#     - Un framework para job scheduling y gestión de recursos de los clusters. 
#     - Tecnología de gestión de clústeres en Hadoop de segunda generación.
#     - Extraído de: <https://hadoop.apache.org/docs/current/hadoop-yarn/hadoop-yarn-site/YARN.html/>.

# - MapReduce
#     - Un sistema basado en YARN para el procesamiento en paralelo de grandes volúmenes de datos.    
#     - Este framework procesa cantidades masivas de datos no estructurados en paralelo en un clúster distribuido.
#     - Extraído de: <https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html>.

# - The Hadoop Ecosystem Table
# - <https://hadoopecosystemtable.github.io/>.

# - Soluciones Hadoop:
#     - Cloudera Data Platform <https://www.cloudera.com/>.
#     - Hortonworks (Adquirida por Cloudera)
#     - Amazon ERM <https://aws.amazon.com/es/emr/>.
#     - Google Dataproc <https://cloud.google.com/dataproc/>.
#     - Microsoft HDInsight <https://azure.microsoft.com/es-es/services/hdinsight/>.
