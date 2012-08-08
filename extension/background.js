var filters =
  {
    urls: ["https://www.google.com/*"]
  };

var onBeforeRequest = function(details) {
    console.log("onBeforeRequest: " + details.url);
  };
var onBeforeSendHeaders = function(details) {
    console.log("onBeforeSendHeaders: " + details.url);
  };
var onSendHeaders = function(details) {
    console.log("onSendHeaders: " + details.url);
  };
var onHeadersReceived = function(details) {
    console.log("onHeadersReceived: " + details.url);
  };
var onBeforeRedirect = function(details) {
    console.log("onBeforeRedirect: " + details.url);
  };
var onResponseStarted = function(details) {
    console.log("onResponseStarted: " + details.url);
  };
var onCompleted = function(details) {
    console.log("onCompleted: " + details.url);
  };
var onErrorOccurred = function(details) {
    console.log("onErrorOccurred: " + details.url);
  };

chrome.webRequest.onBeforeRequest.addListener(onBeforeRequest,filters);
chrome.webRequest.onBeforeSendHeaders.addListener(onBeforeSendHeaders,filters);
chrome.webRequest.onSendHeaders.addListener(onSendHeaders,filters);
chrome.webRequest.onHeadersReceived.addListener(onHeadersReceived,filters);
chrome.webRequest.onBeforeRedirect.addListener(onBeforeRedirect,filters);
chrome.webRequest.onResponseStarted.addListener(onResponseStarted,filters);
chrome.webRequest.onCompleted.addListener(onCompleted,filters);
chrome.webRequest.onErrorOccurred.addListener(onErrorOccurred,filters);

