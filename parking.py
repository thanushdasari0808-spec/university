from datetime import datetime

print("1. Bike")
print("2. Car")
print("3. Bus")

vehicle = int(input("Enter vehicle type (1-3): "))
entry = input("Enter entry time (HH:MM): ")
exit_time = input("Enter exit time (HH:MM): ")

try:
    start = datetime.strptime(entry, "%H:%M")
    end = datetime.strptime(exit_time, "%H:%M")

    if vehicle not in [1, 2, 3]:
        print("Invalid vehicle type")

    else:
        if end < start:
            end += __import__("datetime").timedelta(days=1)

        minutes = int((end - start).total_seconds() / 60)
        hours = max(1, (minutes + 59) // 60)

        rates = {1: 10, 2: 20, 3: 50}
        daily_limit = {1: 100, 2: 200, 3: 500}

        days = (hours + 23) // 24
        fee = min(hours * rates[vehicle],
                  days * daily_limit[vehicle])

        overnight = 30 if end.date() != start.date() else 0
        penalty = 100 if hours > 48 else 0

        total = fee + overnight + penalty

        print("Parking duration:", hours, "hours")
        print("Parking fee: Rs.", fee)
        print("Overnight charge: Rs.", overnight)
        print("Penalty: Rs.", penalty)
        print("Total parking fee: Rs.", total)

except ValueError:
    print("Invalid time! Enter time in HH:MM format.")
