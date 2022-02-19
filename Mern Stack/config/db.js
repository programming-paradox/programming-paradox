const mongoose = require('mongoose');
const config = require('./keys');

const db = config.mongoURI;

const connectDB = async () => {
    try {
        mongoose.connect(db, {
            useNewUrlParser: true,
            useUnifiedTopology: true
        });
        console.log('MongoDB connected...');
    } catch (err) {
        console.error("Connecting to MongoDB failed...", err);
        process.exit(1);
    }
}

module.exports = connectDB;