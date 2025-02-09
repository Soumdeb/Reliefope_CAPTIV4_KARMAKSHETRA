chrome.runtime.onInstalled.addListener(() => {
    console.log("Reliefope Extension Installed.");
});

chrome.action.onClicked.addListener(() => {
    chrome.tabs.create({ url: "https://reliefope.com" });
});
