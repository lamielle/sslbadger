var filters =
  {
    urls: ["https://*/*"],
    types: ["main_frame"]
  };

var pendingRequests = {};

var removeRequest = function(pendingRequests, requestId) {
   pendingRequestData = pendingRequests[requestId];
   if (pendingRequestData !== undefined) {
      timeoutInfo = pendingRequestData['timeoutInfo'];
      if (timeoutInfo !== undefined) {
         console.log("Clearing timeout for timeoutId " + timeoutInfo['timeoutId']);
         clearTimeout(timeoutInfo['timeoutId']);
      }
      delete pendingRequestData[requestId];
   }
};

var onBeforeRequest = function(details) {
   console.log("onBeforeRequest: " + details.requestId + " " + details.tabId);

   // The Chrome extension API guarantees all requests will end with either
   // onCompleted or onErrorOccurred being called EXCEPT for data:// URLs.
   // Exclude those so we don't add a new key that will never be removed.
   if (details.url.substring(0, 7) !== "data://") {
      this.pendingRequests[details.requestId] = {tabId: details.tabId};
   }
};

var onSendHeaders = function(details) {
   console.log("onSendHeaders: " + details.requestId+ " " + details.tabId);

   // The transition from onSendHeaders to onHeadersReceived doesn't
   // happen until the SSL warning is accepted.  Set a timeout to wait a
   // few seconds to see if we're stalled on this transition.  If we are,
   // tell the SSL Badger server to send a tab+enter combo to skip the SSL
   // warning interstitial.
   timeoutId = setTimeout(function() {
      console.log("Setting tabId " + details.tabId + " to be active for requestId " + details.requestId + " and url " + details.url);
      chrome.tabs.update(details.tabId, {active: true});
      var xmlHttp = new XMLHttpRequest();
      xmlHttp.open("GET", "http://localhost:9999/sendTabEnter", false);
      xmlHttp.send(null);
   }, 3000);
   this.pendingRequests[details.requestId]['timeoutInfo'] = {'timeoutId': timeoutId};
};

var onHeadersReceived = function(details) {
   console.log("onHeadersReceived: " + details.requestId);
   removeRequest(this.pendingRequests, details.requestId);
};

var onErrorOccurred = function(details) {
   console.log("onErrorOccurred: " + details.requestId);
   removeRequest(this.pendingRequests, details.requestId);
};

// Register event handlers for various web request states
chrome.webRequest.onBeforeRequest.addListener(onBeforeRequest,filters);
chrome.webRequest.onSendHeaders.addListener(onSendHeaders,filters);
chrome.webRequest.onHeadersReceived.addListener(onHeadersReceived,filters);
chrome.webRequest.onErrorOccurred.addListener(onErrorOccurred,filters);
