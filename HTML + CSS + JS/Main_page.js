'use strict'
let button = document.querySelector("button")

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

const markers = {};  // Antaa nimet pisteille kartalla

function add_to_map(x, y, name) {
    const marker = L.marker([x, y])
        .addTo(map)
        .bindPopup(`${name}`);

    marker.on('mouseover', function(ev) {
        marker.openPopup();
    });
    marker.on('mouseout', function(ev) {
        marker.closePopup();
    });

    markers[name] = marker;  // Tallentaa pisteen
}

function remove_from_map(name) {
    const marker = markers[name];
    if (marker) {
        map.removeLayer(marker);
        delete markers[name];  // Poistaa pisteen
    }
}

// näin lisätään kenttiä!
add_to_map(40.7128, -74.0060,"New York JFK airport")
add_to_map(60.192059, 24.945831,"Helsinki-Vantaa airport")


let name_of_del = document.getElementById("test")


// näin poistetaan kysytty piste; pelkkää demoa, ei tarvita peliin, mutta tästä saa ideoita!
button.addEventListener("click", function(evt){
    let name_to_del = name_of_del.value
  remove_from_map(`${name_to_del}`)
})





