# Input the exam scores
math_score = float(input("Enter your math score: "))
science_score = float(input("Enter your science score: "))

# Define the grading scale
passing_score = 50

# Determine the grade for math
if math_score >= passing_score:
    math_grade = "Pass"
else:
    math_grade = "Fail"

# Determine the grade for science
if science_score >= passing_score:
    science_grade = "Pass"
else:
    science_grade = "Fail"

# Display the grades
print(f"Math Grade: {math_grade}")
print(f"Science Grade: {science_grade}")
