[![Jupyter Book Badge](https://jupyterbook.org/badge.svg)](<https://jupyterbook.org/intro.html>)
[![Fortinux Book Badge](https://fortinux.com/FortinuxBook.svg)](<https://fortinux.github.io/bigdata-book/intro.html>) 

# Introducción a Big Data
## Apuntes de análisis de datos y ML

Introducción a Big Data. Apuntes del curso por Marcelo Horacio Fortino. Versión 2.4.2. Noviembre 2024.    

Esta obra está sujeta a la licencia Reconocimiento-CompartirIgual 4.0 Internacional de Creative Commons. Para ver una copia de esta licencia, visite <http://creativecommons.org/licenses/by-sa/4.0/>. Puede hallar permisos más allá de los concedidos con esta licencia en <https://fortinux.com>. Sugerencias y comentarios a <info@fortinux.com>.     

Todas las marcas son propiedad de sus respectivos dueños. Apache Hadoop, Hadoop, Apache, the Apache feather logo, y el Apache Hadoop project logo son marcas registradas o marcas de la Apache Software Foundation en los Estados Unidos y otros países. Copyright © 2006-2022 The Apache Software Foundation.    
    
| Versión | Autor | Fecha | Observaciones |
|------- | ---------------- | -------- | -----------|
| 1.0 | Marcelo Horacio Fortino | 2020/Nov | Fundamentals of Big Data |
| 1.1 | Marcelo Horacio Fortino | 2022/Feb | Traducido al castellano, actualizado y convertido a markdown - ipynb |    
| 1.2 | Marcelo Horacio Fortino | 2022/Mar | Convertido en Jupyter Book |    
| 2.0 | Marcelo Horacio Fortino | 2023/Oct | Actualizados contenidos. Agregado Data Science |    


Esta obra se distribuye con la esperanza de que sea útil, pero SIN NINGUNA GARANTÍA, incluso sin la garantía MERCANTIL implícita o sin garantizar la CONVENIENCIA PARA UN PROPÓSITO PARTICULAR. El autor no asume ninguna responsabilidad si el lector hace un mal uso de la misma.    
    
- Estos apuntes se basan en: 
    - La bibliografía presentada al final de este documento, y
    - Documentación propia recogida a lo largo de los años de diversas fuentes.
    
## Introducción
En el pasado solamente las grandes organizaciones podían aprovecharse de Big Data: empresas  como Walmart, Google, y/o agentes financieros especializados. Actualmente con [Hadoop](https://hadoop.apache.org/ "Hadoop"), hardware de bajo coste (*commodity*) que utiliza el kernel de Linux, y el *cloud computing*, casi cualquier organización se lo puede permitir.
  
Basta considerar que hay una revolución de datos: los datos que se generan en el mundo aumentan anualmente un 40%.  Se estima que para el 2025 se crearán más de 180 zetabytes. Fuente: <https://es.statista.com/>. En consecuencia, todos esos datos que obtenemos deben ser tratados para ser convertidos en información y poder así tomar decisiones estratégicas.

## Objetivos del curso    

- Conocer las soluciones de Big Data presentes en el mercado como Apache Hadoop y Spark.
- Adquirir conocimientos para diseñar estrategias de business intelligence integrando data lakes y data warehouses.
- Desarrollar *Machine Learning in-house* usando Spark MLlib y TensorFlow.    
    
## Temario    
      
- Big Data: Definición y características: Big Data y el análisis de datos, Definición, Mercado, Big Data en España, Tendencias, 2021 Machine Learning, AI and Data (MAD) Landscape, MAD 2024, Gobierno de datos/Data governance, Apache Atlas, Serie de normas ISO/IEC 20547, NIST Big Data Interoperability Framework, Gestión de la calidad de los datos, Beneficios, Paradigma, Características: Las V de Big Data, Tipos de datos, Historia, Data warehouses / Data lakes / Lakehouses, Apache Hadoop y Apache Spark, Casos de uso y Buenas prácticas en Big Data, Tipos de análisis de datos en Big Data: descriptivo, predictivo y prescriptivo, Big Data analytics y Business Intelligence, Fuentes libres de datos, ASF: Herramientas para Big Data, Apache Hadoop, Módulos de Apache Hadoop.
  
- Ingesta y almacenamiento de datos: Procesos en Big Data, Ingestión de datos, Cuestiones a considerar, Buenas prácticas, Problemas en la ingesta de datos, Procesamiento de datos en tiempo real, Apache Spark, Apache Flume, Apache Flink, Sistemas de mensajería, Apache Kafka, Apache ActiveMQ, Apache Pulsar, Pub/Sub, Logstash, Apache Nifi, Apache Beam, Apache Samza, Apache Airflow, Astro, DBT, Otras herramientas (Mage AI, Fivetran, Stitch, Airbyte, Materialize), Modelo semántico de datos (SDM), Almacenamiento de datos (data storage): Persistencia políglota, Herramientas de almacenamiento para Big Data, HDFS, Apache Ozone, GlusterFS, Ceph, MinIO, Amazon services, MS Azure Data lake store, Google BigQuery, Data warehouses / Data lakes / Lakehouses, Snowflake, Databricks, Delta Lake, Apache Iceberg (Dremio), Apache Hudi, Apache XTable, NoSQL databases, Herramientas de la ASF para Big Data: Apache Mesos, Apache Zookeeper, Apache Ambari, Apache Ranger, Apache Sentry(attic).
  
- Bases de datos para Big Data: Formatos de archivo para Big Data (Apache ORC, Parquet, Avro, Arrow), Bases de datos NoSQL, Bases de datos de documentos: MongoDB, Versiones, Características, Principales funcionalidades, Apache CouchDB, Couchbase, Bases de datos con pares de valores: Redis, Arquitectura, Apache Ignite, Bases de datos columnares: Apache Cassandra, Tutorial Cassandra, Apache HBase, Características, Usos, Requisitos, Bases de datos de grafos: Neo4j, Stardog, Amazon Neptune.
  
- Consulta y visualización de datos: Procesos en Big Data, Procesamiento, análisis y consulta de datos, Apache Scoop(Attic), Motores de consultas, Apache Spark, Apache Impala, Apache Kudu, Apache Hive, Apache Drill, Presto, Trino, Otras herramientas: Hue, Alluxio, Analítica de datos en tiempo real, Apache Doris, Apache Druid, Apache Kylin, Apache Pinot, ClickHouse, Vertica, Perfilado y linaje (Talend Data Fabric, GX Core, OpenMetadata, OpenLineage, Marquez), Calidad de los datos, Limpieza de datos, Prevención y perdida de datos, Visualización de datos: Elastic Stack, Elasticsearch, Apache Lucene, Apache Sorl, Logstash, Kibana, Salesforce, Amazon, Google y Microsoft, Apache superset (Preset), Monitoreo de datos.
  
- Frameworks y aplicaciones para Big Data: Hadoop, Módulos: Hadoop YARN, Modelo de procesamiento DAG, Hadoop MapReduce, Sistemas de ficheros HDFS, Características, Proyectos relacionados con Apache Hadoop, Apache Spark, Características, Casos de uso, Apache Storm, Características, Storm vs. Spark, Apache Kafka, Características, Transmisión de eventos, Procesos.
- Big Data Science: Introducción a la ciencia de datos, Alcance, KDD, Minería de datos, Consideraciones, Cientista de datos, Procesos en la ciencia de datos, CRISP-DM, SEMMA.
- Big Data Stacks y Machine Learning: Apache Hadoop Stack, BDAS - Berkeley Data Analytics Stack, Stack alternativo, Cloudera, Big Data Cloud, Infraestructura de prueba de Big Data (BDTI). 
- Machine Learning(ML): Tensor Flow, Pasos en ML, Redes Neuronales, Entrenar una red neuronal, Apache MLib, Lenguajes soportados, Desempeño, Estadísticas:Correlación, Tácticas adversarias de ML, Caldera + Atlas.
  
    
## Bibliografía
```{bibliography}
``` 
