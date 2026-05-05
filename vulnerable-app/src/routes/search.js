const express = require('express');
const router = express.Router();

router.get('/', (req,res) => {

 const q=req.query.q;

 const query =
   "SELECT * FROM products WHERE name='"
   + q +
   "'";

 db.query(query);

 res.send("ok");

});

module.exports = router;