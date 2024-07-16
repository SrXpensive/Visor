import requests
PROVINCIA = 'VALENCIA'
# URL del endpoint
url = 'http://ovc.catastro.meh.es/OVCServWeb/OVCWcfCallejero/COVCCallejero.svc/json/ObtenerMunicipios?Provincia=VALENCIA' #ObtenerProvincias

# Petición GET
response = requests.get(url)

if response.status_code == 200:
    try:
        data = response.json()
        for d in data['consulta_municipieroResult']['municipiero']['muni']:
            print(d['nm'])
    except ValueError:
        print("Error al procesar JSON")
else:
    print(f"Error en la petición: {response.status_code}")
