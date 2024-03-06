// const csvFile = "teams.csv";

// const input = csvFile[0];
// const reader = new FileReader();
// reader.onload = function (e) {
//   const text = e.target.result;
//   document.write(text);
// };
// reader.readAsText(input);

// lineReader.eachLine("teams.csv", (line, last) => {
//   console.log(line);
// });

const fs = require("fs");
const readline = require("readline");
// const lineReader = require("line-reader");

const columnName1 = "xGoalsFor";
let maxValue = [-Infinity];

const file = readline.createInterface({
  input: fs.createReadStream("teams.csv"),
  output: process.stdout,
  terminal: false,
});

const xGoalsForIndex = 12;

file.on("line", (line) => {
  const values = line.split(","); //"VAN,2023" => ["VAN", "2023",...]
  const columnIndex = values.indexOf(columnName1);

  // Check that it is not first row (headers)
  if (columnIndex === -1) {
    const columnValue = parseFloat(values[xGoalsForIndex]);

    if (!isNaN(columnValue) && columnValue > maxValue[0]) {
      maxValue.splice(0, 0, columnValue);
    } else if (!isNaN(columnValue) && columnValue < maxValue[0]) {
      for (let i = 0; i < 10; i++) {
        if (columnValue > maxValue[i]) {
          if (maxValue.length >= 10) {
            maxValue.pop();
          }
          maxValue.splice(i, 0, columnValue);
          break;
        } else {
          continue;
        }
      }
    }
  }
});

file.on("close", () => {
  maxValue.sort(function (a, b) {
    return a - b;
  });
  while (maxValue.length > 10) {
    maxValue.pop();
  }
  console.log("Top 10 highest goal values:", maxValue);
});
