const {Config} = require('../reactAppBuild/src/Config.js');
const express = require('express');
var https = require('https');
var http = require('http');
var fs = require('fs');
const path = require('path');
const app = express();
const cors = require('cors');

const ca = [];
let chain = fs.readFileSync(Config.API_CA_T,'utf-8');
chain = chain.split("\n");
let cert = [];
for (let line of Array.from(chain)) {
  if (line.length !== 0) {
    cert.push(line);
    if (line.match("-----END CERTIFICATE-----")) {
      ca.push(cert.join("\n"));
      cert = [];
    }
  }
}

//const port = 3000
const httpsPort = 8443
// This line is from the Node.js HTTPS documentation.
var options = {
  ca: ca,
  key: fs.readFileSync(Config.API_KEY),
  cert: fs.readFileSync(Config.API_CRT),
  rejectUnauthorized: false,
  requestCert: false
};

// This application level middleware prints incoming requests to the servers console, useful to see incoming requests
app.use((req, res, next) => {
    res.header("Access-Control-Allow-Origin","*");
    res.header("Access-Control-Allow-Headers","Origin, X-Requested-With, Content-Type, Accept");
    console.log(`Request_Endpoint: ${req.method} ${req.url}`);
    next();
});
// Configure the CORs middleware
app.use(cors());

app.use(express.static(path.join(__dirname, 'build')));

app.get('/', function (req, res) {
  res.sendFile(path.join(__dirname, 'build', 'index.html'));
});

//app.listen(port, () => console.log(`BACK_END_SERVICE_PORT: ${port}`));
// Create an HTTP service.
//http.createServer(app).listen(port,() => console.log(`Http app service started on port: ${port}`));
https.createServer(options, app).listen(httpsPort,() => console.log(`Https app service started on port: ${httpsPort}`));
// app.listen(9000);