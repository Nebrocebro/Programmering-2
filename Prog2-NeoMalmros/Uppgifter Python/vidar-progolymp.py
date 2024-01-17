karta = [[".", ".", ".", ".", ".", "#", "#", "#", "."],
         [".", ".", ".", ".", "#", "#", "#", "#", "#"],
         [".", ".", ".", "#", "#", "#", "#", "#", "#"],
         [".", ".", "#", "#", "#", "#", "#", "#", "."],
         [".", "#", "#", "#", "#", "#", "#", ".", "."],
         [".", "#", "#", "#", "#", ".", ".", ".", "."],
         ["#", "#", "#", "#", "S", "#", ".", "#", "."],
         ["#", "#", "#", "#", "#", ".", ".", ".", "."],
         [".", "#", "#", ".", ".", ".", ".", ".", "."],]

# Gör en array av arrayer, hitta stockholm, leta i koordinaterna bredvid för land, 
# lägg in dem i visited_koordinater array och kolla land omkring om de är land och 
# ifall de är hittade redan, gör inte land visited om det är på andra sidan av vatten från sthlm
vattenpixel = "."
landpixel = "#"
stockholmpixel = "S"
stockholm = 0
land = 0

def mätSverige():
    global stockholm
    global land
    for i, pixel in enumerate(karta):
        if pixel == vattenpixel:
            continue
        elif pixel == stockholmpixel:
            stockholm += 1
            continue
        elif karta[i-3] == stockholmpixel and karta[i-2] == landpixel and karta[i-1] == vattenpixel:
            continue
        else:
            land += 1
            continue
    print(f"Antal landpixlar i Sveriges fastland är {land} stycken, {land + stockholm} om Stockholm räknas som land")

mätSverige()