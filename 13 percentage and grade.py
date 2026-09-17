def calculate_grade(physics, chemistry, mathematics):
    total = physics + chemistry + mathematics
    percentage = total / 3
    print("Percentage =", percentage)
    if percentage >= 90:
        print("Grade A")
    elif percentage >= 80:
        print("Grade B")
    elif percentage >= 70:
        print("Grade C")
    elif percentage >= 60:
        print("Grade D")
    elif percentage >= 40:
        print("Grade E")
    else:
        print("Grade F")
physics = int(input("Enter Physics marks: "))
chemistry = int(input("Enter Chemistry marks: "))
mathematics = int(input("Enter Mathematics marks: "))
calculate_grade(physics, chemistry, mathematics)