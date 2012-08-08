var filters =
  {
    urls: ["https://www.google.com/*",
           "https://www.ackerleyplumbing.com/",
           "https://10.138.102.115/*"]
  };

var onBeforeRequest = function(details) {
   console.log("onBeforeRequest: " + details.tabId + " " + details.url);
};
var onSendHeaders = function(details) {
   console.log("onSendHeaders: " + details.tabId + " " + details.url);
   setTimeout(function() {
      console.log("Setting tabId " + details.tabId + " to be active")
      chrome.tabs.update(details.tabId, {active: true});
   },
   3000);
};
var onHeadersReceived = function(details) {
   console.log("onHeadersReceived: " + details.url);
};
var onCompleted = function(details) {
   console.log("onCompleted: " + details.url);
};
var onErrorOccurred = function(details) {
   console.log("onErrorOccurred: " + details.url);
};

chrome.webRequest.onBeforeRequest.addListener(onBeforeRequest,filters);
chrome.webRequest.onSendHeaders.addListener(onSendHeaders,filters);
chrome.webRequest.onHeadersReceived.addListener(onHeadersReceived,filters);
chrome.webRequest.onCompleted.addListener(onCompleted,filters);
chrome.webRequest.onErrorOccurred.addListener(onErrorOccurred,filters);
