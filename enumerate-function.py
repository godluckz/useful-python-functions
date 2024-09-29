w_tasks = ["Study", "create ren user", "Adf", "Review code", "Attend Meetings", "Write Report/doc"]
print("------1------")
print("can use range.")

for index in range(len(w_tasks)):
    task = w_tasks[index]
    print(f"{index+1}. {task}")


print("------2------")
print("can use enumerate.")
print("------2a------")
print("Note; enumerate returns a tupple with index as the first falue")
print(list(enumerate(w_tasks)))
print("------2b------")
print("Now print results")
for index, task in enumerate(w_tasks):
    print(f"{index+1}. {task}")

