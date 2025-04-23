'use strict'

let button = document.querySelector("button")
button.style.fontSize = "xx-large"
let h1 = document.getElementById("h1")
button.addEventListener("click", function(evt){
  h1.textContent = "Nope"
  location.href="Main_page.html"
})
button.addEventListener("mouseleave",function(evt){
  h1.textContent = "ADAKITE"
})