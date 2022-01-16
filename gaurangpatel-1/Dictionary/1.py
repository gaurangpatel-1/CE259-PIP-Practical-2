dictionary = {
    "name":"Gaurang",
    "age":"19",
    "roll_no":"20CE081",
    "collage" : "CHARUSAT"
}

key = input("Enter the key you want to check: ")

if key in dictionary.keys():
    print("Key is present in the given dictionary")
else:
    print("Key is not there")
