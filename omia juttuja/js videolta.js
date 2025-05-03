// game set up, function to set up game, game settin upping
async function gameData(){
  try {
    const response = await getData('http://127.0.0.1:5000/'); // testdata/newgame.json
    console.log(gameData);
  } catch (error) {
    console.log(error);
  }
}
gameSetup();

//

// function to fetch data from API
async function getData(url) {
    const response = await fetch(url); // testdata/newgame.json
    if (!response.ok) throw new Error('Invalid server input');
    const data = await response.json();
    console.log(data);
    return data
}



//leftpane
const leftpane = document.getElementsByClassName("leftpane");
const lefth1text = document.createTextNode(`Game stats`);
const lefth1 = document.createElement('h1');
lehth1.appendChild(lefth1text);
leftpane.appendChild(lefth1);

const ilmastopisteotsikko = document.createTextNode(`Ilmastopisteet`);
const ilmastopisteh2 = document.createElement('h2');
ilmastopisteh2.appendChild(ilmastopisteotsikko);
leftpane.appendChild(ilmastopisteh2);

const ilmastopistearvo = document.createTextNode(`${ilmastopisteet}`);
const ilmastopisteet = document.createElement('p');
ilmastopisteet.id = 'ilmasto'
ilmastopisteet.appendChild(ilmastopistearvo);
leftpane.appendChild(ilmastopisteet);

const kivipisteotsikko = document.createTextNode(`Kerättyjen kivien arvo`);
const kivipisteh2 = document.createElement('h2');
kivipisteh2.appendChild(kivipisteotsikko);
leftpane.appendChild(kivipisteh2);

const kivipistearvo = document.createTextNode(`${pisteet}`);
const kivipisteet = document.createElement('p');
kivipistearvo.id = 'kivet'
kivipisteet.appendChild(kivipistearvo);
leftpane.appendChild(kivipisteet);


//rightpane
const rightpane = document.getElementsByClassName("rightpane");
const rigth1text = document.createTextNode(`Matkustettavat kentät`);
const righth1 = document.createElement('h1');
right1.appendChild(rigth1text);
rightpane.appendChild(righth1);

const kenttälista = document.createElement('ul');
rightpane.appendChild(kenttälista)

for (i = 0; i <= kenttälista.length; i++) {
  const kentt = document.createTextNode(`${kenttälista[i]}`);
  const list = document.createElement('li');
  list.appendChild(kentt)
  kenttälista.appendChild(list)
}
rightpane.appendChild(kenttälista)

//middlepane
const middlepane = document.createElement('div');
middlepane.className = 'textbox'
const middlep = document.createElement('p');
middlep.className = 'middletext'
middlepane.appendChild(middlep)

