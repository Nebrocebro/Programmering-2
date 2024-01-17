def food(edible, vegan=False):
    if vegan == True:
        print("soja" + edible)
    else:
        print(edible)

food("mjölk")
food("mjölk", True)
food("korv")
food("korv", True)
