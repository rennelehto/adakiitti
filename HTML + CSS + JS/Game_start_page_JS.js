'use strict'
let name = document.getElementById("Name")


let button1 = document.querySelector("#startbutton")
button1.style.fontSize = "xx-large"
button1.addEventListener("click", (event) =>{
  let playerName = name.value
  localStorage.setItem("name", playerName);
  location.href="Main_page.html"

})

let button2 = document.querySelector("#hsbutton")
button2.style.fontSize = "xx-large"
button2.addEventListener("click", (event) =>{
  location.href="highscore.html"
})



