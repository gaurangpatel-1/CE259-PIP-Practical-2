from os import remove


set = {1,2,3,4,5}

remove = int(input("Enter the number you want to remove from the set: "))

set.remove(remove)

print(set)