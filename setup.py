import os

def file_generator():
    sheet = input("Input the number of the current sheet: ")
    number_of_exercises = int(input("Input the number of exercises: "))
    for i in range(number_of_exercises):
        with open("Exercise_" + str(i + 1) + ".tex", "w") as file:
            if i + 1 == 1:
                file.write("\section*{Sheet " + sheet + "}\n")
            file.write("\subsection*{Exercise " + str(i + 1) + "}")

def index_generator():
    dir_path = "."
    dirs = []
    for path in os.listdir(dir_path):
        current_path = os.path.join(dir_path, path)
        if os.path.isdir(current_path) and current_path != "./.git":
            dirs.append(current_path)
    dirs.sort()
    print(dirs)
    sheet = 1
    with open("main.tex", "a") as file:
        for path in dirs:
            count = 1
            print(path)
            for path in os.listdir(path):
                file_name, file_extension = os.path.splitext(os.path.join(dir_path, path))
                if file_extension == ".tex":
                    file.write("\include{./Sheet_" + str(sheet) + "/Exercise_" + str(count) + "}\n")
                    count += 1
            sheet += 1
                    


index_generator()