w_numbers = {2, 4, 6, 8, 10} #can pass list / tuple, as long as it is an iterable object
print("------1------")
w_sum = sum(w_numbers)
print(f"sum: {w_sum}")

print("------2------")
print("can add start value, and this will be added on the sum. default is 0")
print("Start with 10")
w_sum = sum(w_numbers, start=10)
print(f"sum: {w_sum}")

print("------2a-----")
print("Start with -10")
w_sum = sum(w_numbers, start=-10)
print(f"sum: {w_sum}")
