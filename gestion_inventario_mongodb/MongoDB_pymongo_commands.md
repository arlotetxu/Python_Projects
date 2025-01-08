# Guía Básica para Trabajar con MongoDB en Python (pymongo)

## 1. Instalación de `pymongo`
Primero, necesitas instalar la biblioteca `pymongo` si aún no lo has hecho. Abre una terminal y ejecuta:
`pip install pymongo`

## 2. Realizar la Conexión a MongoDB
Para conectarte a una base de datos en MongoDB, utiliza el siguiente código:
`import pymongo`

Establecer la conexión con el servidor de MongoDB:
`cliente = pymongo.MongoClient(“mongodb://localhost:27017/”)  # Conexión local`

Si usas MongoDB Atlas o una conexión remota, reemplaza la URL de arriba por la de tu clúster
Ejemplo:
`cliente = pymongo.MongoClient(“mongodb+srv://usuario:contraseña@cluster.mongodb.net/”)`
Seleccionar la base de datos que vas a usar (si no existe, se crea automáticamente)
`db = cliente[“nombre_de_tu_base_de_datos”]`

Seleccionar una colección dentro de la base de datos (equivalente a una tabla en SQL)
`coleccion = db[“nombre_de_tu_coleccion”]`

## 3. Operaciones CRUD

#### **C - Crear (Insertar Documentos)**
Para insertar documentos (registros) en la colección, usa los siguientes métodos:

- `insert_one()`: Para insertar un solo documento.
- `insert_many()`: Para insertar múltiples documentos.

#### **R - Leer (Consultar Documentos)**
Para leer (consultar) documentos en la colección:

- `find()`: Para obtener todos los documentos.
- `find_one()`: Para obtener un solo documento.
- Puedes filtrar los resultados con condiciones, por ejemplo, `coleccion.find({"edad": 30})` para obtener documentos donde la edad sea 30.

#### **U - Actualizar Documentos**
Para actualizar documentos en la colección:

- `update_one()`: Para actualizar un solo documento.
- `update_many()`: Para actualizar múltiples documentos.
- Ejemplo: Para cambiar la edad de una persona, puedes usar `coleccion.update_one({"nombre": "Juan"}, {"$set": {"edad": 31}})`.

#### **D - Eliminar Documentos**
Para eliminar documentos de la colección:

- `delete_one()`: Para eliminar un solo documento.
- `delete_many()`: Para eliminar múltiples documentos.
- Ejemplo: Para eliminar todos los documentos con edad menor a 30, puedes usar `coleccion.delete_many({"edad": {"$lt": 30}})`.


## 4. Cerrar la Conexión
Una vez que hayas terminado de trabajar con la base de datos, puedes cerrar la conexión utilizando:
`cliente.close()`
---

**Resumen de Operaciones CRUD en MongoDB:**

- **C - Crear**: `insert_one()`, `insert_many()`
- **R - Leer**: `find()`, `find_one()`
- **U - Actualizar**: `update_one()`, `update_many()`
- **D - Eliminar**: `delete_one()`, `delete_many()`

Este conjunto de operaciones te permitirá realizar la mayoría de las acciones necesarias para trabajar con MongoDB desde Python.
