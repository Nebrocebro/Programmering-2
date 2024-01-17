def statueMan(n):
    printers = 1
    statuesPrinted = 0
    days = 0

    while statuesPrinted < n:
        statuesToday = printers

        if statuesToday + statuesPrinted < n:
            printers += 1

        statuesPrinted += statuesToday
        days += 1
    return days
n = int(input())
result = statueMan(n)
print(result)