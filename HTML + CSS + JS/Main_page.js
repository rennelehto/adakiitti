'use strict'

let textcontent = document.getElementById("text")
let textbox = document.getElementById("input")

textbox.addEventListener("submit", function(evt){
  textcontent.textContent = "Here's something new! Yay :)"
})
