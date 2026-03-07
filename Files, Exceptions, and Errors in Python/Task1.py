# Read a File and Handle Errors

try:
    with open('sample.txt', 'r') as file:
        for line in file:
            print(line.rstrip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found.")
except Exception as e:
    print(f"An error occurred: {e}")