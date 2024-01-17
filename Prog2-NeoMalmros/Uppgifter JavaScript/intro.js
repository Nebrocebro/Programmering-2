const express = require('express')
const app = express()
const port = 3000

app.get('/', (req, res) => {
  res.send('Hello ExpressJS Räksmörgås World!')
})

app.get('/cake', (req, res) => {
  res.send('Tårta🍰')
})

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`)
})