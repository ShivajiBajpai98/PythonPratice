# Input the dimensions of the cuboid
length = float(input("Enter the length of the cuboid: "))
width = float(input("Enter the width of the cuboid: "))
height = float(input("Enter the height of the cuboid: "))

# Calculate the surface area of the cuboid
surface_area = 2 * (length * width + width * height + height * length)

# Calculate the volume of the cuboid
volume = length * width * height

# Display the results
print(f"The surface area of the cuboid is {surface_area}.")
print(f"The volume of the cuboid is {volume}.")
