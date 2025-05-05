'use strict';
let button = document.querySelector('button');
let playerLocation = null;
let stones = null

const map = L.map('map', {
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
let all_airports = {};

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

function remove_from_list(name) {
  const marker = markers[name];
  if (marker) {
    map.removeLayer(marker);
    delete markers[name];

    for (let airport of all_airports) {
        if (airport[1] == name){
          all_airports.remove(airport)
          console.log('Removed from data: ', all_airports)
        }
      };

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

function add_player_to_map(x, y, name) {
  let playerIcon = L.icon({
    iconUrl: 'https://raw.githubusercontent.com/rennelehto/adakiitti/refs/heads/A/jsjdjsa/wizard_PNG.png',
    iconSize: [46, 70],
    iconAnchor: [23, 69],
    popupAnchor: [-3, -76],
  });
  const marker = L.marker([x, y], {icon: playerIcon}).
      addTo(map).
      bindPopup(`${name}`);

  marker.on('mouseover', function(ev) {
    marker.openPopup();
  });
  marker.on('mouseout', function(ev) {
    marker.closePopup();
  });
}

function 1getRandomAirports(arr, num) {
  let randomAirports = [];
  for (let i = 0; i < num; i++) {
    const randomIndex = Math.floor(Math.random() * arr.length);
    randomAirports.push(arr[randomIndex]);
  }
  return randomAirports;
}

function toRadian(degree){
  return degree*Math.PI/180
}

function getDistance(originLat, originLon, destinationLat, destinationLon) {
  let lon1 = toRadian(originLon)
  let lat1 = toRadian(originLat)
  let lon2 = toRadian(destinationLon)
  let lat2 = toRadian(destinationLat)
  let deltaLat = lat2 - lat1
  let deltaLon = lon2 - lon1
  let a = Math.pow(Math.sin(deltaLat / 2), 2) + Math.cos(lat1) * Math.cos(lat2) * Math.pow(Math.sin(deltaLon / 2), 2)
  let c = 2 * Math.asin(Math.sqrt(a))
  const EARTH_RADIUS = 6371
  return c * EARTH_RADIUS
}
async function fetchData() {
  try {
    const response = await fetch('http://127.0.0.1:3000/airport/');
    const data = await response.json();

    all_airports = data;

    console.log('Fetched airport data:', all_airports);

    playerLocation = getRandomAirports(all_airports, 1)[0];

    const {lat, long, Name} = playerLocation;
    const p_lat = lat
    const p_long = long
    if (lat && long) {
      add_player_to_map(lat, long, Name);
      remove_from_list(Name);
    }

    const randomAirports = getRandomAirports(all_airports, 20);
    let amount = 0
    while (amount < 20) {
      for (let airport of randomAirports) {
        const {lat, long, Name} = airport;
        let distance = +getDistance(lat, long, p_lat, p_long)
        if (0 < distance < (stones * 500)) {
           if (lat && long) {
            add_to_map(lat, long, Name);
            amount += 1
            console.log(amount)
          }
        } else{
          console.log('Airport too far.')
        }
      }
    }
    return playerLocation;
  } catch (error) {
    console.error('Error fetching data', error);
  }
}

function createNewButton() {
  const container = document.getElementById('button-container');

  const button1 = document.createElement('button');
  button1.textContent = 'Continue';
  button1.id = 'next1';
  container.appendChild(button1);

}

createNewButton();

let name_of_del = document.getElementById('test');

let textBox = document.getElementById('text');

let clickCount = 0;

textBox.textContent = 'Hei Muinaiset tietäjälahkot ovat sodassa! Vanhat lahkot, joiden tavoite on ilmastonmuutos, ' +
    'ovat kaavailleet suunnitelman tuodakseen lopun konfliktille: Suur-Velho Kaik-Oo-Koolle on' +
    ' annettu tehtäväksi kerätä kaikki adakiittikivet maailmasta voittaakseen velhojen taisto. ';

document.getElementById('next1').addEventListener('click', function() {
  clickCount++;

  if (clickCount === 1) {
    textBox.textContent = 'Uudet lahkot ovat päättäneet pysäyttää heidän aikeensa lähettämällä oman valittunsa keräämään kaikki kivet ensin.' +
        ' Toteuttaakseen tämän tehtävän, uudet lahkot valitsivat: sinut!';
  } else if (clickCount === 2) {
    textBox.textContent = 'Nyt, sinun kuuluu kerätä niin paljon adakiittitaikakiviä kuin voit, käyttämällä maailman lentokenttiä kiintopisteinä ja ' +
        'pysäyttää Kaik-Oo-Koo ennen kuin hän ehtii tuhota ilmaston!';
  } else if (clickCount === 3) {
    stones = 5
    fetchData().then((location) => {
      if (location) {
        playerLocation = location;
        textBox.textContent = 'Olet saapunut kentälle: ' + location.Name;
      } else {
        textBox.textContent = 'Kenttää ei voitu ladata.';
      }

      createNewButtons();
    });
  }

  function createNewButtons() {
    const container = document.getElementById('button-container');
    const button1 = document.getElementById('next1');
    const button2 = document.createElement('button');
    button2.textContent = 'Matkusta kentälle';
    button2.id = 'next2';
    button2.addEventListener('click', function() {
      gameLoop(2);
    });

    const button3 = document.createElement('button');
    button3.textContent = 'Jää tälle kentälle';
    button3.id = 'next3';
    button3.addEventListener('click', function() {
      gameLoop(3);
    });

    container.removeChild(button1);
    container.appendChild(button2);
    container.appendChild(button3);

  }
});

let score = 30;

function gameLoop(button) {
  const button2 = document.getElementById('next2');
  const button3 = document.getElementById('next3');
  const enviroment = document.getElementById('ilm_pist')



  if (button === 2) {
    score = score -= 2;
    enviroment.textContent = score;

  } else if (button === 3) {
    button3.addEventListener('click', function() {

    });
  }
}

function schmooving(){

  const {lat, long, Name} = playerLocation;
  remove_from_map(Name)
  playerLocation = getRandomAirports(all_airports, 1)[0];

  const {lat, long, Name} = playerLocation;
  const p_lat = lat
  const p_long = long
  if (lat && long) {
    add_player_to_map(lat, long, Name);
    remove_from_list(Name);
  }
  const randomAirports = getRandomAirports(all_airports, 20);
  let amount = 0
  while (amount < 20) {
    for (let airport of randomAirports) {
      const {lat, long, Name} = airport;
      remove_from_map(Name)
      let distance = +getDistance(lat, long, p_lat, p_long)
      if (0 < distance < (stones * 500)) {
         if (lat && long) {
          add_to_map(lat, long, Name);
          amount += 1
          console.log(amount)
        }
      } else{
        console.log('Airport too far.')
      }
    }
  }
}





