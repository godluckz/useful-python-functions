#Note , do not use open direct as you will have to cose manually
#Use with open, that way close is implicitly done for you.

with open ("test_file.txt", "w+") as f:
    f.write("Hello there.\n")

with open ("test_file.txt", "a+") as f:
    f.write("Hope you are good\n")