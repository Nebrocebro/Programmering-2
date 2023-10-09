# class Class:
#     skola = 0
#     __namn = 0
#     __personnr = 0
#     def Student(self, __namn):
#         def get_namn(__namn):
        
#         def get_ålder(__personnr):
            
#             __personnr.splice()

# def double(i):
#     return i*2

# print(double(4))
# print(double("åtta"))
# print(double([1, 2]))

# x = 10
# try:
#     x/0
#     print("Allt gick bra.")
# except:
#     print("Något gick fel.")
# finally:
#     print("Nu är undantagshanteringen klar.")

# def funk(*args):
# 	return sum(args)/len(args)
# print(funk(2, 4, 6, 8))

# nbr_pieces = input("Ange input: ")
# nbr_pieces = nbr_pieces.split(" ")      # splitta per mellanslag
# output = ""
# try:
#     for i in range(6):
#         if i == 0 or i == 1:            # kung eller drottning
#             output += str(1-int(nbr_pieces[i]))
#         if i == 2 or i == 3 or i == 4:  # löpare, häst eller torn
#             output += str(2-int(nbr_pieces[i]))
#         if i == 5:                      # bönder
#             output += str(8-int(nbr_pieces[i]))
#         output += " "                       # lägg till mellanslag
#     print(output)
# except:
#     print("Fel input!")
