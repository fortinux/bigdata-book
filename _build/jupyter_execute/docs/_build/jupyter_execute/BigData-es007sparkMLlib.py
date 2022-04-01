#!/usr/bin/env python
# coding: utf-8

# # Tutorial Spark 

# - Para realizar este tutorial abrimos un cuaderno de Jupyter <https://jupyter.org/> en nuestro servidor local o utilizamos Colaboratory: <https://colab.research.google.com>.
# - Los pasos son los siguientes:

# - Actualizamos nuestro sistema operativo e instalamos Java y Scala

# In[1]:


apt update


# In[ ]:


apt upgrade --fix-broken


# In[ ]:


apt install default-jre


# In[ ]:


apt autoremove


# In[ ]:


apt install default-jdk


# In[ ]:


apt install scala


# In[6]:


java -version


# In[7]:


javac -version


# In[ ]:


scala -version


# In[9]:


readlink -f $(which java)


# - Descargamos e instalamos Spark

# In[24]:


wget -q https://dlcdn.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz


# In[17]:


wget https://downloads.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz.asc


# In[ ]:


wget https://downloads.apache.org/spark/spark-3.2.1/spark-3.2.1-bin-hadoop3.2.tgz.sha512


# In[19]:


wget https://downloads.apache.org/spark/KEYS


# In[ ]:


gpg --import KEYS


# In[21]:


gpg --verify spark-3.2.1-bin-hadoop3.2.tgz.asc  spark-3.2.1-bin-hadoop3.2.tgz


# In[ ]:


ls


# In[ ]:


tar xvf spark-3.2.1-bin-hadoop3.2.tgz


# - Instalamos e configuramos la biblioteca de Python *findspark*

# In[26]:


pip install -q findspark


# In[29]:


pwd


# In[ ]:


ls


# In[31]:


import os
os.environ["JAVA_HOME"] = "/usr/lib/jvm/java-11-openjdk-amd64"
os.environ["SPARK_HOME"] = "spark-3.2.1-bin-hadoop3.2"


# - Utilizamos la biblioteca *findspark* para crear un *dataframe* 

# In[ ]:


import findspark
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()


# In[ ]:


df = spark.createDataFrame([{"Hola": "mundo"} for x in range(1000)])
df.show(3, False)


# ## Extraer, transformar y selecionar

# - Importamos la biblioteca *pyspark*

# In[36]:


import pyspark
print(pyspark.__version__)


# ## Transformar

# - Transformar significa escalar, convertir o modificar las características de los datos.

# -  Uno de los primeros pasos en NLP (Natural Language Processing) es convertir el texto en tokens o palabras *tokenizadas*.

# In[ ]:


from pyspark.ml.feature import Tokenizer


# In[ ]:


oraciones_df = spark.createDataFrame([
    (1, "Introducción a sparkMlib"),
    (2, "Mlib incluye bibliotecas para clasificación y regresión"),
    (3, "También incluye soporte a datapipe lines"),
    
], ["id", "oraciones"])


# In[ ]:


oraciones_df.show()


# - Para reflejar la importancia de una palabra en un texto utilizamos *Term frequency-inverse document frequency (TF-IDF)*.

# In[ ]:


sent_token = Tokenizer(inputCol = "oraciones", outputCol = "palabras")
sent_tokenized_df = sent_token.transform(oraciones_df)


# In[ ]:


sent_tokenized_df.take(10)


# In[ ]:


from pyspark.ml.feature import HashingTF, IDF
hashingTF = HashingTF(inputCol = "palabras", outputCol = "rawfeatures", numFeatures = 20)
sent_fhTF_df = hashingTF.transform(sent_tokenized_df)


# In[ ]:


sent_fhTF_df.take(1)


# In[ ]:


idf = IDF(inputCol = "rawfeatures", outputCol = "idffeatures")
idfModel = idf.fit(sent_fhTF_df)
tfidf_df = idfModel.transform(sent_fhTF_df)


# In[ ]:


tfidf_df.take(1)


# - Fuente: <https://spark.apache.org/docs/3.0.1/ml-features.html#tokenizer>

# - Utilizamos la clase StandardScaler para estandarizar datos en ML.
# - Los escala entre -1 y 1.

# In[ ]:


from pyspark.ml.feature import  StandardScaler
from pyspark.ml.linalg import Vectors


# In[ ]:


features_df = spark.createDataFrame([
    (1, Vectors.dense([10.0,10000.0,1.0]),),
    (2, Vectors.dense([20.0,40000.0,2.0]),),
    (3, Vectors.dense([30.0,50000.0,3.0]),),
    
],["id", "features"] )


