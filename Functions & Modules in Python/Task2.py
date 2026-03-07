
#Using the Math Module for Calculations

import math
# Get user input
number = float(input("Enter a number: "))

# Calculate square root
sqrt_result = math.sqrt(number)

# Calculate natural logarithm
log_result = math.log(number)

# Calculate sine (input in radians)
sin_result = math.sin(number)

# Display results
print(f"Square root of {number}: {sqrt_result}")
print(f"Natural logarithm of {number}: {log_result}")
print(f"Sine of {number} radians: {sin_result}")