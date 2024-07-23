// Creamos la variable que utilizaremos como mapa
var map = L.map('map').setView([40.416775,-3.703790],6);

// Definimos capa base del mapa
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',transparent:true}).addTo(map);

// Definimos capa de catastro
L.tileLayer.wms('https://ovc.catastro.meh.es/cartografia/INSPIRE/spadgcwms.aspx?getmap', {
    layers: 'CP.CadastralParcel',
    format: 'image/png',
    transparent: true,
    attribution: 'Catastro'
}).addTo(map);
