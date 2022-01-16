from statistics import mode

list = [1,2,7,8,1,4,9,11,26,28,25,29,25,14,16,17,14,25,14]
print(f"Most common element is {mode(list)} for {list.count(mode(list))} times")

tuple = (2,9,10,15,16,41,25,14,10,15,1,2,15,4,9,36,15,14,10)
print(f"Most common element is {mode(tuple)} for {tuple.count(mode(tuple))} times")
