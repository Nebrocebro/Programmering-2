const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));

class Industry {
  constructor(
    industryName,
    resourceName,
    bank,
    isFirst,
    isUnlocked,
    unlockCost,
    buildingList
  ) {
    this.industryName = industryName + " Industry";
    this.isFirst = isFirst;
    this.isUnlocked = isUnlocked;
    this.bank = bank;
    this.resourceName = resourceName;
    this.unlockCost = unlockCost;
    this.buildingList = buildingList;
  }
  checkFirst = function () {
    if (this.isFirst == true) {
      this.isUnlocked = true;
      this.unlockCost = 0;
    } else {
      this.isUnlocked = false;
    }
  };
}

class Building {
  constructor(name, profit, amount, cost, industry) {
    this.name = name;
    this.profit = profit;
    this.amount = amount;
    this.cost = cost;
    this.industry = industry;
  }
}

class Manager {}

function startGame() {
  isRunning = true;
  buyCoef = 0;
  j = 0;
  START_SPEED = 5;
  industryList = [
    (FarmInd = new Industry("Farm", "Potato", 0, true, true, 0, [
      new Building("Farmers", 4, 1, 10, "Farm"),
      new Building("Tractors", 3, 0, 1000, "Farm"),
      new Building("Fields", 9, 0, 100000, "Farm"),
      new Building("Silos", 15, 0, 1000000, "Farm"),
      new Building("Farms", 10, 0, 1000000000, "Farm"),
    ])),
    (ForInd = new Industry("Forest", "Wood", 0, false, false, 10000)),
    (FishInd = new Industry("Fishing", "Fish", 0, false, false, 1000000)),
    (MineInd = new Industry(
      "Mining",
      "Rare Minerals",
      0,
      false,
      false,
      1000000000
    )),
  ];

  for (l = 0; l < industryList.length; l++) {
    var mainContainer = document.getElementsByClassName("mainContainer");
    var industryBox = document.createElement("div");
    industryBox.classList.add("industryContainer");
    industryBox.id = industryList[l].industryName + "Industry";
    for (m = 0; m < industryList[l].buildingList.length; m++) {
      var building = document.createElement("div");
      building.classList.add(
        "building",
        `${Industry.industryName + "Building"}`
      );
      building.id = `${industryList[l].buildingList[m].name}`;
      industryBox.appendChild(building);
    }
    mainContainer.appendChild(industryBox);
  }

  totalAngels = 0; // Prestige percentage multipliers, 1 angel = 2% (0.02x) base bonus
  // Varje industri ger änglar, men olika mycket, typ som comrades i AdCom, tex. farm ger 0.1 änglar per "krävd summa" och mining ger 2
  // (krävd summa som ökar exponentiellt, sök upp adcap how do i get angels och math geeks formula)
}

function buyAmount() {
  percentList = [0, 0.01, 0.1, 0.5, 1];
  buyCoef = percentList[j];
  if (j < percentList.length) {
    j++;
  } else {
    j = 0;
  }
}

function Buy(Building, Industry) {
  if (
    (Building.industry = Industry.industryName) &&
    Industry.bank >= Building.cost
  ) {
    Building.amount += Math.floor(buyCoef * (Industry.bank / Building.cost));
  } else {
    console.log("Du har inte råd!");
  }
}

function gameLoop(Industry) {
  // kanske göra en loop så att den bara kollar varje industri i listan, då förenklas unlockCost delen nedan
  while (isRunning) {
    earnings_this_round = START_SPEED;
    for (let i = 0; i < powerUps.length; i++) {
      const powerUp = powerUps[i];
      earnings_this_round = powerUp.speed * earnings_this_round;
    }
    Industry.bank += earnings_this_round;

    // console.log(totalResource); Visa upp i sidan

    if (industryList.index(Industry) < industryList.length) {
      if (
        Industry.bank >=
        industryList[industryList.index(Industry + 1)].unlockCost
      ) {
        console.log("Du har nu råd med nästa industri!");
      }
    } else {
      continue;
    }
  }
}

startGame();
gameLoop();
