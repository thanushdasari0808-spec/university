# Progressive Electricity Billing

months = int(input("Enter number of months: "))
bills = []

for i in range(months):
    print("\nMonth", i + 1)
    units = int(input("Enter electricity units: "))

    # Slab calculation
    if units <= 100:
        bill = units * 2
    elif units <= 200:
        bill = 100 * 2 + (units - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (units - 200) * 5

    fixed = 50
    surcharge = bill * 0.05
    rebate = 20 if units <= 100 else 0

    total = bill + fixed + surcharge - rebate
    bills.append(total)

    print("Total bill: Rs.", round(total, 2))

# Compare monthly bills
print("\nMonthly Bill Comparison")

for i in range(months):
    print("Month", i + 1, ": Rs.", round(bills[i], 2))

    if i > 0 and bills[i] > bills[i - 1] * 1.2:
        print("Warning: Unusual bill increase!")

print("Highest bill: Rs.", round(max(bills), 2))
print("Lowest bill: Rs.", round(min(bills), 2))
