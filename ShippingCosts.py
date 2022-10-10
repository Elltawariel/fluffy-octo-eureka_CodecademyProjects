weight = 41.5

# ground shipping

if weight <= 2:
  cost = weight * 1.50 + 20.0
  print(cost)
elif weight > 2 and weight <= 6:
  cost = weight * 3 + 20.0
  print(cost)
elif weight > 6 and weight <= 10:
  cost = weight * 4 + 20.0
  print(cost)
elif weight >= 10:
  cost = weight * 4.75 + 20.0
  print(cost)
else:
  print("Error")

# ground premium shipping
premium_cost = 125.00
print("Price of premium shipping:", premium_cost)

# drone shipping
if weight <= 2:
  cost = weight * 4.50
  print(cost)
elif weight > 2 and weight <= 6:
  cost = weight * 9.00
  print(cost)
elif weight > 6 and weight <= 10:
  cost = weight * 12.00
  print(cost)
elif weight >= 10:
  cost = weight * 14.25
  print(cost)
else:
  print("Error")
