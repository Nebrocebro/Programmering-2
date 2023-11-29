class Resource {
  constructor(name) {
    this.name = name;
  }
}

class Industry extends Resource {
  constructor(name, isFirst, isUnlocked) {
    this.name = name + " Industry";
    this.isFirst = isFirst;
  }
  checkOrder = function (isFirst) {
    if ((this.isFirst = true)) {
      this.isUnlocked = true;
    }
  };
}
