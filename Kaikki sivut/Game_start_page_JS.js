'use strict'

let button1 = document.querySelector("#startbutton")
button1.style.fontSize = "xx-large"
button1.addEventListener("click", (event) =>{
  location.href="Main_page.html"

})

let button2 = document.querySelector("#hsbutton")
button2.style.fontSize = "xx-large"
button2.addEventListener("click", (event) =>{
  location.href="highscore.html"
})

