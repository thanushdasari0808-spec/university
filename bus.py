# Bus Passenger Occupancy Simulation

capacity = int(input("Enter bus capacity: "))
stops = int(input("Enter number of stops: "))

passengers = 0

for i in range(stops):
    print("\nStop", i + 1)

    boarding = int(input("Enter boarding passengers: "))
    alighting = int(input("Enter alighting passengers: "))

    if boarding < 0 or alighting < 0 or alighting > passengers:
        print("Invalid passenger count!")
        continue

    passengers = passengers - alighting + boarding

    print("Passengers in bus:", passengers)

    if passengers > capacity:
        print("Warning: Bus capacity exceeded!")
    else:
        print("Occupancy:", round(passengers / capacity * 100, 2), "%")

print("\nFinal passengers:", passengers)
