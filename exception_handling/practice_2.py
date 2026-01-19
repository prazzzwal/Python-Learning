def calc_avg():
    try:
        marks = float(input("Enter the total marks obtained: "))
        subjects = float(input("Enter the number of subjects: "))
        avg_marks = marks / subjects

    except ValueError:
        print("Invalid Input")

    except ZeroDivisionError:
        print("Number of subjects can't be zero")

    else:
        print(f"The average marks obtained is {avg_marks}")

    finally:
        print("Calculation Completed")


calc_avg()
