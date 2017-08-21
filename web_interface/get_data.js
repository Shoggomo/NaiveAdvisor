/*****Holen der Daten*****/
function sendData(string){
request({
          url: string,
          method: "GET",
          success: (data) => document.querySelector('.result_number').innerHTML = data,
          error: () => document.getElementById('con_error').innerHTML = "Bei der Verbindung ist etws schief gelaufen. Versuchen Sie es erneut!",
 });
}
isCorrect(value)
{
    if (isNaN(value) || (value < 1 || value > 5)) {
        document.getElementById('input_error').innerHTML = "Einer der Werte ist nicht zulässig. Beachten Sie, dass es sich bei Ihrer Eingabe um Zahlen zwischen 1 und 5 handeln muss";
        return;
    }
}

/*****Button*****/
var element = document.getElementById('send');
element.addEventListener('click', clickHandler);

var elementIsClicked = false;
function clickHandler(){

    /*****Nutzereingaben*****/
    var service = document.getElementById('service').value;
    var cleanliness = document.getElementById('cleanliness').value;
    var value = document.getElementById('value').value;
    var sleep_quality = document.getElementById('sleep_quality').value;
    var location = document.getElementById('location').value;
    var rooms = document.getElementById('rooms').value;

    var all = [service, cleanliness, value, sleep_quality, location, rooms];
    var names = ['Service', 'Cleanliness', 'Value', 'Sleep Quality', 'Location', 'Rooms'];

    /*****Kontrolle der Eingabe*****/
    var j;
    for(j=0; j<all.length; j++){
        isCorrect(all[j]);
    }


    for(j=0; j<all.length; j++){

    }

    /*****Zusmmensetzung des Links*****/
    var string = "http://127.0.0.1:5000/classify?";
    var i;
    for(i=0; i< 6; i++)
    {
        string += names[i] + "=" + all[i] + "&";
    }
    string = string.substring(0, string.length - 1);
    elementIsClicked = true;
    sendData(string);
}
