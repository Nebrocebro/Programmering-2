# Du är en sångare med en raspig hals som du vill få undersökt, vet inte hur länge du kan säga aah
# Två rader av input, första kollar hur länge du kan säga aaah den dagen
# Och andra kollar hur långt av ett aah doktorn behöver för att kunna diagnosticera dig
# Om rad 1 > rad 2 så printas "gå till doktorn", om rad 1 < rad 2 så printas "gå inte".
def shouldIGo():
    strength = ""
    num_of_a = int(input("Hur många a kan du göra? (i sifferform)"))
    for num_of_a in range(0, num_of_a):
        strength += "a"
    strength += "h"
    requirement = ""
    num_of_a_doc = int(input("Hur många a behöver läkaren? (i sifferform)"))
    for num_of_a_doc in range(0, num_of_a_doc):
        requirement += "a"
    requirement += "h"
    if len(strength) >= len(requirement):
        print("Gå till läkaren")
    else:
        print("Gå inte till läkaren")

shouldIGo()