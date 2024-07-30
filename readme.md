# Proyecto Visor Tavernes de la Valldigna
### ¿Qué es?
Visor urbanístico del ayuntamiento de Tavernes de la Valldigna. El objetivo es proporcionar la información necesaria al usuario para que éste pueda generar automáticamente un informe urbanístico de carácter informativo con tan sólo clicar en la parcela deseada. Este informe no tendrá ninguna validez legal.

### ¿Cómo se ha desarrollado?
- Contamos con dos entornos virtuales diferentes: uno para el backend con **pip** de **Python** y otro para el frontend con **Node** y su gestor de paquetes **npm**.
- Ambos cuentan con las dependencias necesarias ya instaladas en el proyecto en el momento de escribir estas líneas.

#### Backend
- El objetivo es obtener datos de diferentes lugares, mediante uso de API's públicas que nos puedan proporcionar. 
- Hasta este momento el proyecto ha hecho uso de los [servicios web de la Sede Electrónica del Catastro](https://www.sedecatastro.gob.es/Accesos/SECAccDescargaDatos.aspx), para obtener datos de provincias, municipios y nombre de calles de Tavernes de la Valldigna. Los scripts con estos procesos se llaman 'provincias.py','municipios.py' y 'vias.py' respectivamente, y se encuentran en la carpeta de **backend**.
- Con los datos que se obtengan, se pretende poblar una base de datos NoSQL, para posteriormente servirlos a la hora de generar el informe.
- Para dar continuidad al proyecto, se sugiere que se haga uso de estos servicios y se implemente correctamente la información recibida.
- Finalmente se deberá automatizar el proceso de ejecución de los scripts de **Python** para mantener la base de datos actualizada en todo momento.

#### Frontend
 - Se ha hecho uso de la librería Leaflet de JavaScript para generar mapas en el navegador y gestionar las diferentes capas.
 - Hasta el momento, y haciendo uso de los [servicios web INSPIRE](https://www.catastro.hacienda.gob.es/webinspire/index.html), se ha conseguido renderizar una capa de parcelas de ámbito nacional. Esto se encuentra en el archivo 'mapa.js' dentro de la carpeta **frontend**.
 - Para ver el resultado en el navegador, sólo hay que ejecutar el archivo 'index.html' dentro de la carpeta **frontend**.
 - La capa de acequias se ha obtenido de un shapefile del Ayuntamiento, y para mostrarse se ha servido a través de GeoServer, previa importación desde una base de datos PostGres con el plugin PostGIS, a través del sofware QGIS. 

>**NOTA**: Actualmente las partes de cliente (frontend) y servidor (backend) no están conectadas, falta realizar esto y la obtención de otros datos de interés como **riesgo de inundabilidad**, **zonificación** y aquellos que resulten necesarios, según las necesidades de la institución.