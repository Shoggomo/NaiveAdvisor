/*****von Alexander Bazo - Skript zur Verbindung zum Server*****/

var request = request || (function() {

  const READY_STATES = {
      UNITIALIZED: 0,
      CONNECTED: 1,
      SERVER_RECEIVED_REQUEST: 2,
      SERVER_PROCESSING_REQUEST: 3,
      RESPONSE_READY: 4,
    },
    HTTP_CODES = {
      OK_200: 200,
      FORBIDDEN_403: 403,
      NOT_FOUND_404: 404,
    };

  function failed() {
    return false;
  }

  function onResponseReady(response, onSuccess, onError) {
    var success = onSuccess || failed;
      error = onError || failed;
    switch (response.status) {
      case HTTP_CODES.OK_200:
        success(response.responseText);
        break;
      case HTTP_CODES.FORBIDDEN_403:
        error("HTTP Error 403: Access forbidden.");
        break;
      case HTTP_CODES.NOT_FOUND_404:
        error("HTTP Error 404: Document not found.");
        break;
      default:
        error("Unknown Error");
        break;
    }
  }

  function createXMLHttpRequest(onSuccess, onError) {
    var httpRequest = new XMLHttpRequest();
    httpRequest.onreadystatechange = function() {
      switch (this.readyState) {
        case READY_STATES.UNITIALIZED:
          break;
        case READY_STATES.CONNECTED:
          break;
        case READY_STATES.SERVER_RECEIVED_REQUEST:
          break;
        case READY_STATES.SERVER_PROCESSING_REQUEST:
          break;
        case READY_STATES.RESPONSE_READY:
          onResponseReady(this, onSuccess, onError);
          break;
        default:
          break;
      }
    };
    return httpRequest;
  }

  function request(options) { //options beinhaltet die URL, Methode und auszuführenden Befehle bei Erfolg bzw. Misserfolg der Verbindung
    var request = createXMLHttpRequest(options.success,
      options.error);
    request.open(options.method, options.url, true);
    request.send();
  }

  return request;
}());
