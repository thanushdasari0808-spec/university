# Water Distribution Fairness Analysis

areas = ["Area A", "Area B", "Area C"]

demand = [1000, 800, 1200]

# Water supplied to each area over 3 days (in litres)
supply = [
    [800, 700, 900],
    [600, 750, 700],
    [1000, 900, 800]
]

shortages = []

for i in range(len(areas)):
    total_supply = sum(supply[i])
    total_demand = demand[i] * len(supply[i])
    shortage = total_demand - total_supply

    shortages.append(shortage)

    print("\nArea:", areas[i])
    print("Total Demand:", total_demand, "litres")
    print("Total Supply:", total_supply, "litres")
    print("Shortage:", max(0, shortage), "litres")

    percentage = (total_supply / total_demand) * 100
    print("Supply Percentage:", round(percentage, 2), "%")

# Identify most underserved area
index = shortages.index(max(shortages))

print("\nMost Underserved Area:", areas[index])
print("Highest Shortage:", shortages[index], "litres")

# Compare daily supply
print("\nDaily Water Supply Comparison:")
for day in range(3):
    print("Day", day + 1, end=": ")
    for i in range(len(areas)):
        print(areas[i], "=", supply[i][day], "litres", end=" | ")
    print()
