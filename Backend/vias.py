import requests
from pymongo import MongoClient

PROVINCIA = 'VALENCIA'
MUNICIPIO = 'TAVERNES DE LA VALLDIGNA'
# URL del endpoint
url = F'http://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerCallejero?Provincia={PROVINCIA}&Municipio={MUNICIPIO}' #ObtenerProvincias


# URL de la base de datos
MONGO = 'mongodb://root:root@localhost'

# Petición GET
response = requests.get(url)

# Objeto cliente con el que trabajar en la base de datos
cliente = MongoClient(MONGO)

# Lista de bases de datos existentes en el cliente mongo
lista_de_bases = cliente.list_database_names()

# Base de datos 'visor'
db = cliente['visor']

# Lista de colecciones
lista_de_colecciones = db.list_collection_names()

# Colección 'vias de tavernes'
collection = db['vias']

# Comprobar que la respuesta de la petición es exitosa mediante el código de respuesta
if response.status_code == 200:
    try:
        # Recogemos la respuesta y la parseamos en formato JSON
        data = response.json()
        # Este contador se utilizará para asignar claves únicas personalizadas
        cont = 1
        
        # Recorrermos el json devuelto y guardar los datos que queremos
        for d in data['consulta_callejeroResult']['callejero']['calle']:
            # Vamos a usar el código de cada calle como clave, el problema que tenemos es que lo recibimos como string desde el JSON, así que vamos a declararlo como entero antes de realizar la inserción/actualización
            clave = int(d['dir']['cv'])
            collection.update_one({'_id':clave},{'$set':{'tipo de via':d['dir']['tv'],'nombre':d['dir']['nv']}}, upsert= True)
    except ValueError:
        print("Error al procesar JSON")
else:
    print(f"Error en la petición: {response.status_code}")
