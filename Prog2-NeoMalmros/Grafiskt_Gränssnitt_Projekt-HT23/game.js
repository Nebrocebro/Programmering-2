const sleep = (delay) => new Promise((resolve) => setTimeout(resolve, delay));

class AngelSystem {
  constructor() {
    this.points = 0;
    this.baseProfitBoost = 0.02; // 2%
    this.multiplier = 1;
  }

  calculatePoints(industry) {
    const contributionMap = {
      Farm: 1,
      Forest: 2,
      Fishing: 3,
      Mining: 4,
    };

    const contribution = contributionMap[industry.industryName];
    return isNaN(contribution) ? 0 : (industry.bank / 1e12) * contribution;
  }

  updatePoints(industryList) {
    this.points = industryList.reduce((totalPoints, industry) => {
      return totalPoints + this.calculatePoints(industry);
    }, 0);

    this.points = isNaN(this.points) ? 0 : this.points;

    this.multiplier = Math.pow(10, Math.floor(Math.log10(this.points)));
  }

  applyProfitBoost(industryList) {
    const profitBoost = this.points * this.baseProfitBoost;

    industryList.forEach((industry) => {
      industry.buildingList.forEach((building) => {
        building.profit *= 1 + profitBoost;
      });
    });
  }
}

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
    this.buildingList = buildingList || [];
  }
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

function createBuildingContainer(building, industry) {
  var buildingContainer = document.createElement("div");
  buildingContainer.classList.add(
    "building",
    `${building.name.replace(/\s+/g, "_")}Building`
  );
  buildingContainer.id = building.name;
  buildingContainer.dataset.instance = JSON.stringify(building);
  buildingContainer.insertAdjacentHTML(
    "beforeend",
    `<p>${building.name}</p>
     <p>Amount: <span class="amount">${building.amount}</span></p>
     <p>Profit: <span class="profit">${building.profit}</span></p>
     <p>Cost: ${building.cost}</p>
     <button class="buyButton">Buy</button>`
  );

  var buyButton = buildingContainer.querySelector(".buyButton");
  buyButton.addEventListener("click", function () {
    Buy(building, industry);
  });

  return buildingContainer;
}

function createIndustryContainer(industry) {
  var industryContainer = document.createElement("div");
  industryContainer.classList.add("industryContainer");
  industryContainer.id = `${industry.industryName.replace(
    /\s+/g,
    "_"
  )}Industry`;
  industryContainer.dataset.instance = JSON.stringify(industry);

  var header = document.createElement("div");
  header.classList.add("industryHeader");
  industryContainer.appendChild(header);

  if (!industry.isUnlocked) {
    var unlockButton = document.createElement("button");
    unlockButton.textContent = "Unlock";
    unlockButton.addEventListener("click", function () {
      unlockIndustry(industry);
    });
    header.appendChild(unlockButton);

    header.insertAdjacentHTML(
      "beforeend",
      `<p>Unlock Cost: ${industry.unlockCost}</p>`
    );
  }

  if (industry.buildingList) {
    for (var m = 0; m < industry.buildingList.length; m++) {
      var buildingContainer = createBuildingContainer(
        industry.buildingList[m],
        industry
      );
      industryContainer.appendChild(buildingContainer);
    }
  }

  return industryContainer;
}

function appendIndustryContainers() {
  var mainContainer = document.getElementById("mainContainer");
  if (mainContainer) {
    for (var l = 0; l < industryList.length; l++) {
      var industryContainer = createIndustryContainer(industryList[l]);
      mainContainer.appendChild(industryContainer);
    }
  } else {
    console.error("Main container not found");
  }
}

