const express = require('express');
const app = express();
const dt = require('./myfirstmodule');

app.get('/', (req, res) => {
    res.send('Welcome to the homepage!');
});

app.get('/time', (req, res) => {
    res.writeHead(200, { 'Content-Type': 'text/html' });
    res.write("The date and time are currently: " + dt.myDateTime());
    res.end();
});

app.listen(3000, () => {
    console.log('Server is running on http://localhost:3000 and the time function can be viewed at http://localhost:3000/time');
});
