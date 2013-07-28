//what I want to do is initialize the maps object to just be North America
var initialize = function(){
    var mapOptions = {
        center: new google.maps.LatLng(39.0997, -94.5783)
        , zoom: 4
        , mapTypeId: google.maps.MapTypeId.TERRAIN
        , streetViewControl: false
    }

    var map = new google.maps.Map(document.getElementById('map-div'), mapOptions);
};

google.maps.event.addDomListener(window, 'load', initialize);


$('#location-search').blur(function(){
    console.log('searching!!');
});
//then, after initialization, whenever a user's focus leaves the location box,
    //send a request to the geocoding service
    //after receiving the response to that request, relocate the map over that
    //previous location
