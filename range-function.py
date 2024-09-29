print("-----1-----")
w_range = range(2,10) #Exclude last number.
print(w_range) # returns an iterator.

print("-----2-----")
w_rage_list = list(w_range) #Convert to a list.
print(w_rage_list)

print("-----3-----")
w_range_sep_every_2 = range(2,10,2) #start, stop, step - this will give even numbers excluding 10
print(list(w_range_sep_every_2))


print("-----4-----")
# Print in reverse
w_range = range(10 , -10, -2) #Exclude last number.
print(list(w_range))

