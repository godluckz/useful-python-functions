# This function allows us to appy a function to every single item in an iterable object, e.g. list
print("------1------")
w_list = ["mango", "apple", "chair", "orange"]
print(w_list)

w_new_list = map(len, w_list)
print(list(w_new_list)) # you have to cast to list, else you will get object address

print("------2------")
print("=>Using lambda function with map.")
w_new_list_append = map(lambda X: X + "s", w_list) #append s on the list
print(list(w_new_list_append))

print("------3------")
print("=>Can use own function in place of lambda function with map.")
def _append_s(p_instr):
    return p_instr + 's'

w_new_list_append = map(_append_s, w_list) #append s on the list
print(list(w_new_list_append))
