def check_hemoglobin():
    sex = input("Enter your biological sex (male/female): ").lower()
    value = float(input("Enter your hemoglobin value (g/l): "))
    if sex == "female":
        if value < 117:
            print("Hemoglobin value is low.")
        elif value <= 155:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    elif sex == "male":
        if value < 134:
            print("Hemoglobin value is low.")
        elif value <= 167:
            print("Hemoglobin value is normal.")
        else:
            print("Hemoglobin value is high.")
    else:
        print("Invalid input for biological sex.")

check_hemoglobin()
