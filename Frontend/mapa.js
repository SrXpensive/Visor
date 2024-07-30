// Creamos la variable que utilizaremos como mapa
var map = L.map('map').setView([40.416775,-3.703790],6);

// Definimos capa base del mapa
var base = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',transparent:true}).addTo(map);

// Definimos capa de catastro sólo con bordes de parcelas
var parcelas = L.tileLayer.wms('https://ovc.catastro.meh.es/cartografia/INSPIRE/spadgcwms.aspx?getmap', {
    layers: 'CP.CadastralParcel',
    format: 'image/png',
    transparent: true,
    attribution: 'Catastro',
    styles: 'CP.CadastralParcel.BoundariesOnly'
}).addTo(map);
// Definimos capa de catastro con bordes y número de parcela/manzana
var parcelasNum = L.tileLayer.wms('https://ovc.catastro.meh.es/cartografia/INSPIRE/spadgcwms.aspx?getmap', {
    layers: 'CP.CadastralParcel',
    format: 'image/png',
    transparent: true,
    attribution: 'Catastro',
    styles: 'CP.CadastralParcel.ELFCadastre'
});

// Definimos capa de acequias para probar la integración con geoserver
var acequias = L.tileLayer.wms('http://localhost:8080/geoserver/prueba/wms?',{
    layers: "acequias",
    format:"image/png",
    transparent: true,
    opacity: 0.5
});

// Creamos un objeto con la capa del mapa base
var mapaBase = {
    "Base" : base
}
// Creamos un objeto con las capas de las parcelas con borde y con número
var mapaParcelas = {
    "Parcelas" : parcelas,
    "Parcelas con número" : parcelasNum,
    "Acequias": acequias
}

// Pasamos el objeto base y el objeto capas al método control, para crear un controlador de capas
L.control.layers(mapaBase,mapaParcelas).addTo(map);
