const jwt=require('jsonwebtoken');

function login(req,res){

 let user=req.body.user;

 let token=jwt.sign(
   {admin:true},
   "hardcoded-jwt-secret"
 );

 res.json({token});

}

module.exports=login;