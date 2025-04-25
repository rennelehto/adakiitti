'use strict'

var map = L.map('map', {
    center: [30, 0],        // näyttää koko kartan(melkeen)
    zoom: 2,
    minZoom: 2,
    maxZoom: 2,
    zoomControl: false,     // Ei voi zoomata komentoja
    scrollWheelZoom: false,
    doubleClickZoom: false,
    boxZoom: false,
    touchZoom: false,
    dragging: false          // Kartta ei liiku!
});

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 2,
    minZoom: 2,
    attribution: '&copy; OpenStreetMap contributors'
}).addTo(map);

L.marker([60.192059, 24.945831]) // Lisää pisteitä kartalle, käyetään tätä jotta saadaan kaikki pisteet kartalle!
  .addTo(map)
  .bindPopup('Helsinki-Vantaa airport')


L.marker([40.7128, -74.0060]) //
  .addTo(map)
  .bindPopup('New York JFK airport')


