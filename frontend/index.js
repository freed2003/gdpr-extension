"use strict"

const statusElement = document.getElementById("status")
const statusIsElement = document.getElementById("status-is")

function setUnknownCompliance() {
    document.querySelector(".status .status-small:first-of-type").innerText = "This site has"
    statusIsElement.innerText = "unknown"
    document.querySelector(".status .status-small:last-of-type").innerText = "GDPR compliance"
}

(async () => {
    try {
        let queryOptions = { active: true, lastFocusedWindow: true }
        let [tab] = await chrome.tabs.query(queryOptions)
        if (tab.url === undefined) {
            setUnknownCompliance()
            return
        }

        let res = await (await fetch(chrome.runtime.getManifest().serverUrl + "/api/v1/?url=" + encodeURIComponent(tab.url))).json()
        statusElement.dataset.compliant = res.compliant
        if (res.compliant === true) {
            statusIsElement.innerText = "is"
        } else if (res.compliant === false) {
            statusIsElement.innerText = "is not"
        } else {
            setUnknownCompliance()
        }
    } catch (e) {
        console.log(e)
        setUnknownCompliance()
    }
})()
