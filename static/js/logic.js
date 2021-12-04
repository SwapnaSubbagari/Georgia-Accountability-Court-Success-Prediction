// Creating the map object
const myMap = L.map('map', {
  // center: [19.41577, -154.96278],
  center: [37.757815, -122.5076401],
  zoom: 10,
});

// Adding the tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(myMap);

// Store the API query variables.
// For docs, refer to https://dev.socrata.com/docs/queries/where.html.
// And, refer to https://dev.socrata.com/foundry/data.cityofnewyork.us/erm2-nwe9.
const baseURL = 'https://data.cityofnewyork.us/resource/fhrw-4uyv.json?';
const date = "$where=created_date between'2016-01-01T00:00:00' and '2017-01-01T00:00:00'";
const complaint = '&complaint_type=Rodent';
const limit = '&$limit=10000';

// Assemble the API query URL.
let url = baseURL + date + complaint + limit;
url = '/query';
// Get the data with d3.
let res;
d3.json(url).then((response) => {
  if (1) {
    response = response.data;

    response = response.map((d) => {
      d.latitude += '';
      d.longitude += '';

      return d;
    });
    res = response;
  }

  console.log(response);

  // Create a new marker cluster group.
  const markers = L.markerClusterGroup();

  const heatArray = [];
  // Loop through the data.
  for (let i = 0; i < response.length; i++) {
    // Set the data location property to a variable.
    const location = [response[i].latitude, response[i].longitude];

    heatArray.push([location[0], location[1], response[i].price]);

    // Add a new marker to the cluster group, and bind a popup.
    markers.addLayer(L.marker([location[0], location[1]])
      .bindPopup(`${response[i].host_name}<br/>$${response[i].price}`));
  }

  const heat = L.heatLayer(heatArray, {
    radius: 20,
    blur: 35,
  }).addTo(myMap);
  myMap.addLayer(markers);
});
