x = 10
y = 100
print(x == y) #is the x & y equal
print(x > y)
print(x < y)
print(x >= y)
print(x >=y)
print(x != y) # is the x & y or not equal

print(not(100>150 or 100<150)) 

a = 'harsha'
b = 'harshavardhan'
print(not('v'in a) and ('d'in b)) 

a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
print( a & b)
print(a | b)
print(a ^ b)
print(a << 2)
print(b >>1)

a = 7
b = 18
print(not(a<b))

age1 = input("Enter your age: ")
if (age1 >= "18"):
    {
        print('your an adult')
    }
else:
    {
        print('You are a minor')
    }

name = input("Enter your name: ")
print("a" not in name )