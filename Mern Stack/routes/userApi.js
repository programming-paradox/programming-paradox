const express = require('express');
const router = express.Router();
const bcrypt = require('bcryptjs');
const {check, validationResult} = require('express-validator');
const User = require('../models/User');
const jwt = require("jsonwebtoken")
const jwtSecret = require("../config/keys").jwtSecret;


router.post("/", [
    check('name', "Name is required").not().isEmpty(),
    check('email', "Email is required").isEmail(),
    check('password', "Password should have atleast 6 Character").isLength({min: 6})
], async (req, res) => {
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({
            errors: errors.array()
        });
    }

    try {
        const {name, email, password} = req.body;
        let user = await User.findOne({email: email});

        if (user) {
            return res.status(400).json({msg: "User already exists"});
        }

        user = new User({
            name,
            email,
            password
        });

        const salt = await bcrypt.genSalt(10)
        user.password = await bcrypt.hash(password, salt);
        

        //creating a payload
        const payload = {
            user: {
                id: user.id,
                email: user.email
            },
        }; 

        user.save()
        
        jwt.sign(payload, jwtSecret, {expiresIn: 360000}, (err, token) => {
            if (err) {
                res.status(500).json({"msg": "Server Error"});
                return
            } else {
                res.status(200).json({
                    token
                });
            }
         });
        
    } catch (error) {
        console.log(error)
        res.status(500).send("server error")
        return;
    }
})

module.exports = router;