#!/usr/bin/env python
# coding: utf-8

# # Tutorial Apache Hadoop

# - El proyecto Apache™ Hadoop® desarrolla software de código abierto para computación distribuida, escalable y confiable.
#     - Extraído de: <https://hadoop.apache.org/>.

# - Apache Hadoop es un framework para el procesamiento distribuido de grandes conjuntos de datos en grupos de computadoras que utilizan modelos de programación simples.
# - Diseñado para escalar desde servidores individuales a miles de máquinas, cada una de las cuales ofrece computación y almacenamiento locales.

# - En lugar de depender del hardware para brindar alta disponibilidad, la biblioteca en sí está diseñada para detectar y manejar fallas en la capa de la aplicación, por lo que brinda un servicio de alta disponibilidad sobre un grupo de computadoras, cada una de las cuales puede ser propensa a fallas.

# ## Configuración inicial

# - La máquina virtual con Hadoop instalado se descarga de:
# - <https://bitnami.com/stack/hadoop/virtual-machine>.
# - Se puede acceder a la información sobre la configuración predeterminada de la máquina virtual de Bitnami en:
# - <https://docs.bitnami.com/virtual-machine/apps/hadoop/get-started/understand-default-config/>.

# - Una vez instalado Apache Hadoop se deberán abrir los puertos del servidor para los distintos servicios web del framework.

# In[1]:


sudo ufw allow 8042, 8088, 8188, 19888, 9780, 9868, 9864, 10002 proto tcp


# - Mostrar el estado de los servicios

# In[ ]:


sudo /opt/bitnami/ctlscript.sh status


# - Iniciar un servicio

# In[ ]:


sudo /opt/bitnami/ctlscript.sh start


# - Reiniciar un servicio

# In[ ]:


sudo /opt/bitnami/ctlscript.sh restart apache


# - Detener todos los servicios

# In[ ]:


sudo /opt/bitnami/ctlscript.sh stop


# # Ejecutar tareas de pruebas en Hadoop 

# - Ejecutar una tarea (job) de test en Hadoop con mapreduce
# - Este ejemplo obtiene una estimación del número PI

# In[ ]:


hadoop jar /opt/bitnami/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar pi 10 100


# - Ejecutar una tarea con mapreduce involucrando a HDFS
# - Este ejemplo cuenta la cantidad de palabras y letras c que aparecen en el texto

# In[ ]:


echo "A Cuesta le cuesta subir la cuesta y en medio de la cuesta va y se acuesta." | \ 
hadoop fs -put - /tmp/hdfs-ejemplo-input


# In[ ]:


hadoop jar /opt/bitnami/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-*.jar grep /tmp/hdfs-ejemplo-input /tmp/hdfs-ejemplo-output 'c*'


# In[ ]:


hadoop fs -cat /tmp/hdfs-ejemplo-output/part-r-00000


# ## Apache Hive

# - Para conectarse a Hive a través de la interfaz web:
# - <http://localhost:10002>

# - Para conectarse a Hive a través de un túnel SSH:

# In[ ]:


beeline -u jdbc:hive2://localhost:10000 -n hadoop


# - Acceder a la información básica

# In[ ]:


help


# - Crear una base de datos

# In[ ]:


show databases;
show tables;


# In[ ]:


CREATE DATABASE basededatos;    # También se puede usar la orden CREATE SCHEMA


# - También se puede utilizar JDBC para crear una base de datos.
# - El script se guarda en un fichero llamado HiveCreateDb.java con el siguiente código:

# In[ ]:


import java.sql.SQLException;
import java.sql.Connection;
import java.sql.ResultSet;
import java.sql.Statement;
import java.sql.DriverManager;

public class HiveCreateDb {
   private static String driverName = "org.apache.hadoop.hive.jdbc.HiveDriver";
   
   public static void main(String[] args) throws SQLException {
      // Register driver and create driver instance
   
      Class.forName(driverName);
      // get connection
      
      Connection con = DriverManager.getConnection("jdbc:hive://localhost:10000/default", "", "");
      Statement stmt = con.createStatement();
      
      stmt.executeQuery("CREATE DATABASE basededatos");
      System.out.println(“Base de datos creada exitosamente.”);
      
      con.close();
   }
}


# - Para compilar y ejecutar el programa:

# In[ ]:


javac HiveCreateDb.java
java HiveCreateDb


# Documentación: <https://cwiki.apache.org/confluence/display/Hive/GettingStarted>

# ## Apache Spark

# - Abrir el puerto 4040

# In[ ]:


sudo ufw allow 4040


# - Crear el fichero a analizar

# In[ ]:


vim entrada.txt


# - Entrar a la shell de spark

# In[ ]:


spark-shell


# In[ ]:


:help


# - Crear el RDD para el fichero entrada.txt

# In[ ]:


val inputfile = sc.textFile("entrada.txt")


# - Contar las palabras:

# In[ ]:


val counts = inputfile.flatMap(line => line.split(" ")).map(word => (word, 1)).reduceByKey(_+_);


# - Mostrar para tareas de debugging el RDD 

# In[ ]:


counts.toDebugString


# - Guardar en memoria

# In[ ]:


counts.cache()


# - Guardar la salida en un fichero

# In[ ]:


val outputfile = sc.textFile("salida.txt")


# - Almacenamiento no persistente de RDD

# In[ ]:


counts.unpersist()


# - Fuentes:
# - <https://docs.bitnami.com/virtual-machine/apps/hadoop/>.
# - <https://fortinux.com/linux-2-tutoriales/hadoop-installation-centos8/>.
# - <https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html>.
# - <https://spark.apache.org/docs/latest/quick-start.html>.
