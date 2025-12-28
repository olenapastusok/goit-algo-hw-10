import pulp

model = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

lemonade = pulp.LpVariable('Lemonade', lowBound=0, cat='Integer')
fruit_juice = pulp.LpVariable('Fruit_Juice', lowBound=0, cat='Integer')

model += lemonade + fruit_juice, "Total_Production"


# Вода: 2*L + 1*J <= 100
model += 2 * lemonade + 1 * fruit_juice <= 100, "Water_Constraint"

# Цукор: 1*L <= 50
model += 1 * lemonade <= 50, "Sugar_Constraint"

# Лимонний сік: 1*L <= 30
model += 1 * lemonade <= 30, "Lemon_Juice_Constraint"

# Фруктове пюре: 2*J <= 40
model += 2 * fruit_juice <= 40, "Fruit_Puree_Constraint"

# 5. Розв'язання задачі
model.solve()

print(f"Solution status: {pulp.LpStatus[model.status]}")
print(f"Lemonade: {lemonade.varValue} units.")
print(f"Fruit Juice: {fruit_juice.varValue} units.")
print(f"Total products: {pulp.value(model.objective)} units.")