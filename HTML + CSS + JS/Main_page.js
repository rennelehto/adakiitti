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
    const randomIndex = Math.floor(Math.random() * arr.length);  
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

function createNewButton() {
    const container = document.getElementById("button-container");

    const button1 = document.createElement("button");
    button1.textContent = "Continue";
    button1.id = "next1"
    container.appendChild(button1);

}
createNewButton()

let name_of_del = document.getElementById('test');

let textBox = document.getElementById("text")

let clickCount = 0;

textBox.textContent = "Hei Muinaiset tietäjälahkot ovat sodassa! Vanhat lahkot, joiden tavoite on ilmastonmuutos, " +
    "ovat kaavailleet suunnitelman tuodakseen lopun konfliktille: Suur-Velho Kaik-Oo-Koolle on" +
    " annettu tehtäväksi kerätä kaikki adakiittikivet maailmasta voittaakseen velhojen taisto. "

document.getElementById("next1").addEventListener("click", function() {
    clickCount++;


    if (clickCount === 1) {
        textBox.textContent = "Uudet lahkot ovat päättäneet pysäyttää heidän aikeensa lähettämällä oman valittunsa keräämään kaikki kivet ensin." +
      " Toteuttaakseen tämän tehtävän, uudet lahkot valitsivat: sinut!";
    } else if (clickCount === 2) {
        textBox.textContent = "Nyt, sinun kuuluu kerätä niin paljon adakiittitaikakiviä kuin voit, käyttämällä maailman lentokenttiä kiintopisteinä ja " +
      "pysäyttää Kaik-Oo-Koo ennen kuin hän ehtii tuhota ilmaston!";
    } else if (clickCount === 3) {
        textBox.textContent = ""
        createNewButtons();
    }

function createNewButtons() {
    const container = document.getElementById("button-container");

    const button2 = document.createElement("button");
    button2.textContent = "Matkusta kentälle";
    button2.id = "next"
    button2.addEventListener("click", function() {

    });

    const button3 = document.createElement("button");
    button3.textContent = "Jää tälle kentälle";
    button3.id = "next3"
    button3.addEventListener("click", function() {

    });
    container.appendChild(button2);
    container.appendChild(button3);
}})











