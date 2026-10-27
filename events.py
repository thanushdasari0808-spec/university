# Campus Event Financial Planning

venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost per participant: "))
transport = float(input("Enter transport cost: "))
certificate = float(input("Enter certificate cost per participant: "))

participants = int(input("Enter expected participants: "))
fee = float(input("Enter registration fee per participant: "))
sponsor = float(input("Enter sponsorship amount: "))

# Calculate costs
fixed_cost = venue + equipment + transport
variable_cost = (catering + certificate) * participants
total_cost = fixed_cost + variable_cost

income = participants * fee + sponsor
shortfall = max(0, total_cost - income)

# Minimum registrations to break even
if fee > catering + certificate:
    minimum = max(0, int((fixed_cost - sponsor) /
                         (fee - catering - certificate)) + 1)
else:
    minimum = 0 if sponsor >= fixed_cost else -1

# Display results
print("\n--- Event Financial Report ---")
print("Fixed costs: Rs.", fixed_cost)
print("Variable costs: Rs.", variable_cost)
print("Total cost: Rs.", total_cost)
print("Participant contributions: Rs.", participants * fee)
print("Sponsorship: Rs.", sponsor)
print("Sponsorship shortfall: Rs.", shortfall)
print("Total income: Rs.", income)

if minimum == -1:
    print("Break-even is not possible with this registration fee.")
else:
    print("Minimum registrations to break even:", minimum)

if income >= total_cost:
    print("Event is financially successful.")
else:
    print("Event has a financial loss of Rs.", round(total_cost - income, 2))
