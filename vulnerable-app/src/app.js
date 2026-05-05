const express = require("express");
const search = require("./routes/search");
const login = require("./routes/login");

const app = express();

app.use(express.json());

app.use("/search", search);
app.use("/login", login);

app.listen(3000, () => {
 console.log("running");
});