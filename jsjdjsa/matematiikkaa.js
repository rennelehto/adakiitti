function toRadian(degree){
  return degree*Math.PI/180
}

function getDistance(originLat, originLon, destinationLat, destinationLon){
  let lon1 = toRadian(originLon)
  let lat1 = toRadian(originLat)
  let lon2 = toRadian(destinationLon)
  let lat2 = toRadian(destinationLat)
  let deltaLat = lat2 - lat1
  let deltaLon = lon2 - lon1
  console.log(deltaLon)
  console.log(deltaLat)
  let a = Math.pow(Math.sin(deltaLat/2), 2) + Math.cos(lat1) * Math.cos(lat2) * Math.pow(Math.sin(deltaLon/2), 2)
  let c = 2 * Math.asin(Math.sqrt(a))
  const EARTH_RADIUS = 6371
  return c * EARTH_RADIUS * 1000

let distance = getDistance(lat, long, playerLocation[3],playerLocation[4])
    if (0 < distance < stones*500)






