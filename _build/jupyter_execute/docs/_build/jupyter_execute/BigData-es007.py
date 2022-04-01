#!/usr/bin/env python
# coding: utf-8

# # Big Data tema 7

# ## Big data stacks

# - Teniendo en cuenta las numerosas opciones que existen en el mercado para implantar una solución de Big data en la organización, se enumeran a continuación tres arquitecturas que tienen en cuenta los procesos de ingestión de datos, almacenamiento, tratamiento y análisis de datos, y presentación.

# ## Apache Hadoop Stack

# - La biblioteca de software Apache Hadoop es un framework para el procesamiento distribuido de grandes conjuntos de datos en grupos de computadoras.
#     - Fuente: <https://hadoop.apache.org/>.

# - Ingestión de datos: Apache Flume, Apache Nifi. 
#     - Mensajería: Apache Kafka.
# - Almacenamiento: 
#     - Gestión de recursos: Apache Hadoop YARN.
#     - Sistema de ficheros: HDFS.
#     - Datalakes/Datawarehouses: Databrics, Snowflake.
#     - Bases de datos: Apache Cassandra, Apache HBase.

# - Análisis y tratamiento de los datos: Apache Hadoop MapReduce, Apache Spark, Apache Flink.
#     - SQL: Apache Hive, Apache Pig.
#     - ML: Apache Mahout, Apache Spark MLLib.
#     - Orquestación: Apache Zookeeper.
# - Presentación: Kibana, Grafana.
# - Gestión: 
#     - Seguridad: Apache Zookeeper.
#     - Gobernanza: Apache Atlas.

# ## BDAS - Berkeley Data Analytics Stack

# - BDAS (*Berkeley Data Analytics Stack*) es un stack de software open source que integra componentes creados por el AMPLab para Big Data, entre ellos, el framework *Apache Spark*.
#     - Fuente: https://amplab.cs.berkeley.edu/software/

# - Ingestión de datos: Apache Flume, Apache Nifi. 
#     - Mensajería: Apache Kafka.
# - Almacenamiento: 
#     - Gestión de recursos: Apache Mesos, Apache Hadoop YARN.
#     - Sistema de ficheros: HDFS, S3, Ceph.
#     - Datalakes/Datawarehouses: Alluxio.
#     - Bases de datos: Apache Cassandra, Apache HBase.

# - Análisis y tratamiento de los datos: Apache Spark.
#     - ML: Apache Spark MLLib.
#     - Orquestación: Apache Zookeeper, Apache Airflow.
# - Presentación: Google Looker, Microsoft Power BI, Tableau.
# - Gestión: 
#     - Seguridad: Apache Zookeeeper.
#     - Gobernanza: Apache Atlas.

# ## Big data stack alternativo

# - Este es un ejemplo de un stack basado en un artículo de la empresa *dbt*.
#     - <https://blog.getdbt.com/future-of-the-modern-data-stack/>.

# - Ingestión de datos: Fivetran, Stitch. 
# - Almacenamiento: 
#     - Gestión de recursos: Apache Hadoop YARN.
#     - Sistema de ficheros: S3, Kubernetes.
#     - Datalakes/Datawarehouses: Snowflake, Databricks, Bigquery, Redshift.
# - Análisis y tratamiento de los datos: dbt.
# - Presentación: Looker, Mode, Periscope.

# ## Big data cloud

# - En esta comparación de productos para big data y análisis se presentan las soluciones que ofrecen los tres grandes actores del mundo de servicios *cloud computing*. 

# - Ingestión de datos: Amazon Kinesis/Glue, Azure Synapse Analytics, Google Dataflow.
# - Almacenamiento: 
#     - AWS Simple Storage Service (S3), Azure Blob Storage, Google Cloud Storage.
# - Datalakes/Datawarehouses: 
#     - Amazon Redshift, Azure SQL Data Warehouse (SQL DW), Google BigQuery.
# - Bases de datos: 
#     - Amazon Relational Database Service, Azure SQL Database, Google Cloud SQL.

# - Análisis y tratamiento de los datos: 
#     - Amazon Kinesis, Azure Synapse Analytics, Google Cloud Smart Analytics Platform.
#     - ML: Amazon SageMaker, Azure Machine Learning, Google Cloud Machine Learning Engine.
# - Presentación: 
#     - Amazon OpenSearch, Microsoft Power BI, Google Looker.

# - Amazon EMR es un servicio gestionado que permite procesar y analizar datos utilizando herramientas y frameworks como Apache Hadoop, Spark, HBase, y Presto.
#     - <https://aws.amazon.com/es/emr/>
# - Azure HDInsight es una solución completa de Apache Hadoop, Spark, R Server, HBase y Storm en la nube.
#     - <https://azure.microsoft.com/es-es/services/hdinsight/>
# - Google Dataproc es un servicio totalmente gestionado y escalable que permite ejecutar Apache Spark, Apache Flink, y más de 30 herramientas y frameworks de código abierto. 
#     - <https://cloud.google.com/dataproc>

