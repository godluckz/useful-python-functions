print("------1------")
w_names = ["Jimmy", "Smith", "Ali", "Baraka"]
w_ages = [10, 9, 11, 12]
w_grades = [5, 4, 6]

print("=>Can manualy combine the result of the lists")
for idx in range(min(len(w_names), len(w_ages), len(w_grades))): #Have to look at minimum so that doest fail if data is not the same
    w_name = w_names[idx]
    w_age = w_ages[idx]
    w_grade = w_grades[idx]
    print(f"{idx+1}. {w_name} is {w_age} years old and in grade {w_grade}")

print("------2------")
print("=>Using Zip")

w_class_zip = list(zip(w_names,w_ages,w_grades))
print(w_class_zip)
for name, age, grade in w_class_zip:    
    print(f"{name} is {age} years old and in grade {grade}")


print("------3------")
print("=>Using Zip with Enumerage")
w_class_zip = list(enumerate(zip(w_names,w_ages,w_grades)))
for idx, students in w_class_zip:  
    print(f"{idx+1}. {students[0]} is {students[1]} years old and in grade {students[2]}")
