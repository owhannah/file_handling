def write_to_file(lines):
    # Open the file in write mode
    with open("mylife.txt", "w") as file:
        # Write each line from the list to the file
        for line in lines:
            file.write(line + "\n")

# Example usage:
lines_to_write = [
    "Once upon a time, there was a little girl named Hannah.",
    "She lived at Valenzuela City.",
    "Every day, she is dreaming for a drifting car.",
    "She loves watching car drifting and racing."
]

write_to_file(lines_to_write)