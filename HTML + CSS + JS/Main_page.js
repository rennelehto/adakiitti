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
let all_airports = {

}
function getRandomAirports(arr, num) {
  let randomAirports = [];
  for (let i = 0; i < num; i++) {
    const randomIndex = Math.floor(Math.random() * arr.length);  // Random index from 0 to arr.length-1
    randomAirports.push(arr[randomIndex]);
  }
  return randomAirports;
}
async function fetchData () {
  try {
    const response = await fetch('http://127.0.0.1:3000/airport/');
    const data = await response.json();

    console.log("Fetched airport data:", data);

    all_airports = data;
    const randomAirports = getRandomAirports(data, 20);

randomAirports.forEach((airport) => {
  const { lat, long, Name } = airport;
  if (lat && long) {
    add_to_map(lat, long, Name);
    all_airports[Name] = airport;
  }
});

    } catch (error) {
    console.error("Error fetching data", error);
  }
}
fetchData()



let name_of_del = document.getElementById('test');

// näin poistetaan kysytty piste; pelkkää demoa, ei tarvita peliin, mutta tästä saa ideoita!
button.addEventListener('click', function(evt) {
  let name_to_del = name_of_del.value;
  remove_from_map(`${name_to_del}`);

});







