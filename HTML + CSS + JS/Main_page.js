'use strict';
let button = document.querySelector('button');
let playerLocation = null;
let playerMarker = null;
let isChoosingDestination = false;
const visitedAirports = new Set();
let available_airports = {};
let all_airports = {};

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

  marker.on('click', function() {
    if (!isChoosingDestination) return;

    isChoosingDestination = false;

    const destination = {lat: x, long: y, Name: name};

    add_player_to_map(x, y, name);

    textBox.textContent = `Olet saapunut kentälle: ${name}`;

    diceRoll(1).then(() => {
      return diceRoll(2);
    }).then(() => {
      createContinueButton(() => {
        refreshAirports();
        textBox.textContent = 'Tässä seuraavat kentät joille voit matkustaa! Mitä seuraavaksi?';
        createNewButtons();
      });
    });
  });
}

function remove_from_map(name) {
  const marker = markers[name];
  if (marker) {
    map.removeLayer(marker);
    delete markers[name];

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

  if (playerMarker) {
    map.removeLayer(playerMarker);
  }

  playerMarker = L.marker([x, y], {icon: playerIcon}).
      addTo(map).
      bindPopup(`${name}`);

  playerMarker.on('mouseover', () => playerMarker.openPopup());
  playerMarker.on('mouseout', () => playerMarker.closePopup());

  playerLocation = {lat: x, long: y, Name: name};
  visitedAirports.add(name);

  remove_from_map(name);
}

function getRandomAirports(arr, num) {
  let randomAirports = [];
  for (let i = 0; i < num; i++) {
    const randomIndex = Math.floor(Math.random() * arr.length);
    randomAirports.push(arr[randomIndex]);
  }
  return randomAirports;
}


function refreshAirports() {
  for (const name in markers) {
    remove_from_map(name);
  }

  document.getElementById('airport_names').innerHTML = '';

  if (playerLocation && available_airports[playerLocation.Name]) {
    delete available_airports[playerLocation.Name];
  }

  const newAirports = getRandomAirports(Object.values(available_airports), 20);
  newAirports.forEach(({ lat, long, Name }) => {
    if (lat && long) {
      add_to_map(lat, long, Name);
    }
  });
}

async function fetchData() {
  try {
    const response = await fetch('http://127.0.0.1:3000/airport/');
    const data = await response.json();

    all_airports = data;

    available_airports = structuredClone(data);

    const randomAirports = getRandomAirports(Object.values(available_airports), 20);
    playerLocation = getRandomAirports(Object.values(available_airports), 1)[0];

    randomAirports.forEach(({ lat, long, Name }) => {
      if (lat && long) add_to_map(lat, long, Name);
    });

    const { lat, long, Name } = playerLocation;
    if (lat && long) {
      add_player_to_map(lat, long, Name);
      delete available_airports[Name];
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
        document.getElementById('next1').
            addEventListener('click', function() {
              textBox.textContent = 'Tässä kentät joihin voit matkustaa. Mitä seuraavaksi?';
              createNewButtons();
            });

      } else {
        textBox.textContent = 'Kenttää ei voitu ladata.';
      }
    });
  }
});

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
  button2.addEventListener('click', function() {
    gameLoop(2);
  });

  const button3 = document.createElement('button');
  button3.textContent = 'Jää tälle kentälle';
  button3.id = 'next3';
  button3.addEventListener('click', function() {
    gameLoop(3);
  });

  container.appendChild(button2);
  container.appendChild(button3);
}

const stones = document.getElementById('kiv_pist');
let enviromentalPoints = 30;
let score = 5;
let evilScore = 5;

function createEndButton(num) {
  const container = document.getElementById('button-container');

  const continueBtn = document.createElement('button');
  continueBtn.textContent = 'Continue';
  continueBtn.id = 'next1';
  removeButtons('next2', 'next3');
  container.appendChild(continueBtn);
  if (num === 1) {
    textBox.textContent = 'Olet löytänyt tarpeeksi Adakiittejä! Paina nappia jatkaaksesi loppu taisteluun.';
  } else if (num === 2) {
    textBox.textContent = 'Vihollinen löysi tarvitsemansa Adakiitit.. Paina nappia jatkaaksesi loppu taisteluun.';
  }
  continueBtn.addEventListener('click', () => {
    location.href =  './Game_end_page.html';
  });
}

function gameEnd(id) {
  if (id === 1) {
    createEndButton(1);
  } else if (id === 2) {
    createEndButton(2);
  }
}

function diceRoll(player) {
  return fetch('http://127.0.0.1:3000/airport/kivi').
      then(response => response.json()).
      then(data => {
        const textBox = document.getElementById('text');
        if (player === 1) {
          textBox.textContent = `${data.message} (Arvo: ${data.value})`;
          score = score + data.value;
          if (score >= 50) {
            score = 50;
            gameEnd(1);
          }
          stones.textContent = score;
        } else if (player === 2) {
          evilScore = evilScore + data.value;
          if (evilScore >= 50) {
            evilScore = 50;
            gameEnd(2);
          }
          console.log(evilScore);
        }

      });
}

function createContinueButton(callback) {
  const container = document.getElementById('button-container');

  const existing = document.getElementById('next1');
  if (existing) existing.remove();

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
    if (button === 2) {
      textBox.textContent = 'Valitse lentokenttä johon haluat matkustaa painamalla sitä kartalta.';

      enviromentalPoints -= 2;
      enviroment.textContent = enviromentalPoints;

      isChoosingDestination = true;
    }

    createContinueButton(() => {
      createNewButtons();
    });

  } else if (button === 3) {

    enviromentalPoints += 2;
    enviroment.textContent = enviromentalPoints;
    diceRoll(2)

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

const kuvat = [
  {
    kuva: 'https://users.metropolia.fi/~rennel/kuvia_peliin/propaganda1.jpg',
    alt: 'Puiden istutus on kivaa.',
  },
  {
    kuva: 'https://users.metropolia.fi/~rennel/kuvia_peliin/propaganda2.jpg',
    alt: 'Koulujen rakentaminen pitää yhteisöistä huolta pitkällä tähtäimellä.',
  },
  {
    kuva: 'https://users.metropolia.fi/~rennel/kuvia_peliin/propaganda3.jpg',
    alt: 'Puhtaan juomaveden saanti pitää yhteisön terveenä.',
  },
  {
    kuva: 'https://users.metropolia.fi/~rennel/kuvia_peliin/propaganda4.jpg',
    alt: 'Omavarainen yhteisö pitää pintansa myös vaikeampina aikoina.',
  },
];



