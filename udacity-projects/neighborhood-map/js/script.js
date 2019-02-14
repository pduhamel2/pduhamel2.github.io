var map;
var newInfoWindow;
var markers = [];
var restaurants = ko.observableArray([
  {
    title: 'The Red Arrow Diner', location: { lat: 42.993656, lng: -71.460901 }, phoneNumber: ' ', image: ' ', rating: ' ',
    reviewCount: ' ', address: ' ', city: ' ', state: ' ', zipcode: ' ', price: ' ', category: ' ', yelpURL: ' ', yelpAttempts: 0
  },
  {
    title: 'Hanover Street Chophouse', location: { lat: 42.990987, lng: -71.459779 }, phoneNumber: ' ', image: ' ', rating: ' ',
    reviewCount: ' ', address: ' ', city: ' ', state: ' ', zipcode: ' ', price: ' ', category: ' ', yelpURL: ' ', yelpAttempts: 0
  },
  {
    title: 'Cotton', location: { lat: 42.993610, lng: -71.467540 }, phoneNumber: ' ', image: ' ', rating: ' ',
    reviewCount: ' ', address: ' ', city: ' ', state: ' ', zipcode: ' ', price: ' ', category: ' ', yelpURL: ' ', yelpAttempts: 0
  },
  {
    title: 'The Foundry Restaurant', location: { lat: 42.986565, lng: -71.469302 }, phoneNumber: ' ', image: ' ', rating: ' ',
    reviewCount: ' ', address: ' ', city: ' ', state: ' ', zipcode: ' ', price: ' ', category: ' ', yelpURL: ' ', yelpAttempts: 0
  },
  {
    title: 'Piccola Italia Ristorante', location: { lat: 42.990157, lng: -71.462845 }, phoneNumber: ' ', image: ' ', rating: ' ',
    reviewCount: ' ', address: ' ', city: ' ', state: ' ', zipcode: ' ', price: ' ', category: ' ', yelpURL: ' ', yelpAttempts: 0
  },
  {
    title: 'Firefly American Bistro', location: { lat: 42.993098, lng: -71.462281 }, phoneNumber: ' ', image: ' ', rating: ' ',
    reviewCount: ' ', address: ' ', city: ' ', state: ' ', zipcode: ' ', price: ' ', category: ' ', yelpURL: ' ', yelpAttempts: 0
  },
  {
    title: 'Cabonnay', location: { lat: 42.994995, lng: -71.461685 }, phoneNumber: ' ', image: ' ', rating: ' ',
    reviewCount: ' ', address: ' ', city: ' ', state: ' ', zipcode: ' ', price: ' ', category: ' ', yelpURL: ' ', yelpAttempts: 0
  },
  {
    title: 'Republic Cafe and Bistro', location: { lat: 42.993543, lng: -71.462795 }, phoneNumber: ' ', image: ' ', rating: ' ',
    reviewCount: ' ', address: ' ', city: ' ', state: ' ', zipcode: ' ', price: ' ', category: ' ', yelpURL: ' ', yelpAttempts: 0
  },
  {
    title: 'The Birch On Elm', location: { lat: 42.991733, lng: -71.462621 }, phoneNumber: ' ', image: ' ', rating: ' ',
    reviewCount: ' ', address: ' ', city: ' ', state: ' ', zipcode: ' ', price: ' ', category: ' ', yelpURL: ' ', yelpAttempts: 0
  }
]);

function initializeMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: { lat: 43.000891, lng: -71.454675 },
    zoom: 15,
    mapTypeControl: false
  });
  for (let i = 0; i < restaurants().length; i++) {
    var myurl = "https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/" + editTitleForURL(restaurants()[i].title) + "-manchester";
    getRestaurantInfo(myurl, restaurants()[i]);
  }
}

function googleError() {
  console.log("There was a problem loading Google Maps.");
  alert("There was a problem loading Google Maps. Try refreshing the page.");
}

function createMarker(restaurant) {
  var largeInfowindow = new google.maps.InfoWindow();
  var defaultIcon = makeMarkerIcon('ff0000');
  var highlightedIcon = makeMarkerIcon('ADD8E6');
  var marker = new google.maps.Marker({
    position: restaurant.location,
    title: restaurant.title,
    phoneNumber: restaurant.phoneNumber,
    image: restaurant.image,
    rating: restaurant.rating,
    reviewCount: restaurant.reviewCount,
    address: restaurant.reviewCount,
    city: restaurant.city,
    state: restaurant.state,
    zipcode: restaurant.zipcode,
    price: restaurant.price,
    category: restaurant.category,
    yelpURL: restaurant.yelpURL,
    yelpAttempts: restaurant.yelpAttempts,
    icon: defaultIcon,
    animation: google.maps.Animation.DROP,
    id: i
  });
  newInfoWindow = largeInfowindow;
  markers.push(marker);
  marker.addListener('click', function () {
    populateInfoWindow(this, newInfoWindow);
    bounceMarker(this);
  });
  marker.addListener('mouseover', function () {
    this.setIcon(highlightedIcon);
  });
  marker.addListener('mouseout', function () {
    this.setIcon(defaultIcon);
  });
  displayMarkers();
}

