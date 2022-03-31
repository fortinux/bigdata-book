#!/usr/bin/env python
# coding: utf-8

# # Big Data tema 6

# ## Elastic Stack

# - El ELK Stack se compone de las aplicaciones Elasticsearch, Logstash, Kibana, y Beats.
# - Actualmente se lo conoce como Elastic Stack, nombre que le permite agregar nuevas funcionalidades denominadas *beats*.

# - Elasticsearch 8.0
# - Logstash 8.0
# - Kibana 8.0
# - Beats 8.0

# - Extraído de: <https://www.elastic.co/what-is/elasticsearch>.

# ## Casos de uso

# - Búsqueda de aplicaciones
# - Búsqueda de sitio web
# - Búsqueda Empresarial
# - Logging y analíticas de log
# - Métricas de infraestructura y monitoreo de contenedores
# - Monitoreo de rendimiento de aplicaciones
# - Análisis y visualización de datos geoespaciales
# - Analítica de Seguridad
# - Analítica de Negocios

# ## Elasticsearch

# - Elasticsearch es un motor de análisis y búsqueda de código abierto distribuido para todo tipo de datos, incluidos textuales, numéricos, geoespaciales, estructurados y no estructurados.
# - Elasticsearch se basa en Apache Lucene y fue lanzado por primera vez en 2010 por Elasticsearch N.V. (ahora conocido como Elastic). 
#     - Extraído de: <https://www.elastic.co/>.

# - Conocido por sus API REST simples, naturaleza distribuida, velocidad y escalabilidad, Elasticsearch es el componente central de Elastic Stack, un conjunto de herramientas de código abierto para la ingesta, el enriquecimiento, el almacenamiento, el análisis y la visualización de datos.

# - La ingesta de datos es el proceso mediante el cual estos datos sin procesar se analizan, normalizan y enriquecen antes de indexarlos en Elasticsearch. 
# - Los datos sin procesar fluyen hacia Elasticsearch desde una variedad de fuentes, incluidos registros, métricas del sistema y aplicaciones web.

# ## Apache Lucene

# - Lucene Core es una biblioteca de Java que proporciona potentes funciones de indexación y búsqueda, así como funciones de corrección ortográfica, resaltado de aciertos y análisis/tokenización avanzados.
#     - Extraído de: <https://lucene.apache.org/>.

# - Entre los proyectos relacionados se encuentra PyLucene que proporciona enlaces de Python para Lucene Core. 
# - PyLucene incorpora una VM de Java con Lucene en un proceso de Python.
# - El módulo de Python llamado *lucene* es generado por máquina por JCC.
#     - Extraído de: <https://lucene.apache.org/pylucene/>.    

# - Lucene Core tiene una serie de proyectos relacionados, entre los cuales se encuentran: 

# - Manifold: Framework de código abierto para conectar repositorios de contenido de origen, como Microsoft Sharepoint y EMC Documentum, a repositorios o índices de destino, como Apache Solr, Open Search Server o ElasticSearch.
#     - <https://manifoldcf.apache.org/en_US/index.html>. 
# - LUCENE.net: biblioteca de motor de búsqueda de alto rendimiento para .NET
#     - <https://lucenenet.apache.org/>.

# - Apache Tika: El kit de herramientas Apache Tika detecta y extrae metadatos y texto de más de mil tipos de archivos diferentes (como PPT, XLS y PDF). Todos estos tipos de archivos se pueden analizar a través de una sola interfaz, lo que hace que Tika sea útil para la indexación de motores de búsqueda, el análisis de contenido, la traducción y mucho más.
#     - <https://tika.apache.org/>

# - Nutch es un rastreador web altamente extensible, altamente escalable, maduro y listo para producción que permite una configuración detallada y se adapta a una amplia variedad de tareas de adquisición de datos.
#     - <https://nutch.apache.org/>.

# - La biblioteca Apache OpenNLP es un conjunto de herramientas basado en el aprendizaje automático para el procesamiento de texto en lenguaje natural.
# - Admite las tareas más comunes de NLP, como la tokenización, la segmentación de oraciones, el etiquetado de partes del discurso, la extracción de entidades nombradas, la fragmentación, el análisis y la resolución de correferencias.
#     - Extraído de: <https://opennlp.apache.org/>.

