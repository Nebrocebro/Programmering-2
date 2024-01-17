from datetime import datetime, timedelta

nu = datetime.now()

minutes_to_add = 1000
speed = 1
while minutes_to_add > 0:
    interval = timedelta(minutes=min(minutes_to_add, speed))
    nu += interval
    print("nu:", nu)
    minutes_to_add -= interval.total_seconds() // 60

print("Datum och tid efter 10^100 minuter:", nu)