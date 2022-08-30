const https = require('https')
const url = ''
https.get(url, (resp) => {
    const {statusCode} = resp
    const contType = resp.headers['content-type']
    let err
    if (statusCode !== 200) {
        err = new Error(`request failed with code ${statusCode}`)
    } else if (!/^text\/html/.test(contType)) {
        err = new Error(`invalid content-type of ${contType}`)
    }
    if (err) {
        console.error(err.message)
        resp.resume()
        return
    }

    let rawData = ''
    resp.on('data', (chunk) => {
        rawData += chunk
    })
    resp.on('end', () => {
        try {
            // console.log(rawData)
            const jsdom = require("jsdom");
            const {JSDOM} = jsdom;
            const {window} = new JSDOM(rawData, {runScripts: "dangerously", resources:"usable", url:url})
            // window.location.
            // global.document = new JSDOM(rawData, {runScripts: "dangerously", resources:"usable"}).window.document
            console.log(window.document.body.children[0].outerHTML)

            window.document.addEventListener('DOMContentLoaded', () => {
                setImmediate(() => {
                    console.log(window.document.body.children[1].outerHTML)
                })
            })
        } catch (e) {
            console.error(e.message)
        }
    })
}).on('error', (err) => {
    console.error(err.message)
})