var app = require("express")();
var http = require("http").Server(app);
var io = require("socket.io")(http);

app.get("/", function (req, res) {
  res.sendFile(__dirname + "/index.html");
});

// on "connection" sker när en klient kopplar sig till servern
io.on("connection", function (socket) {
  console.log("A user connected");

  // Säger till servern att lyssna efter "scream" emit från klienten
  socket.on("scream", function (data) {
    console.log("I heard a scream: " + data);
  });
});

http.listen(8080, function () {
  console.log("listening on *:8080");
});
