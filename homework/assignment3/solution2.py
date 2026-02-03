def inches_to_cm():
    while True:
        inches = float(input("Enter length in inches (negative to quit): "))
        if inches < 0:
            print("Program ended.")
            break
        centimeters = inches * 2.54
        print(f"{inches} inches = {centimeters} cm")

inches_to_cm()