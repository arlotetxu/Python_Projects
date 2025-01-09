"""
Proyecto: Gestor de Tareas en la Nube

Funcionalidades:
	1.	Crear tareas:
	   •	Cada tarea tendrá un título, descripción, prioridad y estado (pendiente o completada).
	2.	Listar tareas:
	   •	Mostrar todas las tareas con opción de filtrar por estado o prioridad.
	3.	Actualizar tareas:
	   •	Modificar el estado o los detalles de una tarea.
	4.	Eliminar tareas:
	   •	Permitir eliminar una tarea específica.


Firebase es una plataforma desarrollada por Google que proporciona herramientas para construir y administrar aplicaciones web y móviles. Los servicios que ofrece incluyen bases de datos, autenticación, almacenamiento, hosting, funciones en la nube y más. Firebase es particularmente útil para proyectos que requieren un backend escalable con mínima configuración.

Conceptos básicos de Firebase:
	1.	Realtime Database:
	•	Base de datos NoSQL que almacena y sincroniza datos en tiempo real entre los usuarios.
	•	Ideal para aplicaciones en las que múltiples usuarios colaboran o ven actualizaciones simultáneas.
	2.	Firestore (Base de datos preferida):
	•	Una base de datos flexible, escalable y orientada a documentos.
	•	Similar a MongoDB, trabaja con colecciones y documentos.
	•	Ofrece consultas avanzadas y soporte para datos offline.
	3.	Autenticación:
	•	Gestiona fácilmente los métodos de inicio de sesión, como Google, Facebook, correo electrónico y más.
	4.	Almacenamiento:
	•	Permite guardar archivos como imágenes, videos o documentos.
	5.	Hosting:
	•	Servicio para alojar aplicaciones web y contenido estático de forma gratuita con HTTPS.
	6.	Funciones en la nube:
	•	Permite ejecutar lógica del backend en entornos serverless.

Documentación y ayuda:
	•	Documentación oficial de Firebase para Python:
	       Firebase Admin SDK Python: https://firebase.google.com/docs/admin/setup?hl=es
	•	Tutoriales y guías:
            https://firebase.google.com/docs/firestore?hl=es-419&authuser=1

	web DB: https://console.firebase.google.com/u/1/project/lista-tareas-fef11/firestore/databases/-default-/data?hl=es-419

	coleccion: 'lista_tareas_col'
"""

from firebase_config import get_collection # Gestiona la conexion a la base de datos
from db_crud import add_task
from utils import get_field_values



if  __name__ == '__main__':
    collection = get_collection() # Campo a pasar como argumento a las funciones para operaciones CRUD
    docs = collection.stream()

    """data = {"name": "New York", "state": "NY", "country": "USA"}
    collection.document('NY').set(data)

    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")"""

    add_task(collection)
