let playerLocation = getRandomAirports(data, 1)
console.log(playerLocation)

function add_player_to_map(x, y, name) {
  var playerIcon = L.icon({
    iconUrl: 'wizard_PNG.png',
    shadowUrl: 'wizard_PNG.png',

    iconSize: [46, 70],
    shadowSize: [60, 48],
    iconAnchor: [23, 69],
    shadowAnchor: [5, 47],
    popupAnchor: [-3, -76]
  })
  const marker = L.marker([x, y], {icon:playerIcon}).addTo(map).bindPopup(`${name}`)

  marker.on('mouseover', function(ev) {
    marker.openPopup();
  });
  marker.on('mouseout', function(ev) {
    marker.closePopup();
  });

  markers[name] = marker;  // Tallentaa pisteen
}

playerLocation.forEach((airport) => {
  const { lat, long, Name } = airport;
  if (lat && long) {
    add_player_to_map(lat, long, Name);
    all_airports[Name] = airport;
  }
});
