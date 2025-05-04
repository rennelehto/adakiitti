'use strict';
let button = document.querySelector('button');
let playerLocation = null;

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
  li.style.fontSize = 'x-large';
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

    all_airports.forEach((airport) => {
      const {lat, long, Name} = airport;
      if (lat && long) {
        all_airports[Name] = airport;
        all_airports.remove(airport);
      }
    });

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
      remove_from_list(x,y,name);
      remove_from_map(name)

  marker.on('mouseover', function(ev) {
    marker.openPopup();
  });
  marker.on('mouseout', function(ev) {
    marker.closePopup();
  });
}

function getRandomAirports(arr, num) {
  let randomAirports = [];
  for (let i = 0; i < num; i++) {
    const randomIndex = Math.floor(Math.random() * arr.length);
    randomAirports.push(arr[randomIndex]);
  }
  return randomAirports;
}

async function fetchData() {
  try {
    const response = await fetch('http://127.0.0.1:3000/airport/');
    const data = await response.json();

    console.log('Fetched airport data:', data);

    all_airports = data;
    const randomAirports = getRandomAirports(data, 20);
    playerLocation = getRandomAirports(data, 1)[0];
    console.log(playerLocation);

    randomAirports.forEach((airport) => {
      const {lat, long, Name} = airport;
      if (lat && long) {
        add_to_map(lat, long, Name);
      }
    });

    const {lat, long, Name} = playerLocation;
    if (lat && long) {
      add_player_to_map(lat, long, Name);
      all_airports[Name] = playerLocation;
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
    fetchData().then((location) => {
      if (location) {
        playerLocation = location;
        textBox.textContent = 'Olet saapunut kentälle: ' + location.Name;
      } else {
        textBox.textContent = 'Kenttää ei voitu ladata.';
      }

      createNewButtons();
    });
  }})
function removeButtons(...ids) {
  ids.forEach(id => {
    const btn = document.getElementById(id);
    if (btn) btn.remove();
  });
}


function createNewButtons() {
  const container = document.getElementById('button-container');
  container.innerHTML = '';

  const button2 = document.createElement('button');
  button2.textContent = 'Matkusta kentälle';
  button2.id = 'next2';
  button2.addEventListener('click', function () {
    gameLoop(2);
  });

  const button3 = document.createElement('button');
  button3.textContent = 'Jää tälle kentälle';
  button3.id = 'next3';
  button3.addEventListener('click', function () {
    gameLoop(3);
  });

  container.appendChild(button2);
  container.appendChild(button3);
}

const stones = document.getElementById('kiv_pist')
let enviromentalPoints = 30;
let score = 5;
let evilScore = 5

function diceRoll(player) {
  return fetch('http://127.0.0.1:3000/airport/kivi')
    .then(response => response.json())
    .then(data => {
      const textBox = document.getElementById('text');
      if (player === 1 ) {
        textBox.textContent = `${data.message} (Arvo: ${data.value})`;
      score = score + data.value
      stones.textContent = score
      } else if (player === 2) {
        evilScore = evilScore + data.value
        console.log(evilScore)
      }

    });
}

function createContinueButton(callback) {
  const container = document.getElementById('button-container');


  if (document.getElementById('next1')) return;

  const continueBtn = document.createElement('button');
  continueBtn.textContent = 'Continue';
  continueBtn.id = 'next1';

  continueBtn.addEventListener('click', () => {
    continueBtn.remove();
    textBox.textContent = 'Tässä seuraavat kentät joille voit matkustaa! Mitä seuraavaksi?';
    if (typeof callback === 'function') {
      callback();
    }
  });

  container.appendChild(continueBtn);
}

function gameLoop(button) {
  const enviroment = document.getElementById('ilm_pist');
  const kuvanpaikka = document.getElementById('map');
  const mapContainer = kuvanpaikka.parentElement;

  removeButtons('next2', 'next3');

  if (button === 2) {
    enviromentalPoints -= 2;
    enviroment.textContent = enviromentalPoints;

    diceRoll(1);
    diceRoll(2);

    createContinueButton(() => {
      createNewButtons();
    });

  } else if (button === 3) {
    enviromentalPoints += 2;
    enviroment.textContent = enviromentalPoints;

    diceRoll(2);

    const nro = Math.floor(Math.random() * kuvat.length);
    const skippauskuva = document.createElement('img');
    skippauskuva.src = kuvat[nro].kuva;
    skippauskuva.alt = kuvat[nro].alt;
    skippauskuva.style.maxWidth = '70%';
    skippauskuva.style.display = 'block';
    skippauskuva.style.margin = '0 auto';

    kuvanpaikka.classList.add('hidden');

    const mapContainer = document.getElementById('map-container');
const imageContainer = document.createElement('div');
imageContainer.id = 'image-temp';

const img = document.createElement('img');
img.src = kuvat[nro].kuva;
img.alt = kuvat[nro].alt;

imageContainer.appendChild(img);
mapContainer.appendChild(imageContainer);

    textBox.textContent = kuvat[nro].alt;

    createContinueButton(() => {
      const imageTemp = document.getElementById('image-temp');
    if (imageTemp) imageTemp.remove();

      kuvanpaikka.classList.remove('hidden');
      textBox.textContent = 'Tässä seuraavat kentät joille voit matkustaa! Mitä seuraavaksi?';
      createNewButtons();
    });
  }
}

const kuvat =[
{
	kuva: 'https://users.metropolia.fi/~rennel/kuvia_peliin/propaganda1.jpg',
	alt: 'Puiden istutus on kivaa.'
},
{
	kuva: 'https://users.metropolia.fi/~rennel/kuvia_peliin/propaganda2.jpg',
	alt: 'Koulujen rakentaminen pitää yhteisöistä huolta pitkällä tähtäimellä.'
},
{
	kuva: 'https://users.metropolia.fi/~rennel/kuvia_peliin/propaganda3.jpg',
	alt: 'Puhtaan juomaveden saanti pitää yhteisön terveenä.'
},
{
	kuva: 'https://users.metropolia.fi/~rennel/kuvia_peliin/propaganda4.jpg',
	alt: 'Omavarainen yhteisö pitää pintansa myös vaikeampina aikoina.'
}
]