# In[ ]:


features_stand_scaler = StandardScaler(inputCol = "features", outputCol = "sfeatures", withStd=True, withMean=True)
stmodel = features_stand_scaler.fit(features_df)
stand_sfeatures_df = stmodel.transform(features_df)


# In[ ]:


stand_sfeatures_df.show()


# - Fuente: MA Raza, Ph.D. <https://towardsdatascience.com/machine-learning-with-spark-f1dbc1363986>.
# - Spark docs: <https://spark.apache.org/docs/3.0.1/ml-features.html#standardscaler>.

# - Utilizamos la clase MinMaxScaler en ML para normalizar datos numéricos. 
# - Escala los datos entre 0 y 1.

# In[ ]:


from pyspark.ml.feature import MinMaxScaler
from pyspark.ml.linalg import Vectors


# In[ ]:


features_df = spark.createDataFrame([
    (1, Vectors.dense([10.0,10000.0,1.0]),),
    (2, Vectors.dense([20.0,40000.0,2.0]),),
    (3, Vectors.dense([30.0,50000.0,3.0]),),
    
],["id", "features"] )


# In[ ]:


features_df.show()


# - Aplicamos la transformación de la biblioteca MinMaxScaler.

# In[ ]:


features_scaler = MinMaxScaler(inputCol = "features", outputCol = "sfeatures")
smodel = features_scaler.fit(features_df)
sfeatures_df = smodel.transform(features_df)


# In[ ]:


sfeatures_df.show()


# - Fuente: <https://spark.apache.org/docs/3.0.1/ml-features.html#minmaxscaler>
# - El ejemplo completo se encuentra en *examples/src/main/python/ml/min_max_scaler_example.py* dentro del repositorio de Spark.

# - La clase Bucketizer transforma los datos en varias frecuencias o *buckets*.

# In[ ]:


from pyspark.ml.feature import  Bucketizer
from pyspark.ml.linalg import Vectors


# In[ ]:


splits = [-float("inf"), -10, 0.0, 10, float("inf")]
b_data = [(-800.0,), (-10.5,), (-1.7,), (0.0,), (8.2,), (90.1,)]
b_df = spark.createDataFrame(b_data, ["features"])


# In[ ]:


b_df.show()


# In[ ]:


bucketizer = Bucketizer(splits=splits, inputCol= "features", outputCol="bfeatures")
bucketed_df = bucketizer.transform(b_df)


# In[ ]:


bucketed_df.show()


# Fuente: <https://spark.apache.org/docs/3.0.1/ml-features.html#bucketizer>

# ## Clustering

# - Para agrupar datos en un razonable grupo de frecuencias se puede utilizar como técnica el llamado *clustering*.

# In[ ]:


from pyspark.ml.clustering import KMeans
from pyspark.ml.evaluation import ClusteringEvaluator
import glob


# In[37]:


# Carga los datos
dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")


# In[ ]:


# Entrena el modelo k-means
kmeans = KMeans().setK(2).setSeed(1)
model = kmeans.fit(dataset)


# In[ ]:


# Hace predicciones
predictions = model.transform(dataset)


# In[ ]:


# Evalua utilizando Silhouette score
evaluator = ClusteringEvaluator()


# In[ ]:


silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))


# In[ ]:


# Shows the result.
centers = model.clusterCenters()
print("Cluster Centers: ")
for center in centers:
    print(center)


# - Fuente: <https://spark.apache.org/docs/3.0.1/ml-clustering.html#k-means>

# - Otro algoritmo de *clustering* implementado en MLlib es el llamado *Bisecting K-Means*.

# In[ ]:


from pyspark.ml.clustering import BisectingKMeans
from pyspark.ml.evaluation import ClusteringEvaluator


# In[ ]:


# Carga de datos
dataset = spark.read.format("libsvm").load("data/mllib/sample_kmeans_data.txt")


# In[ ]:


# Entrenamiento del modelo bisecting k-means
bkm = BisectingKMeans().setK(2).setSeed(1)
model = bkm.fit(dataset)


# In[ ]:


# Hace predicciones
predictions = model.transform(dataset)


# In[ ]:


# Evalua utilizando Silhouette score
evaluator = ClusteringEvaluator()

silhouette = evaluator.evaluate(predictions)
print("Silhouette with squared euclidean distance = " + str(silhouette))


# In[ ]:


# Muestra los resultados
print("Cluster Centers: ")
centers = model.clusterCenters()
for center in centers:
    print(center)


