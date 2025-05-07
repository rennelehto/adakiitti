const score = parseInt(localStorage.getItem("score")) || 0;
const evilScore = parseInt(localStorage.getItem("evilScore")) || 0;
const ilmasto = parseInt(localStorage.getItem("environmentalPoints")) || 0;

let pelaajanKivet = score + ilmasto
let vastustajanKivet = evilScore

let pelaajanPisteet = 0;
let vastustajanPisteet = 0;

let pelaajanJaljellaHeitot = pelaajanKivet;
let vastustajanJaljellaHeitot = vastustajanKivet;

const fightButton = document.getElementById("fightbutton");
const rollResultsElement = document.getElementById("roll-results");
const pelaajanPisteetElement = document.getElementById("pelaajan-pisteet");
const vastustajanPisteetElement = document.getElementById("vastustajan-pisteet");
const pelaajanKivetElement = document.getElementById("pelaajan-kivet");
const vastustajanKivetElement = document.getElementById("vastustajan-kivet");

pelaajanKivetElement.innerText = pelaajanKivet;
vastustajanKivetElement.innerText = vastustajanKivet;
pelaajanPisteetElement.innerText = pelaajanPisteet;
vastustajanPisteetElement.innerText = vastustajanPisteet;


fightButton.addEventListener("click", () => {
    let heittotulosHTML = "";

if (pelaajanJaljellaHeitot > 0) {
    const heittojenMaara = Math.min(10, pelaajanJaljellaHeitot);
    let heittojenSumma = 0;
    heittotulosHTML = "";

    for (let i = 0; i < heittojenMaara; i++) {
        const heitto = Math.floor(Math.random() * 6) + 1;
        pelaajanPisteet += heitto;
        pelaajanJaljellaHeitot--;
        heittojenSumma += heitto;
    }

    heittotulosHTML = `<p>Pisteesi = ${heittojenSumma}</p>`;
    rollResultsElement.innerHTML = heittotulosHTML;
}

if (vastustajanJaljellaHeitot > 0) {
    const heittojenMaara = Math.min(10, vastustajanJaljellaHeitot);
    let heittojenSumma = 0;

    for (let i = 0; i < heittojenMaara; i++) {
        const heitto = Math.floor(Math.random() * 6) + 1;
        vastustajanPisteet += heitto;
        vastustajanJaljellaHeitot--;
        heittojenSumma += heitto;
    }

    heittotulosHTML += `<p>Vastustajan pisteet = ${heittojenSumma}</p>`;
    rollResultsElement.innerHTML = heittotulosHTML;
}

    pelaajanPisteetElement.innerText = pelaajanPisteet;
    vastustajanPisteetElement.innerText = vastustajanPisteet;
    pelaajanKivetElement.innerText = pelaajanKivet;
    vastustajanKivetElement.innerText = vastustajanKivet;

    if (pelaajanJaljellaHeitot <= 0 && vastustajanJaljellaHeitot <= 0) {
        fightButton.disabled = true;
        naytaLopputulos();
    }
});

function naytaLopputulos() {
    let lopputeksti = `<h3>Lopputulos:</h3>
        <p>Pisteesi: ${pelaajanPisteet}</p>
        <p>Vastustajan pisteet: ${vastustajanPisteet}</p>`;

    if (pelaajanPisteet > vastustajanPisteet) {
        lopputeksti += `<p><strong>Voitit pelin!</strong></p>`;
    } else if (pelaajanPisteet < vastustajanPisteet) {
        lopputeksti += `<p><strong>Hävisit pelin.</strong></p>`;
    } else {
        lopputeksti += `<p><strong>Tasapeli!!</strong></p>`;
    }

    rollResultsElement.innerHTML = lopputeksti;
}