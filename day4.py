#Introduction of Set
s={2,4,6,8,10,4}
print(s)
info={"carla",19,False,5.9,19}
print(info)
# dhruv={} This is not empty set, is you run this it will show distionary
dhruv=set()
print(type(dhruv))

for value in info:
    print(value)
#Set doesn't follow order    


#Meathods in Sets
s1={1,2,5,7}
s2={5,7,9}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)
c1={"tokyo","japan","germany","atlanta"}
c2={"pakistan","punjab","japan","tokyo"}
c3=c1.union(c2)
print(c3)
c4=c1.intersection(c2)
print(c4)
c5=c1.symmetric_difference(c2)
print(c5)
c6=c1.difference(c2)
print(c6)
c7=c2.difference(c1)
print(c7)
print(c1.isdisjoint(c2))
print(c1.issubset(c2))
print(c1.issuperset(c2))
c1.add("Jaipur")
c2.remove("punjab")
print(c1)
print(c2)
item=c1.pop
print(c1)


#Distionary in Python
dic={
    "Harry":"Human being",
    "spoon":"object",
    "Google.com":"Website"
}
print(dic["Harry"])
emp={
    344:"Harry",
    343:"Dhruv",
    345:"Rahul",
    3456:"zakir"
}
print(emp[344])
info={'name':'Dhruv','age':'20','Eligible':True}
print(info)
print(info['name'])
print(info.keys())

for key in info.keys():
    print(info[key])



#Distionary Meathods in Python
ep1={122:45,123:89,124:69,125:79}
ep2={222:67,565:90}
ep1.update(ep2)
print(ep1)
# empt ={}
# print{empt}
ep1.pop(122)
ep1.popitem()
print(ep1)



#For loop With else in Python
for i in range(5):
    print(5)
else:
    print("sorry no i")    
for i in range(6):
    print(i)
    if i==4:
        break  
else:
    print("sorry no i")      


y=0
while y<7:
    print(y)
    y=y+1
else:
    print("sorry no y")       



#Error Handling In Python
a=input("enter the number:")
print(f"multiplaction table of {a} is:")
try:
 for i in range(1,11):
    print(f"{int(a)}x{i}={int(a)*i}")
except Exception as e:
  print("Invalide input,enter the number")    
print("Some line of code")
print("End of program")
try:
  num=int(input("Enter an integer: "))
except ValueError:
  print("Number entered is not an integer.")
except IndexError:
  print("Index Error")    



  #Finally In Pyhton
# try:
#     l=[1,3,5,6,890]
#     i=int(input("enter the number: "))
#     print(l[i])
# except:
#     print("Some error occured:")    
# finally:
#     print("I will always executed.")    
def func():
    try:
        l=[1,2,3,4]
        i=(int(input("Enter the Number:"))) 
        print(l[i])
        return 1
    except:
        print("Some Error is occured")
        return 0       
    finally:
        print("I always executed...")
x=func()
print(x)        



#Raising Custom Error In Python
a=int(input("Enter any number between 5 and 9: "))
if(a<5 or a>9):
    raise ValueError("Value should be between 5 and 9")



#Encryption and decryption of the plaintext in which,if word contain atleast 3 characters than remove first character of the word and append it at the last character position 
#else reverse the string


#encryption
pt=input("Enter a Word=")
if len(pt)>3:
    pt1=pt[1:]+pt[0]
    print("Encrypted word is ",pt1)
else:
    pt2=pt[::-1]
    print("Encrypted word is ",pt2) 


#decryption
ct=input("Enter the cyphertext=")
if len(pt)<3:
    ct1=ct[::-1]
    print("Your plaintext is:",ct1)
else:
    # ct2=pt1[::-1]
    pt=ct[-1]+ct[:-1]
    print("Your plaintext is:",pt)
