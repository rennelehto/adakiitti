
let pelaajanKivet = 10;
let vastustajanKivet = 8;
let ilmastopisteet = 5;

let pelaajanPisteet = 0;
let vastustajanPisteet = 0;

let pelaajanJaljellaHeitot = pelaajanKivet + ilmastopisteet;
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
        const heitto = Math.floor(Math.random() * 6) + 1;
        pelaajanPisteet += heitto;
        pelaajanJaljellaHeitot--;
        heittotulosHTML += `<p>Pelaajan heitto: ${heitto}</p>`;
    }

    if (vastustajanJaljellaHeitot > 0) {
        const heitto = Math.floor(Math.random() * 6) + 1;
        vastustajanPisteet += heitto;
        vastustajanJaljellaHeitot--;
        heittotulosHTML += `<p>Vastustajan heitto: ${heitto}</p>`;
    }

    rollResultsElement.innerHTML = heittotulosHTML;

    pelaajanPisteetElement.innerText = pelaajanPisteet;
    vastustajanPisteetElement.innerText = vastustajanPisteet;
    pelaajanKivetElement.innerText = pelaajanKivet;
    vastustajanKivetElement.innerText = vastustajanKivet;

    if (pelaajanJaljellaHeitot === 0 && vastustajanJaljellaHeitot === 0) {
        fightButton.disabled = true;
        naytaLopputulos();
    }
});

function naytaLopputulos() {
    let lopputeksti = `<h3>Lopputulos:</h3>
        <p>Pelaajan pisteet: ${pelaajanPisteet}</p>
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