def fact(num):
    total = 1
    for i in range(1, num + 1):
        total = total * i
        yield total

for el in fact(10):
    print(el)
