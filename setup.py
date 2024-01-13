import os

def file_generator(sheet, number_of_exercises):
    os.mkdir("Sheet_" + sheet)
    for i in range(number_of_exercises):
        with open("./Sheet_" + sheet + "/Exercise_" + str(i + 1) + ".tex", "w") as file:
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
    with open("Exercises.tex", "a") as file:
        for path in dirs:
            count = 1
            print(path)
            for path in os.listdir(path):
                file_name, file_extension = os.path.splitext(os.path.join(dir_path, path))
                if file_extension == ".tex":
                    file.write("\include{./Sheet_" + str(sheet) + "/Exercise_" + str(count) + "}\n")
                    count += 1
            sheet += 1

def clean_up():
    dir_path = "."

    for path in os.listdir(dir_path):
        current_path = os.path.join(dir_path, path)
        if os.path.isdir(current_path):
            for path in os.listdir(current_path):
                file_name, file_extention = os.path.splitext(os.path.join(current_path, path))
                if file_extention == ".aux":
                    os.remove(os.path.join(current_path, path))
        else:
            file_name, file_extention = os.path.splitext(current_path)
            if file_extention == ".dvi" or file_extention == ".synctex.gz":
                os.remove(current_path)
                    
print("Input a number for the option you are interested in:")
print("\t- 1 - Clean the directory removing any compilation files")
print("\t- 2 - Generate a new directory containing the necessary files to start working!")
print("\t- 3 - Regenerate the index for the main.tex file")

i = 0

while i < 1 or i > 3:
    i = int(input("Input a choice: "))
    match i:
        case 1:
            print("cleaning...")
            clean_up()

        case 2:
            sheet = input("Input the number of the current sheet: ")
            number_of_exercises = int(input("Input the number of exercises: "))
            print("generating the new directory...")
            file_generator(sheet, number_of_exercises)
        
        case 3:
            print("regenerating the index...")
            index_generator()