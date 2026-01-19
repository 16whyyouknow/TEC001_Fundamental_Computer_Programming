def calculate_pay(hours_worked, hourly_rate):
    if hours_worked > 40:
        total_pay = (hours_worked - 40) * 1.5 * hourly_rate + 40 * hourly_rate
    else:
        total_pay = hours_worked * hourly_rate
    return total_pay

hours_worked = float(input("Enter your hours: "))
hourly_rate = float(input("Enter your rate: "))
print("Pay: ", calculate_pay(hours_worked, hourly_rate))
