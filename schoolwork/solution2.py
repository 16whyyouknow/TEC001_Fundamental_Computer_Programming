def generate_spruce(height):
    print("A spruce is coming!")

    # print the tree
    i = 1
    while i <= height:
        spaces = height - i
        asterisks = 2 * i - 1
        print(" " * spaces + "*" * asterisks)
        i += 1

    # print the base
    print(" " * (height - 1) + "*")

generate_spruce(6)