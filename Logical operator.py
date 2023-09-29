# Using and Operator
# Input a number
number = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

# Using or Operator:

# Input age and student status
age = int(input("Enter your age: "))
is_student = input("Are you a student (yes/no): ").lower() == "yes"

# Check eligibility for a discount
if age <= 18 or is_student:
    print("You are eligible for a discount.")
else:
    print("You are not eligible for a discount.")


# Using not Operator
# Define the correct password
correct_password = "mysecretpassword"

# Input a password
entered_password = input("Enter your password: ")

# Check if the password is incorrect
if not entered_password == correct_password:
    print("Incorrect password. Access denied.")
else:
    print("Welcome! Access granted.")

