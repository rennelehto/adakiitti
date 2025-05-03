'use strict';


const dflex = document.querySelector('.d-flex');
const ilmastopisteet1 = 0;
const pisteet1 = 0;

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
	alt: 'Puhtaan juomaveden saanti pitää yhteisön terveenä'
},
{
	kuva: 'https://users.metropolia.fi/~rennel/kuvia_peliin/propaganda4.jpg',
	alt: 'Omavarainen yhteisö pitää pintansa myös vaikeampina aikoina.'
}
]

//leftpane
const leftpane = document.createElement("div");
leftpane.className ='leftpane';
const lefth1text = document.createTextNode(`Game stats`);
const lefth1 = document.createElement('h1');
lefth1.appendChild(lefth1text);
leftpane.appendChild(lefth1);
dflex.appendChild(leftpane);

const ilmastopisteotsikko = document.createTextNode(`Ilmastopisteet`);
const ilmastopisteh2 = document.createElement('h2');
ilmastopisteh2.appendChild(ilmastopisteotsikko);
leftpane.appendChild(ilmastopisteh2);

const ilmastopistearvo = document.createTextNode(`${ilmastopisteet1}`);
const ilmastopisteet = document.createElement('p');
ilmastopisteet.id = 'ilmasto';
ilmastopisteet.appendChild(ilmastopistearvo);
leftpane.appendChild(ilmastopisteet);

const kivipisteotsikko = document.createTextNode(`Kerättyjen kivien arvo`);
const kivipisteh2 = document.createElement('h2');
kivipisteh2.appendChild(kivipisteotsikko);
leftpane.appendChild(kivipisteh2);

const kivipistearvo = document.createTextNode(`${pisteet1}`);
const kivipisteet = document.createElement('p');
kivipistearvo.id = 'kivet';
kivipisteet.appendChild(kivipistearvo);
leftpane.appendChild(kivipisteet);

dflex.appendChild(leftpane);


//middlepane
const middlepane = document.createElement('div');
middlepane.className = 'middlepane';

const mapp = document.createElement('div');
mapp.id = 'map';

const middletext = document.createElement('div');
middletext.className = 'textbox';
const middlep = document.createElement('p');
middlep.id = 'text';
middletext.appendChild(middlep);
middlepane.appendChild(mapp);
middlepane.appendChild(middletext);

dflex.appendChild(middlepane);
//rightpane
const rightpane = document.createElement("div");
rightpane.className ='rightpane';

const rigth1text = document.createTextNode(`Matkustettavat kentät`);
const righth1 = document.createElement('h1');
righth1.appendChild(rigth1text);
rightpane.appendChild(righth1);

const kenttälista = document.createElement('ul');
rightpane.appendChild(kenttälista);

//for (i = 0; i <= kenttälista.length; i++) {
  //const kentt = document.createTextNode(`${kenttälista[i]}`);
  //const list = document.createElement('li');
  //list.appendChild(kentt);
  //kenttälista.appendChild(list);
//}
rightpane.appendChild(kenttälista);
dflex.appendChild(rightpane);


async function skippaavuoro(){
	const nro = Math.floor(Math.random() * 4);
	const skippauskuva = document.createElement('img');
	skippauskuva.src = kuvat[nro]['kuva']
	skippauskuva.alt = kuvat[nro]['alt']
	mapp.appendChild(skippauskuva)
  const skippausteksti = document.createTextNode(`${kuvat[nro]['alt']}`);
  middlep.appendChild(skippausteksti)
}

skippaavuoro();


