w_numbers = {2, 4, -1, 3, 8, 1, 10} #can pass list / tuple, as long as it is an iterable object
print(f"numbers: {w_numbers}")

print("------1------")
w_sorted_numbers = sorted(w_numbers)
print(f"sorted: {w_sorted_numbers}")

print("------2------")
print("can reverse")
w_sorted_numbers = sorted(w_numbers, reverse=True)
print(f"sum: {w_sorted_numbers}")

print("------3------")
w_customers = [
    {"name":"Jimmy", "age":"20"},
    {"name":"Smith", "age":"50"},
    {"name":"Ali", "age":"18"},
    {"name":"Baraka", "age":"35"},

]

print("Using Key, to sort based on the function")
w_sorted_customers = sorted(w_customers, key=lambda customer: customer["age"])#can add reverse if needed.
print(f"sum: {w_sorted_customers}")

