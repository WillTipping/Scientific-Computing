#gitbash
def f(data):
    list1 = []
    for i in range(0,len(data)):
        list1.append(data[i]**2)
    return list1

data = [2,3,1,-1]

x = f(data)

print(x)