// const express = require("express");
// const app = express();
// var fs = require("fs");
// app.get("/", (req, res) => {
//   res.send("Welcome to the homepage!");
// });
// app.get("/counter", (req, res) => {
//   fs.readFile("./counter.txt", function (err, data) {
//     var nbr = Number(data.toString());
//     nbr++;
//     fs.writeFile("./counter.txt", nbr, function (err) {
//       if (err) throw err;
//     });
//     res.setHeader("Content-Type", "text/html; charset=utf-8");
//     res.end(`Denna sida har laddats ${nbr} gånger`);
//   });
// });
// app.listen(3000);

const express = require("express");
const app = express();
const fs = require("fs");

app.get("/", (req, res) => {
  res.send("Welcome to the homepage!");
});

app.get("/counter", (req, res) => {
  fs.readFile("./counter.txt", (err, data) => {
    if (err) {
      console.error("Error reading counter.txt:", err);
      res.status(500).send("Internal Server Error");
      return;
    }

    let nbr = Number(data.toString());
    nbr++;

    fs.writeFile("./counter.txt", nbr, (err) => {
      if (err) {
        console.error("Error writing counter.txt:", err);
        res.status(500).send("Internal Server Error");
        return;
      }
    });

    res.setHeader("Content-Type", "text/html; charset=utf-8");
    res.end(`Denna sida har laddats ${nbr} gånger`);
  });
});

app.listen(3000, () => {
  console.log("Server is running on http://localhost:3000");
});
