function sendData(string){
request({
          url: "http://127.0.0.1:5000/classifier?service=3&cleanliness=4$value=5&sleep_quality=3&location=2&rooms=5", //hier gehört string hin
          method: "GET",
          success: (data) => document.getElementByClassName('result_text').innerHTML = data,
          error: () => alert("Failed to connect to server!"),
 });
}
