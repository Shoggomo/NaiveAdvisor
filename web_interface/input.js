var element = document.getElementById('send');
element.addEventListener('click', clickHandler);

var elementIsClicked = false;
function clickHandler(){
    console.log('clicked');
    var service = document.getElementById('service').value;
    var cleanliness = document.getElementById('cleanliness').value;
    var value = document.getElementById('value').value;
    var sleep_quality = document.getElementById('sleep_quality').value;
    var location = document.getElementById('location').value;
    var rooms = document.getElementById('rooms').value;
    var all = [service, cleanliness, value, sleep_quality, location, rooms];
    var names = ['service', 'cleanliness', 'value', 'sleep_quality', 'location', 'rooms'];
    console.log(names);
    console.log(service);
    console.log(document.getElementById('service').innerHTML);
    console.log(all);

    var string = "http://127.0.0.1:5000/classifier?";
    var i;
    for(i=0; i< 6; i++)
    {
        string += names[i] + "=" + all[i] + "&";
    }

    string = string.substring(0, string.length - 1);

    document.getElementById('test').innerHTML = string;
    elementIsClicked = true;
    sendData(string);

}









//service, cleanliness, value, sleep quality, location, rooms