# Fuente: <https://spark.apache.org/docs/3.0.1/ml-clustering.html#bisecting-k-means>

# ## Regresión utilizando PySpark

# - En este ejemplo se realizara una regresión logística binomial.

# In[ ]:


from pyspark.ml.classification import LogisticRegression


# In[ ]:


# Se cargan los datos
training = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")


# In[ ]:


lr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8)


# In[ ]:


# Ajusta el modelp
lrModel = lr.fit(training)


# In[ ]:


# Imprime los coeficientes y el intercepto para la regresión logística
print("Coefficients: " + str(lrModel.coefficients))
print("Intercept: " + str(lrModel.intercept))


# In[ ]:


# Se puede usar también la familia multinomial para clasificación binaria
mlr = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8, family="multinomial")


# In[ ]:


# Ajusta el modelo
mlrModel = mlr.fit(training)


# In[ ]:


# Imprima los coeficientes e intersecciones para la regresión logística con familia multinomial
print("Multinomial coefficients: " + str(mlrModel.coefficientMatrix))
print("Multinomial intercepts: " + str(mlrModel.interceptVector))


# - Fuente: <https://spark.apache.org/docs/3.0.1/ml-classification-regression.html#binomial-logistic-regression>

# ## La clasificación Naive Bayes

# In[ ]:


from pyspark.ml.classification import NaiveBayes
from pyspark.ml.evaluation import MulticlassClassificationEvaluator


# - Creamos los *splits* de entrenamiento y test:

# In[ ]:


data = spark.read.format("libsvm")     .load("data/mllib/sample_libsvm_data.txt")

splits = data.randomSplit([0.6, 0.4], 1234)
train = splits[0]
test = splits[1]


# - Aplicamos la clasificación Naive bayes:

# In[ ]:


nb = NaiveBayes(smoothing=1.0, modelType="multinomial")
model = nb.fit(train)
predictions = model.transform(test)


# In[ ]:


predictions.show()


# - Evaluamos el clasificador entrenado:

# In[ ]:


evaluator = MulticlassClassificationEvaluator(labelCol="label", predictionCol="prediction",
                                              metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("Test set accuracy = " + str(accuracy))


# - Fuente: <https://spark.apache.org/docs/3.0.1/ml-classification-regression.html#naive-bayes>

# ## Clasificación con árboles de decisión

# In[ ]:


from pyspark.ml import Pipeline
from pyspark.ml.classification import DecisionTreeClassifier
from pyspark.ml.feature import StringIndexer, VectorIndexer
from pyspark.ml.evaluation import MulticlassClassificationEvaluator


# In[ ]:


# Cargar los datos en formato LIBSVM como un DataFrame
data = spark.read.format("libsvm").load("data/mllib/sample_libsvm_data.txt")

# Index labels agregan metadata a la columna label
# Ajuste en todo el conjunto de datos para incluir todas las etiquetas en el índice
labelIndexer = StringIndexer(inputCol="label", outputCol="indexedLabel").fit(data)

# Identifica automáticamente características categóricas y las indexa
# Especifica maxCategories para que las entidades con > 4 valores distintos se traten como continuas
featureIndexer =    VectorIndexer(inputCol="features", outputCol="indexedFeatures", maxCategories=4).fit(data)


# In[ ]:


# Divide los datos en conjuntos de entrenamiento y prueba (30% retenido para prueba)
(trainingData, testData) = data.randomSplit([0.7, 0.3])

# Entrena el modelo DecisionTree
dt = DecisionTreeClassifier(labelCol="indexedLabel", featuresCol="indexedFeatures")

# Encadena índices y árboles en tuna Pipeline
pipeline = Pipeline(stages=[labelIndexer, featureIndexer, dt])

# Entrena el modelo y ejecuta los indexadores
model = pipeline.fit(trainingData)

# Hace predicciones
predictions = model.transform(testData)

# Selecciona filas de jemplo para mostrar
predictions.select("prediction", "indexedLabel", "features").show(5)

# Selecciona (predicción, etiqueta verdadera) y calcula el error de prueba
evaluator = MulticlassClassificationEvaluator(
    labelCol="indexedLabel", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictions)
print("Test Error = %g " % (1.0 - accuracy))

treeModel = model.stages[2]
# Resumen
print(treeModel)


# - Fuente: <https://spark.apache.org/docs/3.0.1/ml-classification-regression.html#decision-tree-classifier>
# - Se pueden encontrar otros algoritmos de clasificación de la biblioteca Spark MLLib en:     
# <https://spark.apache.org/docs/3.0.1/ml-classification-regression.html#classification>
