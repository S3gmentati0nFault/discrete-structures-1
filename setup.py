sheet = input("Input the number of the current sheet: ")
number_of_exercises = int(input("Input the number of exercises: "))
for i in range(number_of_exercises):
    with open("Exercise_" + str(i + 1) + ".tex", "w") as file:
        if i + 1 == 1:
            file.write("\section*{Sheet " + sheet + "}\n")
        file.write("\subsection*{Exercise " + str(i + 1) + "}")
