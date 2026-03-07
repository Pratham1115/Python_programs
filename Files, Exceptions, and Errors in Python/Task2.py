# Write and Append Data to a File
 
# Write initial data to file
filename = "output.txt"
user_input = input("Enter data to write to file: ")

with open(filename, "w") as file:
    file.write(user_input + "\n")

# Append additional data
append_input = input("Enter data to append to file: ")

with open(filename, "a") as file:
    file.write(append_input + "\n")

# Read and display the final content
with open(filename, "r") as file:
    content = file.read()
    print("\nFile content:")
    print(content)
