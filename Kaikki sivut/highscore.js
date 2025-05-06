'use strict';

let highscores = {};

async function fetchHighscoreData() {
  try {
    const response = await fetch('http://127.0.0.1:3000/highscore/');
    const data = await response.json();

    console.log('Fetched highscore data:', data);
    highscores = data;
    for(let i = 0; i <= highscores.length; i++){
    let nimipaikka = document.createElement("li");
    let nimi = document.createTextNode(`${highscores[i].Nimi}`);
    nimipaikka.appendChild(nimi)
    nimilista.appendChild(nimipaikka)

    let pistepaikka = document.createElement("li");
    let piste = document.createTextNode(`${highscores[i].Pisteet}`);
    pistepaikka.appendChild(piste)
    pistelista.appendChild(pistepaikka)
}

  } catch (error) {
    console.error('Error fetching data', error);
  }
}

fetchHighscoreData();


//sivun elementit
const body = document.querySelector('body');

const taulukko = document.createElement("div");
taulukko.id = 'taulukko';
const listat = document.createElement("div");
listat.id = 'listat';

const nimilista = document.createElement("ul");
nimilista.id = 'nimilista';

const pistelista = document.createElement("ul");
pistelista.id = 'pistelista';
taulukko.classname = 'taulukko';
const otsikko = document.createElement("h1");
otsikko.id = 'pisteotsikko';
const otsikkoteksti = document.createTextNode(`Huippupisteet`);
otsikko.appendChild(otsikkoteksti);
listat.appendChild(nimilista);
listat.appendChild(pistelista);
let nappi = document.createElement("button");
nappi.id = 'nappi';
const nappiteksti = document.createTextNode(`Etusivulle`);
nappi.addEventListener("click", (event)=> {
  location.href = "Game_start_page.html";
})
nappi.appendChild(nappiteksti);
taulukko.appendChild(otsikko);
taulukko.appendChild(listat);
taulukko.appendChild(nappi);
body.appendChild(taulukko);






