const button3 = document.createElement("button");
    button3.textContent = "Jää tälle kentälle";
    button3.id = "next3"
    button3.addEventListener("click", (event) =>{
      let nro = Math.floor(Math.random() * 4);
      let kuvanpaikka = document.querySelector('#map');
      let skippauskuva = document.createElement('img');
      skippauskuva.src = kuvat[nro]['kuva']
      skippauskuva.alt = kuvat[nro]['alt']
      kuvanpaikka.appendChild(skippauskuva)
      textBox.textContent = `${kuvat[nro]['alt']}`;



      let container = document.getElementById("button-container");
      container.removeChild(button2);
      container.removeChild(button3);
      let button4 = document.createElement("button");
      button4.textContent = "Continue";
      button4.id = "button4"
      container.appendChild(button4);
      button4.addEventListener("click", (event) => {
        kuvanpaikka.removeChild(skippauskuva);
        textBox.textContent = ``
        container.removeChild(button4)
        container.appendChild(button2);
        container.appendChild(button3);
      })})