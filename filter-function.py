# This will take all items in the iterable object and pass into a compatible function
print("------1------")
w_list = ["mango", "apple", "chair", "orange"]
print(w_list)


def _keep_if_len_greater_5(p_list):
    return len(p_list) > 5


w_new_list = filter(_keep_if_len_greater_5,w_list)
print(list(w_new_list))

print("------2------")
print("This can be done using lambda also, instead of custom function")
w_new_list = filter(lambda X: len(X) > 5, w_list)
print(list(w_new_list))
