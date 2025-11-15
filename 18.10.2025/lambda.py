# zwykła funkcja
def avg(x,y):
    return (x + y) / 2

# funkcja lambda
avg2 = lambda x, y: (x + y) / 2

print(avg(10, 20))
print(avg2(10, 20))
# zwykła funkcja
def sqrList1(numbers):
    resList = []
    for el in numbers:
        resList.append(el**2)
    return resList

#lambda
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqrList2 = list(map(lambda el: el**2, numbers))

print(sqrList1(numbers))
print(sqrList2)