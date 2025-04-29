'use strict';
let button = document.querySelector('button');

var map = L.map('map', {
  center: [40, 0],
  zoom: 2,
  minZoom: 2,
  maxZoom: 8,
  zoomControl: true,
  scrollWheelZoom: true,
  doubleClickZoom: false,
  boxZoom: true,
  touchZoom: true,
  dragging: true,
  maxBounds: [
    [-85, -180],
    [85, 180],
  ],
});

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
  minZoom: 2,
  maxZoom: 8,
  noWrap: true,               // << Estää kartan looppaamista
}).addTo(map);

const markers = {};  // Antaa nimet pisteille kartalla

function add_to_map(x, y, name) {
  const marker = L.marker([x, y]).addTo(map).bindPopup(`${name}`);

  marker.on('mouseover', function(ev) {
    marker.openPopup();
  });
  marker.on('mouseout', function(ev) {
    marker.closePopup();
  });

  markers[name] = marker;  // Tallentaa pisteen
  let li = document.createElement('li');
  li.innerHTML = name;
  document.getElementById('airport_names').appendChild(li);
}

function remove_from_map(name) {
  const marker = markers[name];
  if (marker) {
    map.removeLayer(marker);
    delete markers[name];  // Poistaa pisteen

    const ul = document.getElementById('airport_names');
    const items = ul.getElementsByTagName('li');

    for (let i = 0; i < items.length; i++) {
      if (items[i].innerHTML === name) {
        ul.removeChild(items[i]);
        break;
      }
    }
  }
}

// näin lisätään kenttiä!
add_to_map(40.7128, -74.0060, 'New York JFK airport');
add_to_map(60.192059, 24.945831, 'Helsinki-Vantaa airport');
add_to_map(33.6407, -84.4277, 'Atlanta Hartsfield–Jackson Intl');
add_to_map(40.0801, 116.5846, 'Beijing Capital Intl');
add_to_map(25.2532, 55.3657, 'Dubai Intl');
add_to_map(33.9416, -118.4085, 'Los Angeles Intl');
add_to_map(35.5494, 139.7798, 'Tokyo Haneda Intl');
add_to_map(41.9742, -87.9073, "Chicago O'Hare Intl");
add_to_map(51.4700, -0.4543, 'London Heathrow');
add_to_map(22.3080, 113.9185, 'Hong Kong Intl');
add_to_map(31.1443, 121.8083, 'Shanghai Pudong Intl');
add_to_map(49.0097, 2.5479, 'Paris Charles de Gaulle');
add_to_map(52.3105, 4.7683, 'Amsterdam Schiphol');
add_to_map(50.0379, 8.5622, 'Frankfurt Intl');
add_to_map(32.8998, -97.0403, 'Dallas/Fort Worth Intl');
add_to_map(23.3924, 113.2988, 'Guangzhou Baiyun Intl');
add_to_map(1.3644, 103.9915, 'Singapore Changi');
add_to_map(37.4602, 126.4407, 'Seoul Incheon Intl');
add_to_map(39.8561, -104.6737, 'Denver Intl');
add_to_map(41.2753, 28.7519, 'Istanbul Airport');

let name_of_del = document.getElementById('test');

// näin poistetaan kysytty piste; pelkkää demoa, ei tarvita peliin, mutta tästä saa ideoita!
button.addEventListener('click', function(evt) {
  let name_to_del = name_of_del.value;
  remove_from_map(`${name_to_del}`);

});







