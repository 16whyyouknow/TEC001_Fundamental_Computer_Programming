import math

def unit_price(diameter, price):
    radius = diameter / 2
    area_cm2 = math.pi * (radius ** 2)
    area_m2 = area_cm2 / 10000
    return price / area_m2

d1 = float(input("Enter diameter of the first pizza (cm): "))
p1 = float(input("Enter price of the first pizza (USD): "))
d2 = float(input("Enter diameter of the second pizza (cm): "))
p2 = float(input("Enter price of the second pizza (USD): "))

u1 = unit_price(d1, p1)
u2 = unit_price(d2, p2)

print(f"First pizza unit price: {u1:.2f} USD/m²")
print(f"Second pizza unit price: {u2:.2f} USD/m²")

if u1 < u2:
    print("The first pizza provides better value for money.")
elif u2 < u1:
    print("The second pizza provides better value for money.")
else:
    print("Both pizzas provide the same value for money.")

