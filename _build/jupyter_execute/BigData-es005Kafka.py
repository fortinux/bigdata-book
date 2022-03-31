#!/usr/bin/env python
# coding: utf-8

# # Tutorial Apache Kafka

# - Apache Kafka es una plataforma de transmisión de eventos distribuidos de código abierto utilizada por miles de empresas para canalizaciones de datos de alto rendimiento, análisis de streaming, integración de datos y aplicaciones de misión crítica.
# - Es un sistema de mensajería escalable que permite a los usuarios publicar y consumir grandes cantidades de mensajes en tiempo real por suscripción.
#     - Extraído de: <https://kafka.apache.org/>. 

# ## Configuración inicial

# - La máquina virtual con Hadoop instalado se descarga de:
# - <https://bitnami.com/stack/kafka>.
# - Se puede acceder a la información sobre la configuración predeterminada de la máquina virtual de Bitnami en:
# - <https://docs.bitnami.com/general/infrastructure/kafka/get-started/understand-default-config/>.

# - Una vez instalado Apache Kafka se deberán abrir los puertos del servidor para los distintos servicios del framework.
# - Puerto 9092 para Kafka y puerto 2181 para Zookeeper.

# In[1]:


sudo ufw allow 9092


# In[ ]:


sudo ufw allow 2081


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


# # Ejecutar un productor y un consumidor en Kafka

# - Crear y colectar un tópico en Kafka utilizando la consola.
# - Se inicia exportando la configuración de autenticación a Kafka.

# In[ ]:


export KAFKA_OPTS="-Djava.security.auth.login.config=/opt/bitnami/kafka/config/kafka_jaas.conf"


# - Crear un nuevo tópico con una única partición y una única réplica.

# In[ ]:


opt(/bitnami/kafka/bin/kafka-topics.sh, --create, --zookeeper, \)
SERVER-IP:2181 --replication-factor 1 --partitions 1 --topic test


# - Crear un nuevo productor y generar el mensaje para el tópico.

# In[ ]:


opt(/bitnami/kafka/bin/kafka-console-producer.sh, --broker-list, SERVER-IP:9092, --producer.config, /opt/bitnami/kafka/config/producer.properties, --topic, test)


# In[ ]:


Este es mi primer mensaje
y este es el segundo


# - Recuperar y presentar los mensajes.

# In[ ]:


opt(/bitnami/kafka/bin/kafka-console-consumer.sh, --bootstrap-server, localhost:9092, --topic, test, --consumer.config, /opt/bitnami/kafka/config/consumer.properties, --from-beginning)


# - Fuentes:
# - <https://docs.bitnami.com/virtual-machine/apps/kafka/>.
# - <https://docs.bitnami.com/general/infrastructure/kafka/administration/run-producer-consumer/>.
