const http = require('http')

const hostname = '127.0.0.1'
const port = 3000

const server = http.createServer((req, res) => {
    /**
     * req: http.IncomingMessage
     * res: http.ServerResponse 
     */
    let file
    if (/\/.*\.js/.test(req.url)) {
      file = req.url
    } else {
      file = '/a.html'
    }
    const fs = require('fs')
    fs.readFile(__dirname + file, (err, data) => {
      if (err) {
        console.error(err.message)
        res.statusCode = 400
        res.setHeader('Content-Type', 'text/plain')
        res.end(err.message)
        return
      }
      res.statusCode = 200
      res.setHeader('Content-Type', ' text/html')
      
      res.end(data.toString())
    })
})

server.listen(port, hostname, () => {
    // 通知server 已启动
  console.log(`Server running at http://${hostname}:${port}/`)
})