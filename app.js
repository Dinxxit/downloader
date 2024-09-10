const express = require('express');
const path = require('path');
const app = express();
const port = 3000;

// Serve static files from the "public" directory
app.use(express.static('public'));

// Route for downloading files
app.get('/download', (req, res) => {
    const file = req.query.file;
    const filePath = path.join(__dirname, 'downloads', file);

    res.download(filePath, file, (err) => {
        if (err) {
            console.error("Error while downloading file:", err);
            res.status(500).send('File not found.');
        }
    });
});

app.listen(port, () => {
    console.log(`App is running at http://localhost:${port}`);
});