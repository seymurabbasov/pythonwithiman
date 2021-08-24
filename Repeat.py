"GITHUBNAN ELE"
"""1)input 2)+,-,* 3)modul 4)min 5)max 6)sqrt 7)inputnan kalkyatornan 8)if  9)while 10)for  11)copy 12)index
13)upper , lower 14)append 15)for"""""

a=input("name")
b=input("surname")
c=input("age")
print(" name " + a + " surname " + b + " age " + c)

a=2
b=4
c=6
print(a+b+c)
print(a-b-c)
print(a*b*c)

print(abs(-5))
print(min(3,4,5,2,1))
print(max(2,1,1,-6,-3,2))

a=input()
b=input()
c=input()
print(a+b+c)

if a in range (2,8):
    print(a)

a=2
while a<=10:
    a=a+1
    print(a)

a=["English","Chinese","Japanese","German"]
b=a.copy()
print(a)

h=["chinese","spanish"]
print(h.index("chinese"))

a="iman"
b="guluzade"
c="age"
d=(a.upper())
e=(b.upper())
f=(c.upper())
print(" name " + d + " surname " + e + " age " + f)


z=["Space X", "Amazon", "AliBaba"]
z.append("Apple")
print(z)
