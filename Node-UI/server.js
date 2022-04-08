const express = require('express');
const path = require('path');
const app = express();

const mark_nodes = require('../Markiplier/network.json');

//Init Middleware
app.use(express.json({ extend: false }));

//app.use(express.static("public"));

app.get("/", (req, res) => res.sendFile(path.join(__dirname, '/public/index.html')));

app.get("/markiplier", (req, res) => {
    try {
        res.json(mark_nodes);
    } catch (err) {
        console.error(err.message);
        res.status(500).send('Server error');
    }
})

const port = process.env.PORT || 3000;

app.listen(port, () => {
    console.log(`App listening at http://localhost:${port}`)
})