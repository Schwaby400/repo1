import Function as f


for x in "banana":
    print(x)

fruits = ["apple", "banana", "cherry"]
for z in fruits:
    print(z)

numbers = [1, 2, 3, 4, 5]
for y in numbers:
    print(y)
    if y < 3:
        print("not enough")
    elif y == 3:
        print("enough")
    else:
        print("Enough or too much")
print ("initializing function")
w = f.add(1)
print(w)