# - Enlaces:
#     - <https://aws.amazon.com/es/big-data/datalakes-and-analytics/>.
#     - <https://aws.amazon.com/es/architecture/analytics-big-data/>
#     - <https://azure.microsoft.com/es-es/services/>.
#     - <https://cloud.google.com/solutions/smart-analytics>.

# - Arquitectura Big data en Amazon
#     - Modern Data Analytics Reference Architecture on AWS.
#     - <https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/modern-data-analytics-using-lake-house-ra.pdf>.

# - Ejemplo Azure
#     - Análisis de un extremo a otro con Azure Synapse.
#     - <https://docs.microsoft.com/es-es/azure/architecture/example-scenario/dataplate2e/data-platform-end-to-end>.

# - Ejemplo Google
#     - How Renault solved scaling and cost challenges on its Industrial Data platform using BigQuery and Dataflow.
#     - <https://cloud.google.com/blog/topics/manufacturing/renault-improves-its-industrial-data-platform-with-bigquery>.

# ## Machine Learning

# - Si bien se viene estudiando la forma de hacer que las máquinas puedan aprender por si solas desde 1970 aproximadamente, no fue hasta 1983 cuando se publicó *Machine learning: The AI Apprioach*, que la disciplina de *Machine learning* tomó el impulso luego sistematizado en el libro de T. Mitchell *Machine Learning* (1997).     

# Fuente: {cite:ps}`Kubat2017`

# ## TensorFlow

# - El aprendizaje automático es la práctica de ayudar al software a realizar una tarea sin programación o reglas explícitas.
# - Con la programación tradicional de computadoras, un programador especifica las reglas que debe usar la computadora.
#     - Extraído de TensorFlow: <https://www.tensorflow.org/about>.

# - Sin embargo, ML requiere una mentalidad diferente.
# - El aprendizaje automático del mundo real se centra mucho más en el análisis de datos que en la codificación.
# - Los programadores proporcionan un conjunto de ejemplos y la computadora aprende patrones a partir de los datos.
# - Se puede entender el aprendizaje automático como "programación con datos".

# ## Pasos en ML

# - Paso 1: recopilar datos.
# - Paso 2: Explorar los datos.
# - Paso 2.5: Eligir un modelo.
# - Paso 3: Preparar los datos.
# - Paso 4: construir, entrenar y evaluar el modelo.
# - Paso 5: Sintonizar los hiperparámetros.
# - Paso 6: Implementar el modelo.

# - Extraído de Maching Learning:    
# - <https://developers.google.com/machine-learning/guides/text-classification/>.

# ## Redes neuronales

# - Es un tipo de modelo que se puede entrenar para reconocer patrones.
# - Está compuesto por capas, incluidas las de entrada y salida, y al menos una capa oculta.
# - Las neuronas de cada capa aprenden representaciones cada vez más abstractas de los datos.

# - Extraído de TensorFlow: <https://www.tensorflow.org/about>.

# ## Entrenar una red neuronal

# - Las redes neuronales se entrenan por descenso de gradiente.
# - Los pesos en cada capa comienzan con valores aleatorios, y estos se mejoran iterativamente con el tiempo para hacer que la red sea más precisa.
# - Se usa una función de pérdida para cuantificar qué tan imprecisa es la red, y se usa un procedimiento llamado retropropagación para determinar si se debe aumentar o disminuir cada peso para reducir la pérdida.

# ## Apache MLlib

# - MLlib es la biblioteca escalable de aprendizaje automático (ML) de Apache Spark.
# - Su objetivo es hacer que el aprendizaje automático práctico sea escalable y fácil.
#     - Fuente: <https://spark.apache.org/mllib/>.

# - Las utilidades de flujo de trabajo de ML incluyen:
#      - Algoritmos de ML: algoritmos de aprendizaje comunes como clasificación, regresión, agrupamiento y filtrado colaborativo.
#      - Caracterización: extracción de características, transformación, reducción de dimensionalidad y selección.
#         - Fuente: <https://spark.apache.org/docs/latest/ml-guide.html>.

# - Pipelines: 
#     - Incluye herramientas para construir, evaluar y ajustar ML Pipelines.
# - Persistencia: 
#     - Guarda y carga algoritmos, modelos y Pipelines.
# - Utilidades: 
#     - Disponibles para álgebra lineal, estadística, manejo de datos, etc.

# ## Lenguajes soportados por MLlib

