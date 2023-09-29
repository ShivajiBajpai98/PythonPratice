# Input distance in kilometers
kilometers = float(input("Enter distance in kilometers: "))

# Conversion factor: 1 kilometer = 0.621371 miles
conversion_factor = 0.621371

# Calculate the equivalent distance in miles
miles = kilometers * conversion_factor

# Display the result
print(f"{kilometers} kilometers is equal to {miles} miles.")
