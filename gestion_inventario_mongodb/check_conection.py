from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import certifi

# Reemplaza '<URI_DE_CONEXION>' con tu URI proporcionado por MongoDB Atlas
MONGO_URI = "mongodb+srv://arlotetxu:jMb3v2aU4W3MNja@arlo-cluster.cy15o.mongodb.net/?retryWrites=true&w=majority&appName=arlo-cluster"

def test_connection(uri):
    try:
        # Usar certifi para los certificados
        # Crea el cliente de MongoDB
        client = MongoClient(
            uri,
            tlsCAFile=certifi.where()
        )

        # Envía un ping para verificar la conexión
        client.admin.command('ping')
        print("Conexión exitosa")

        # Opcional: lista las bases de datos disponibles
        print("Bases de datos disponibles:", client.list_database_names())
        return client
    except ConnectionFailure as e:
        print("Error de conexión:", e)
        return None

# Llama a la función para probar la conexión
test_connection(MONGO_URI)