# - MLlib utiliza las API de Spark e interactúa con NumPy en las bibliotecas de Python y R.
# - Puede usar cualquier fuente de datos de Hadoop (por ejemplo, HDFS, HBase o archivos locales), lo que facilita la conexión a los flujos de trabajo de Hadoop.

# ## Desempeño de MLlib

# - Algoritmos de alta calidad, 100 veces más rápidos que MapReduce.
# - Spark sobresale en el cálculo iterativo, lo que permite que MLlib se ejecute rápidamente.
# - MLlib contiene algoritmos de alta calidad que aprovechan la iteración y pueden generar mejores resultados que las aproximaciones de un solo paso que a veces se usan en MapReduce.

# - Se puede ejecutar Spark con su modo de clúster independiente, en EC2, en Hadoop YARN, en Mesos o en Kubernetes.
# - Acceso a datos en HDFS, Apache Cassandra, Apache HBase, Apache Hive y cientos de otras fuentes de datos.

# ## Estadísticas en MLlib

# - Correlación:
#      - Los métodos admitidos actualmente son la correlación de Pearson y Spearman.
# - Prueba de hipótesis:
#      - spark.ml actualmente es compatible con las pruebas de independencia chi-cuadrado (*Chi-squared - χ2*) de Pearson.

# - Resumidor (*summarizer*):
#      - Proporciona estadísticas de resumen de columnas vectoriales para el *dataframe* a través de *Summarizer*. 
#      - Las métricas disponibles son el máximo, el mínimo, la media, la suma, la varianza, la desviación estándar y la cantidad de valores distintos de cero por columna, así como el recuento total.

# ## Estadísticas: correlación

# - La correlación calcula la matriz de correlación para el conjunto de datos de vectores de entrada utilizando el método especificado. 
# - La salida será un *dataframe* que contiene la matriz de correlación de la columna de vectores. 

# In[1]:


# Ejemplo de correlación en Python 
# Fuente:
# https://spark.apache.org/docs/latest/ml-statistics.html

from pyspark.ml.linalg import Vectors
from pyspark.ml.stat import Correlation

data = [(Vectors.sparse(4, [(0, 1.0), (3, -2.0)]),),
        (Vectors.dense([4.0, 5.0, 0.0, 3.0]),),
        (Vectors.dense([6.0, 7.0, 0.0, 8.0]),),
        (Vectors.sparse(4, [(0, 9.0), (3, 1.0)]),)]

df = spark.createDataFrame(data, ["features"])

r1 = Correlation.corr(df, "features").head()
print("Pearson correlation matrix:\n" + str(r1[0]))

r2 = Correlation.corr(df, "features", "spearman").head()
print("Spearman correlation matrix:\n" + str(r2[0]))


# - El código fuente del ejemplo completo se encuentra en *examples/src/main/python/ml/correlation_example.py* en el repositorio de Spark. 
# - Fuente: <https://spark.apache.org/docs/latest/ml-guide.html>.

# ## Tácticas adversarias en ML

# - Adversarial Machine Learning Threat Matrix es un framework abierto centrado en la industria para empoderar a los analistas de seguridad para detectar, responder y remediar amenazas contra sistemas de ML. 
# - Recientemente este framework se ha ampliado conviertiéndose en MITRE ATLAS, Adversarial Threat Landscape for Artificial-Intelligence Systems.

# - MITRE ATLAS, Adversarial Threat Landscape for Artificial-Intelligence Systems, es una base de conocimiento de tácticas adversarias, técnicas y estudios de casos para sistemas de aprendizaje automático (ML) basados en observaciones del mundo real, demostraciones de equipos rojos y grupos de seguridad de ML, y el estado de lo posible a partir de la investigación académica. 
# - ATLAS sigue el modelo del marco MITRE ATT&CK® y sus tácticas y técnicas son complementarias a las de ATT&CK.
#     - Extraído de: <https://atlas.mitre.org/> 

# - Estas tácticas adversarias pueden ser:
#     - Hacer que el sistema ML aprenda algo incorrecto (envenenamiento de datos),
#     - Hacer algo incorrecto (ataques de evasión), o
#     - Revelar lo incorrecto (inversión del modelo).

# - Extraído de: [SEI](https://insights.sei.cmu.edu/cert/2020/10/adversarial-ml-threat-matrix-adversarial-tactics-techniques-and-common-knowledge-of-machine-learning.html).
# - Repositorio Github: 
# - <https://github.com/mitre/advmlthreatmatrix>. 

# ## Tutorial MLlib

# - Práctica: Aplicaciones de ML en datasets.
# - <https://colab.research.google.com/github/tensorflow/docs/blob/master/site/en/tutorials/quickstart/beginner.ipynb>
# - <https://towardsdatascience.com/machine-learning-with-spark-f1dbc1363986>
# - <https://sparkbyexamples.com/>
