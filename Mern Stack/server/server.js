const express = require('express');
const app = express();
const connectDb = require('../config/db');
const PORT = process.env.PORT || 5000;

connectDb();


//Defining routes
app.use(express.json({ extended: false }));
app.use("/api/users", require("../routes/userApi"));

app.use("/api/products", require("../routes/productsApi"));



app.get("/", (req, res) => {
    res.send("My app is up and running!");
})


app.listen(PORT, () => {
    console.log(`server is running on port ${PORT}`);
})