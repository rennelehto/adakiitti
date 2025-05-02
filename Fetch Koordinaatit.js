async function fetchLocation(){
  let results = []
  const response = await fetch()
  const data = response.json
  for (i of data){
    if (i.ICAO == ""){
      results.push(i.lat)
      results.push(i.long)
      results.push(i.Location)
    }
  } return results
}