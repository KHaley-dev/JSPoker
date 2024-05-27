const express = require('express');
const app = express();
const path = require('path');

app.use(express.static(path.join(__dirname)));

app.get("/", (req, res) => {
    res.sendFile(path.join(__dirname, 'index.html'))
})

app.get('/room/:roomId', (req, res) => {
    const roomId = req.params.roomId;
    res.sendFile(path.join(__dirname, 'room.html'));
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});