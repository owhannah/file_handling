def main():
    # Read numbers from number.txt
    with open ("number.txt", "r") as file:
        numbers = [int(num) for num in file.read().split()]

    # Separate even and odd numbers
    even_numbers = [num for num in numbers if num % 2 == 0]
    odd_numbers = [num for num in numbers if num % 2 != 0]

    # Write even numbers to even.txt
    with open("even.txt", "w") as even_file:
        for num in even_numbers:
            even_file.write(str(num) + "\n")

    # Write odd numbers to odd.txt
    with open("odd.txt", "w") as odd_file:
        for num in odd_numbers:
            odd_file.write(str(num) + "\n")

if __name__ == "__main__":
    main()

