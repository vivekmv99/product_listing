
myList = [ 15 , 20 , 50 , 16 , +1]
myInt = 5
newList = [x / myInt for x in myList]
print(f"{newList} result after dividing by 5")
result = [i / j for i, j in zip(newList, myList)]
print(f"{result} result")