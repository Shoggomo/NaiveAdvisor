function sendData(string){
request({
          url: string, //hier gehört string hin
          method: "GET",
          success: (data) => document.querySelector('.result_number').innerHTML = data,
          error: () => alert("Failed to connect to server!"),
 });
}
