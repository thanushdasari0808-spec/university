# Hospital Ward Occupancy Monitoring

wards = ["General", "ICU", "Emergency"]
capacity = [50, 20, 30]

# Occupancy for 3 wards over 4 days
occupancy = [
    [30, 40, 45, 55],
    [10, 15, 18, 22],
    [20, 25, 28, 30]
]

for i in range(len(wards)):
    print("\nWard:", wards[i])

    for j in range(len(occupancy[i])):
        beds = occupancy[i][j]
        utilization = (beds / capacity[i]) * 100

        print("Day", j + 1, "Occupied:", beds,
              "Utilization:", round(utilization, 2), "%")

        if beds > capacity[i]:
            print("Warning: Capacity exceeded!")

# Peak-demand day
daily_total = [
    sum(occupancy[i][j] for i in range(len(wards)))
    for j in range(len(occupancy[0]))
]

peak = daily_total.index(max(daily_total))

print("\nDaily Total Occupancy:", daily_total)
print("Peak Demand: Day", peak + 1)
print("Maximum Occupied Beds:", daily_total[peak])
