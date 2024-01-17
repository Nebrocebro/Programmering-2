def badstrand():
    köpta_tomter = 0
    tomt_budget = input("Skriv antalet tomter och Majas budget: ").split()
    for j in range(0, len(tomt_budget)):
        tomt_budget[j] = int(tomt_budget[j])
    tomt_priser = input("Skriv tomternas priser: ").split()
    for k in range(0, len(tomt_priser)):
        tomt_priser[k] = int(tomt_priser[k])
    majas_budget = tomt_budget[1]
    if tomt_budget[0] > len(tomt_priser):
        print("Skriv mindre än eller lika många tomtpriser som antalet tomter")
    elif tomt_budget[0] <= len(tomt_priser):
        for i in range(0, len(tomt_priser)):
            if majas_budget >= tomt_priser[i]:
                majas_budget -= tomt_priser[i]
                köpta_tomter += 1
            else:
                print("Antalet köpta tomter är: " + köpta_tomter)
                break


badstrand()