# - Apache Mahout es un framework distribuido de álgebra linear y Scala DSL que tiene como objetivo crear aplicaciones de aprendizaje automático (ML) escalables y eficaces. 
#     - <https://mahout.apache.org/>.

# ## Apache Solr

# - Solr es un servidor de búsqueda de alto rendimiento creado con Lucene Core.
# - Solr es altamente escalable y proporciona indexación, búsqueda y análisis distribuidos totalmente tolerantes a fallas.
# - Expone las características de Lucene a través de interfaces JSON/HTTP fáciles de usar o de clientes nativos para Java y otros lenguajes. 
#     - Extraído de: <https://lucene.apache.org/>.

# - Tutorial Sorl: 
#     - <https://solr.apache.org/guide/8_11/solr-tutorial.html/>.

# ## Logstash

# - Logstash se usa para agregar y procesar datos y enviarlos a Elasticsearch.
# - Es una canalización (*pipeline*) de procesamiento de datos del lado del servidor de código abierto que le permite ingerir datos de múltiples fuentes simultáneamente y enriquecerlos y transformarlos antes de que se indexen en Elasticsearch.

# - Un índice de Elasticsearch es una colección de documentos que están relacionados entre sí.
# - Elasticsearch almacena datos como documentos JSON.
# - Cada documento correlaciona un conjunto de claves (nombres de campos o propiedades) con sus valores correspondientes (cadenas, números, booleanos, fechas, matrices de valores, geolocalizaciones u otros tipos de datos).

# - Elasticsearch utiliza una estructura de datos denominada índice invertido, que está diseñada para permitir búsquedas de texto completo muy rápidas.
# - Un índice invertido enumera cada palabra única que aparece en cualquier documento e identifica todos los documentos en los que aparece cada palabra.

# - La indexación se inicia con la API de índice, a través de la cual puede agregar o actualizar un documento JSON en un índice específico.
# - Durante el proceso de indexación, Elasticsearch almacena documentos y crea un índice invertido para que los datos del documento se puedan buscar casi en tiempo real.

# - Una vez indexados en Elasticsearch, los usuarios pueden ejecutar consultas complejas en sus datos y usar agregaciones para recuperar resúmenes complejos de sus datos.
# - Desde Kibana, los usuarios pueden crear potentes visualizaciones de sus datos, compartir paneles y administrar el Elastic Stack.

# ## Elasticsearch Kibana

# - Kibana es una herramienta de visualización y gestión de datos para Elasticsearch que brinda histogramas en tiempo real, gráficos circulares y mapas. 
# - Kibana también incluye aplicaciones avanzadas, como Canvas, que permite a los usuarios crear infografías dinámicas personalizadas con base en sus datos, y Elastic Maps para visualizar los datos geoespaciales.

# ## Lenguajes soportados

# - Elasticsearch soporta una variedad de lenguajes de programación facilitando clientes para:
#     - Java
#     - JavaScript (Node.js)
#     - Go
#     - .NET (C#)
#     - PHP
#     - Perl
#     - Python
#     - Ruby

# ## Herramientas para la línea de comandos

# - elasticsearch-certgen
# - elasticsearch-certutil
# - elasticsearch-croneval
# - elasticsearch-keystore
# - elasticsearch-migrate

# - Font: <https://www.elastic.co/guide/en/elasticsearch/reference/current/commands.html>.

# - elasticsearch-node
# - elasticsearch-saml-metadata
# - elasticsearch-setup-passwords
# - elasticsearch-shard
# - elasticsearch-syskeygen
# - elasticsearch-users

# ## Kibana dev tools

# In[1]:


# Un documento puede contener varios campos con valores

{
  "name" : "Elastic",
  ...
  <field> : <value>
}


# - Fuente: (assets.contentstack.io) [<https://assets.contentstack.io/v3/assets/bltefdd0b53724fa2ce/blt56ad3f4e2c755f29/5d37c1602a506857d64eff48/es_commands.txt>]

# ## Tutorial Elasticsearch

# - Descargar e instalar la máquina virtual de elasticsearch en Bitnami
# - <https://bitnami.com/stack/elasticsearch/virtual-machine>. 
