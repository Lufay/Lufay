const {JSDOM} = require("jsdom");
const fs = require('fs')
const path = require('path')
const url = require('url')

const html_file = process.argv[2]
fs.readFile(html_file, 'utf8', (err, data) => {
    if (err) {
        console.error(err)
        return
    }
    // global.document = new JSDOM(data).window.document
    console.log(path.normalize(html_file))
    const html_url = url.pathToFileURL(html_file)
    
    const {document} = new JSDOM(data, {"runScripts":"dangerously", "resources":"usable", url: html_url.href}).window
    console.log(document.body.childElementCount)
    console.log(document.body.children[0].outerHTML)

    document.addEventListener('DOMContentLoaded', () => {
        setImmediate(() => {
            console.log(document.body.children[0].outerHTML)
        })
    })
// eval("x=10;y=20;document.write(x*y)");
// document.write("<br>" + eval("2+2"));
// document.write("<br>" + eval(x**2));

// console.log(document.querySelector('html').outerHTML)
})

