const express = require('express');
const path = require('path');
const fs = require('fs');

const app = express();

//const mark_nodes = require('../Markiplier/network.json');

//Init Middleware
app.use(express.json({ extend: false }));

//app.use(express.static("public"));

app.get("/", (req, res) => res.sendFile(path.join(__dirname, '/public/index.html')));

app.get("/markiplier", (req, res) => {
    try {
        let rawdata = fs.readFileSync('../Markiplier/network.json');
        let data = JSON.parse(rawdata);
        res.json(data);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server error');
    }
})

const port = process.env.PORT || 3000;

app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`)
})