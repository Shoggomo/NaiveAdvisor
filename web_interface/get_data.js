/*****Abfragen der Daten*****/
function getStatistics() {
  request({
      url: "http://127.0.0.1:5000/statistics",
      method: "GET",
      success: (data) => showStatistics(data),
    error: () => document.getElementById('error').innerHTML = "Bei der Verbindung ist etws schief gelaufen. Versuchen Sie es erneut!",
});
}

function getResult(string) {
  request({
      url: string,
      method: "GET",
      success: (data) => document.querySelector('.result_number').innerHTML = data,
      error: () => document.getElementById('error').innerHTML = "Bei der Verbindung ist etws schief gelaufen. Versuchen Sie es erneut!",
});
}

/*****Eintragen der Statistiken*****/
function showStatistics(data) {
  statistics = JSON.parse(data);
  document.getElementById('accuracy').innerHTML = Math.round(statistics.accuracy*10000)/100 + "%";
  document.getElementById('valid').innerHTML = statistics.valid;
}

/*****Kontrolle der Eingabe*****/
function isCorrect(values) {
  console.log(values);
  var j;
  for (j = 0; j < values.length; j++) {
    if (isNaN(values[j]) || (values[j] < 1 || values[j] > 5)) {
      document.getElementById('error').innerHTML = "Einer der Werte ist nicht zulässig. Beachten Sie, dass es sich bei Ihrer Eingabe um Zahlen zwischen 1 und 5 handeln muss";
      console.log(values[j]);
      return false;
    }
  }
  return true;
}

/*****Zusmmensetzung des Links*****/
function buildLink(names, values) {
  var string = "http://127.0.0.1:5000/classify?";
  var i;
  for (i = 0; i < 6; i++) {
    string += names[i] + "=" + values[i] + "&";
  }
  string = string.substring(0, string.length - 1);
  return string;
}

/*****Abfragen der Nutzereingaben*****/
function getInput(){
  var service = document.getElementById('service').value;
  var cleanliness = document.getElementById('cleanliness').value;
  var value = document.getElementById('value').value;
  var sleep_quality = document.getElementById('sleep_quality').value;
  var location = document.getElementById('location').value;
  var rooms = document.getElementById('rooms').value;
  var values = [service, cleanliness, value, sleep_quality, location, rooms];
  return values;
}
/*****Geschehnisse bei Klick des Buttons*****/
function clickHandler() {
  var names = ['Service', 'Cleanliness', 'Value', 'Sleep Quality', 'Location', 'Rooms'];

  /*****Nutzereingaben*****/
  var values = getInput();

  /*****"Versenden" der Eingaben, falls Eingaben korrekt*****/
  if (isCorrect(values)) {
    getResult(buildLink(names, values));
    document.querySelector('#error').innerHTML = " ";// Sofern bei einem Test zuvor Fehlermeldungen entstanden, werden diese gelöscht.
  }
  else {
    document.querySelector('.result_number').innerHTML = " "; // Sofern bei einem Test zuvor ein gültiges Ergebnis entstand, wird dieses nun gelöscht.
  }
}

function main() {
    /*****Eintragen der Daten*****/
    getStatistics();

    /*****Button*****/
    var element = document.getElementById('button');
    element.addEventListener('click', clickHandler);
}

main();