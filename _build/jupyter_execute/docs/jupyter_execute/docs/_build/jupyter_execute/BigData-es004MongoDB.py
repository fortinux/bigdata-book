#!/usr/bin/env python
# coding: utf-8

# # Tutorial MongoDB

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

# ## MongoDB paso a paso

# - Adaptado del tutorial <https://docs.atlas.mongodb.com/tutorial/deploy-free-tier-cluster/>.

# - Crear una cuenta gratuita y entrar a:
#     - MongoDB Atlas: https://account.mongodb.com/account/login?

# - Crear una base de datos compartida gratuita:
#     - Opción Deploy a cloud database 
#     - Free shared

# - Parámetros:
#     - Región y proveedor cloud: seleccionar gratuitos (Frankfurt, Paris, Irlanda...)
#     - Cluster Tier: M0 Sandbox (Shared RAM, 512 MB Storage)
#     - MongoDB 5.0, No Backup 
#     - Nombre al cluster: Cluster0

# - Crear un/a usuaria/o para la base de datos: 
#     - Nombre de usuario: usuaria/o
#     - Clave:
# - Asignar clave al usuario *dbTestUser*

# - En la vista del Cluster0 en la página principal clicar en *Connect*
#     - Seleccionar *connection security -> Connect using MongoDB Compass* 
#     - Descargar e instalar *MongoDB Compass*
#     - Copiar el enlace de acceso, por ejemplo: 
#     <mongodb+srv://dbTestUser:<password>@cluster_name.h1a5h.mongodb.net/test>

# - A la Izquierda, desde el menú *Security* seleccionar *Network Access*
# - Agregar la propia IP para conectarse a la base de datos

# - OPCIONAL: 
# - Descargar e instalar la shell mongosh: 
#     <https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/>

# - Abrir *MongoDB Compass* y conectarse al cluster:
# - <mongodb+srv://dbTestUser:<password>@cluster0.h1a5h.mongodb.net/test>

# - Una vez conectada la base de datos, se utiliza la shell *MongoSH* localizada en la parte inferior de la pantalla para crear una base de datos:

# In[1]:


use gettingStarted


# - Inserir un documento en la base de datos:

# In[ ]:


db.people.insertOne({
  name: { first: 'Alan', last: 'Turing' },
  birth: new Date('Jun 23, 1912'),
  death: new Date('Jun 07, 1954'),
  contribs: [ 'Turing machine', 'Turing test', 'Turingery' ],
  views : Long(1250000)
})


# - Verificar si está todo correcto:

# In[ ]:


db.people.find({ "name.last": "Turing" })


# ## Consultar documentos

# - Adaptado del tutorial <https://docs.mongodb.com/manual/tutorial/query-documents/>

# - Crear una nueva base de datos llamada "inventario":

# In[ ]:


use inventario


# - Ingresar datos en la base de datos:

# In[ ]:


db.inventario.insertMany([
   { item: "journal", qty: 25, size: { h: 14, w: 21, uom: "cm" }, status: "A" },
   { item: "notebook", qty: 50, size: { h: 8.5, w: 11, uom: "in" }, status: "A" },
   { item: "paper", qty: 100, size: { h: 8.5, w: 11, uom: "in" }, status: "D" },
   { item: "planner", qty: 75, size: { h: 22.85, w: 30, uom: "cm" }, status: "D" },
   { item: "postcard", qty: 45, size: { h: 10, w: 15.25, uom: "cm" }, status: "A" }
]);


# - Seleccionar todos los documentos en "inventario":

# In[ ]:


db.inventario.find( {} )


# - Esta orden es similar a la utilizada en SQL: `SELECT * FROM inventario`

# - Seleccionar todos los documentos donde la clave "status" es igual a "D":

# In[ ]:


db.inventario.find( { status: "D" } )


# In[ ]:


SELECT * FROM inventario WHERE status = "D"


# - Mostrar todos los documents de "inventario" donde "status" es igual a "A" o "D":

# In[ ]:


db.inventario.find( { status: { $in: [ "A", "D" ] } } )


# In[ ]:


SELECT * FROM inventario WHERE status in ("A", "D")


# - Recuperar todos los documentos de "inventario" donde "status" es igual a "A" y "qty" es menor que ($lt) 30:

# In[ ]:


db.inventario.find( { status: "A", qty: { $lt: 30 } } )


# In[ ]:


SELECT * FROM inventario WHERE status = "A" AND qty < 30


# - Recuperar todos los documentos de "inventario" donde "status" es igual a "A" o "qty" es menor que ($lt) 30:

# In[ ]:


db.inventario.find( { $or: [ { status: "A" }, { qty: { $lt: 30 } } ] } )


# In[ ]:


SELECT * FROM inventario WHERE status = "A" OR qty < 30


# - Recuperar todos los documentos de "inventario" donde "status" es igual a "A" y/o "qty" es menor que ($lt) 30, o item comienza con la letra p:

# In[ ]:


db.inventario.find( {
     status: "A",
     $or: [ { qty: { $lt: 30 } }, { item: /^p/ } ]
} )


# In[ ]:


SELECT * FROM inventario WHERE status = "A" AND ( qty < 30 OR item LIKE "p%")

