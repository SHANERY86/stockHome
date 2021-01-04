var http = require('http'); // Import Node.js core module
const fs = require('fs').promises;
var server = http.createServer(function (req, res) {   //create web server
    if (req.url == '/') { //check the URL of the current request
       
        
        // set response content    
    fs.readFile(__dirname + "/index.html")
        .then(contents => {
            res.setHeader("Content-Type", "text/html");
            res.writeHead(200);
            res.end(contents);
        })


});

server.listen(5000); //6 - listen for any incoming requests

console.log('Node.js web server at port 5000 is running..')