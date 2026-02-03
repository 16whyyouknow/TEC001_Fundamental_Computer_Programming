def min_max_numbers():
    numbers = []
    while True:
        entry = input("Enter a number (empty to quit): ")
        if entry == "":
            break
        try:
            num = float(entry)
            numbers.append(num)
        except ValueError:
            print("Invalid input, please enter a number.")

    if numbers:
        print("Smallest number:", min(numbers))
        print("Largest number:", max(numbers))
    else:
        print("No numbers were entered.")

min_max_numbers()
