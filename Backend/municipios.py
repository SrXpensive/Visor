import requests
from pymongo import MongoClient

# URL del endpoint
url = 'http://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerMunicipios?Provincia=VALENCIA' #ObtenerProvincias

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

# Colección 'municipios'
collection = db['municipios']

# Comprobar que la respuesta de la petición es exitosa mediante el código de respuesta
if response.status_code == 200:
    try:
        # Recogemos la respuesta y la parseamos en formato JSON
        data = response.json()
        # Este contador se utilizará para asignar claves únicas personalizadas
        cont = 1
        # Usando d para iterar la respuesta recibida, actualizamos los datos de nuestra base de datos con nuestra clave, y actualizamos el valor del nombre del municipio (si es necesario)
        for d in data['consulta_municipieroResult']['municipiero']['muni']:
            collection.update_one({'_id':cont},{'$set':{'municipio':d['nm']}},upsert= True)
            cont+=1
    except ValueError:
        print("Error al procesar JSON")
else:
    print(f"Error en la petición: {response.status_code}")
