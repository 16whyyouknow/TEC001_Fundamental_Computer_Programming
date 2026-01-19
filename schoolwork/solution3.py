hours_worked = float(input("Enter your hours: "))
hourly_rate = float(input("Enter your rate: "))
if hours_worked > 40:
    total_pay = (hours_worked - 40) * (1.5 * hourly_rate) + 40 * hourly_rate
    print("Pay: ", total_pay)
else:
    print("Pay: ", float(hours_worked) * float(hourly_rate))
