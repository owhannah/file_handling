def process_numbers_file():
    # Read numbers from integers.txt
    with open("integers.txt", "r") as file:
        numbers = [int(num) for num in file.read().split()]

    # Separate even and odd numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    # Calculate squares of even numbers and cubes of odd numbers
    squares = [num ** 2 for num in even_numbers]
    cubes = [num ** 3 for num in odd_numbers]

    # Write squares to double.txt
    with open("double.txt", "w") as double_file:
        for square in squares:
            double_file.write(str(square) + "\n")

    # Write cubes to triple.txt
    with open("triple.txt", "w") as triple_file:
        for cube in cubes:
            triple_file.write(str(cube) + "\n")

# Call the method to execute
process_numbers_file()
