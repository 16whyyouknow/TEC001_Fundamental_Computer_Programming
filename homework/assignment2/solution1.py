def check_zander():
    length = float(input("Enter the length of the zander in centimeters: "))
    if length < 42:
        difference = 42 - length
        print(f"Release the fish back into the lake. It is {difference:.2f} cm below the size limit.")
    else:
        print("The zander meets the size limit. You can keep it.")

check_zander()