function startGame() {
  isRunning = true;
  const farmBuildings = [
    new Building("Farmers", 2, 1, 10, "Farm"),
    new Building("Tractors", 3, 0, 1000, "Farm"),
    new Building("Fields", 9, 0, 100000, "Farm"),
    new Building("Silos", 15, 0, 1000000, "Farm"),
    new Building("Farms", 10, 0, 10000000000, "Farm"),
  ];

  const forestBuildings = [
    new Building("Lumberjacks", 3, 1, 10, "Forest"),
    new Building("Sawmills", 3, 0, 1000, "Forest"),
    new Building("Tree Plantations", 9, 0, 1000000, "Forest"),
    new Building("Logging Camps", 15, 0, 10000000, "Forest"),
    new Building("Forest Gods", 10, 0, 100000000000, "Forest"),
  ];

  const fishingBuildings = [
    new Building("Fishing Boats", 4, 1, 10, "Fishing"),
    new Building("Fish Farms", 3, 0, 10000, "Fishing"),
    new Building("Harpoon Cannons", 9, 0, 100000, "Fishing"),
    new Building("Seafood Processing Plants", 15, 0, 10000000, "Fishing"),
    new Building("Atlantis Submarine", 10, 0, 10000000000, "Fishing"),
  ];

  const miningBuildings = [
    new Building("Miners", 6, 1, 100, "Mining"),
    new Building("Quarries", 3, 0, 1000, "Mining"),
    new Building("Drilling Rigs", 9, 0, 1000000, "Mining"),
    new Building("Refineries", 15, 0, 1000000, "Mining"),
    new Building("Asteroid Mines", 10, 0, 1000000000, "Mining"),
  ];

  industryList = [
    (FarmInd = new Industry("Farm", "Potato", 0, true, true, 0, farmBuildings)),
    (ForInd = new Industry(
      "Forest",
      "Wood",
      0,
      false,
      false,
      10000,
      forestBuildings
    )),
    (FishInd = new Industry(
      "Fishing",
      "Fish",
      0,
      false,
      false,
      1000000,
      fishingBuildings
    )),
    (MineInd = new Industry(
      "Mining",
      "Rare Minerals",
      0,
      false,
      false,
      1000000000,
      miningBuildings
    )),
  ];

  appendIndustryContainers();
}

function Buy(Building, Industry) {
  if (
    (Building.industry = Industry.industryName) &&
    Industry.bank >= Building.cost
  ) {
    Industry.bank -= Building.cost;
    Building.amount += 1;
    updateBuildingDisplay(Building);
  } else {
    console.log("Du har inte råd!");
  }
}

function unlockIndustry(industry) {
  const precedingIndustry = getPrecedingIndustry(industry);

  if (precedingIndustry && precedingIndustry.bank >= industry.unlockCost) {
    industry.isUnlocked = true;
    updateIndustryHeader(industry);
    updateIndustryHeader(precedingIndustry);
  } else {
    console.log("Du har inte råd med industrin! Fortsätt jobba på!");
  }
}

function getPrecedingIndustry(industry) {
  const industryIndex = industryList.findIndex((i) => i === industry);
  if (industryIndex > 0) {
    return industryList[industryIndex - 1];
  }
  return null;
}

async function gameLoop(angelSystem) {
  while (isRunning) {
    for (let i = 0; i < industryList.length; i++) {
      const currentIndustry = industryList[i];
      const buildingList = currentIndustry.buildingList || [];

      if (
        buildingList &&
        buildingList.length > 0 &&
        currentIndustry.isUnlocked
      ) {
        for (let j = 1; j < buildingList.length; j++) {
          const currentBuilding = buildingList[j];
          const previousBuilding = buildingList[j - 1];

          const profit = currentBuilding.profit * previousBuilding.amount;
          currentIndustry.bank += profit;

          const generatedAmount = Math.floor(profit / currentBuilding.cost);
          previousBuilding.amount += generatedAmount;
          updateBuildingDisplay(previousBuilding);
        }

        const firstBuilding = buildingList[0];
        currentIndustry.bank += firstBuilding.profit * firstBuilding.amount;
        updateBuildingDisplay(firstBuilding);
      }

      updateIndustryHeader(currentIndustry);
    }

    angelSystem.updatePoints(industryList);
    angelSystem.applyProfitBoost(industryList);

    await sleep(1000);
  }
}

function updateBuildingDisplay(building) {
  var buildingContainer = document.getElementById(building.name);
  var amountElement = buildingContainer.querySelector(".amount");
  var profitElement = buildingContainer.querySelector(".profit");

  amountElement.textContent = building.amount;
  profitElement.textContent = building.profit;
}

function updateIndustryHeader(industry) {
  var industryContainer = document.getElementById(
    `${industry.industryName.replace(/\s+/g, "_")}Industry`
  );

  if (industryContainer) {
    var header = industryContainer.querySelector(".industryHeader");

    if (header) {
      header.innerHTML = `<p>Bank: ${industry.bank}</p>
                          <p>Profit Rate: ${industry.buildingList[0].profit}</p>`;

      if (!industry.isUnlocked) {
        var unlockButton = header.querySelector(".buyButton");
        if (!unlockButton) {
          unlockButton = document.createElement("button");
          unlockButton.textContent = "Unlock";
          unlockButton.classList.add("buyButton");
          unlockButton.addEventListener("click", function () {
            unlockIndustry(industry);
          });

          header.insertAdjacentHTML(
            "beforeend",
            `<p class="unlockCost excludeGreyOut">Unlock Cost: ${industry.unlockCost}</p>`
          );

          header.appendChild(unlockButton);
        }

        industryContainer.classList.add("lockedIndustry");
      } else {
        industryContainer.classList.remove("lockedIndustry");
      }
    }
  }
}

const angelSystem = new AngelSystem();
startGame();
gameLoop(angelSystem);