function getRestaurantInfo(url, restaurant) {
  $.ajax({
    url: url,
    headers: {
      'Authorization': 'Bearer gxlzDiU86svQ3QZ-y3Cl51uY_C0k9IGCxJK_AOE4ap0ciTQ_dOAsf2vrhF4IovFZe5vV6YlWNkmBoXJCS2RgprZNXchgSFZZTkeXMgFYmIn86iFvClJrWH5oKVTOW3Yx',
    },
    method: 'GET',
    dataType: 'json',
    success: function (data) {
      restaurant.phoneNumber = data.display_phone;
      restaurant.image = data.image_url;
      restaurant.rating = data.rating;
      restaurant.reviewCount = data.review_count;
      restaurant.address = data.location.address1;
      restaurant.city = data.location.city;
      restaurant.state = data.location.state;
      restaurant.zipcode = data.location.zip_code;
      restaurant.price = data.price;
      restaurant.category = data.categories[0].title;
      restaurant.yelpURL = data.url;

      createMarker(restaurant);
    },
    error: function (status, error) {
      if (restaurant.yelpAttempts < 3) {
        console.log("Something went wrong, trying " + restaurant.title + " again.");
        getRestaurantInfo(url, restaurant);
        restaurant.yelpAttempts++
      } else {
        console.log("Could not retrieve data for " + restaurant.title);
        restaurant.title = "Could not retrieve data for " + restaurant.title;
        createMarker(restaurant);
      }
    }
  });
}

function populateInfoWindow(marker, infowindow) {
  if (infowindow.marker != marker) {
    infowindow.marker = marker;
    if (marker.yelpAttempts < 3) {
    infowindow.setContent('<div>' + marker.title + '<p>\n</p>' + marker.phoneNumber + '<p>\n</p>' +
      marker.address + ', ' + marker.city + ', ' + marker.state + ', ' + marker.zipcode +
      '<p>\n</p>' + '<img src=' + marker.image + ' id="infoImage">' + '<p>\n</p>' + 'Great if you like ' + marker.category +
      '<p>\n</p>' + 'Price: ' + marker.price + ' - ' + marker.rating + '/5 Stars - ' + marker.reviewCount + ' Reviews' +
      '<p>\n</p>' + 'Learn more on ' + '<a href=' + marker.yelpURL + ' target="_blank">Yelp</a>' + '</div>');
    } else {
      infowindow.setContent('<div>' + marker.title + '</div>');
    }
    infowindow.open(map, marker);
    infowindow.addListener('closeclick', function () {
      infowindow.marker = null;
    });
  }
}

function displayMarkers() {
  var bounds = new google.maps.LatLngBounds();
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
    bounds.extend(markers[i].position);
  }
  map.fitBounds(bounds);
}

function bounceMarker(marker) {
  marker.setAnimation(google.maps.Animation.BOUNCE);
  setTimeout(function () { marker.setAnimation(null); }, 375);
}

function makeMarkerIcon(markerColor) {
  var markerImage = new google.maps.MarkerImage(
    'http://chart.googleapis.com/chart?chst=d_map_spin&chld=1.15|0|' + markerColor +
    '|40|_|%E2%80%A2',
    new google.maps.Size(21, 34),
    new google.maps.Point(0, 0),
    new google.maps.Point(10, 34),
    new google.maps.Size(21, 34));
  return markerImage;
}

function editTitleForURL(title) {
  for (i = 0; i < title.length; i++) {
    title = title.replace(" ", "-");
  }
  return title;
}

function searchRestaurants() {
  var userInput = document.getElementById("searchInput").value;
  for (var i = 0; i < markers.length; i++) {
    var lowerCaseTitle = markers[i].title.toLowerCase();
    if (userInput.toLowerCase() != lowerCaseTitle.substr(0, userInput.length)) {
      markers[i].setMap(null);
    } else {
      markers[i].setMap(map);
      bounceMarker(markers[i]);
    }
  }
}

function showRestaurant(restaurant) {
  for (var i = 0; i < markers.length; i++) {
    if (markers[i].title == restaurant.title) {
      populateInfoWindow(markers[i], newInfoWindow)
      markers[i].setMap(map);
      bounceMarker(markers[i]);
    }
  }
}

function toggleSideBar() {
  var sideBar = document.getElementById("restaurant-list-container");
  var header = document.getElementById("header");
  var toggleButton = document.getElementById("toggle-button");
  if (sideBar.style.display === "none") {
    sideBar.style.display = "block";
    header.style.display = "block";
    toggleButton.innerHTML = "Expand Map";
  } else {
    sideBar.style.display = "none";
    header.style.display = "none";
    toggleButton.innerHTML = "Retract Map";
  }
}

ko.applyBindings();