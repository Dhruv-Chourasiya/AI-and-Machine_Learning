#Strings in Python
name="Dhruv"
friend="harry"
anotherfriend="raju"
print("Hello, " +name)
print(friend + " said i wanna eat apple")
apple="i wanna eat apple"
print(apple)
banana='''

i
wanna 
eat 
banana
triple single or double quote can used to multi lines string
'''
print(banana)
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5]) this will throws an error
for character in name:
    print(character)
for character in apple:
    print(character)


#String Slicing and Operations on python
name="Dhruv,Shubham"
print(name[0:1])
print(name[0:5])
print(name[5:6])
print(name[4:8])
print(name[3:10])
print(name[8:11])
print(name[2:12])
print(name[-5:12])
print(len(name))
len1=len(name)
print("mango is a ",len1," length word.")
# Quick quiz:
nm="harry" 
print(nm[-4:-2])



#Meathods of String in  Python
a="!!!DHRuv!! Harry !!!!"
print(len(a))
print(a.upper())
print(a.lower())
print("Strings are immutables")
print(a.isalpha())
print(a.islower())
print(a.isupper())
print(a.isnumeric())
print(a.isprintable())
print(a.isspace())
print(a.rstrip("!"))
print(a.replace("DHRuv","Harry"))
print(a.split(" "))
print(a.center(50))
print(a.count("!"))
print(a.find("R"))
print(a.index("Ha"))
print(a.swapcase)


# If else Statement in  Python
a=int(input("Enter your age:"))
print("Your age is:",a)
if(a>18):

   print("You can Drive")

else:
    print("You cant Drive!")
budget=200
appleprice=340
if(appleprice>=budget):
 print("You can not buy apple")
elif(appleprice<=budget):
 print("you can buy apples")



# Good Morning Sir
import time
t=time.strftime('%H:%M:%S')
hour=int(time.strftime('%H'))
print(hour)

if(hour>=0 and hour<12):
    print("GOOD MORNING SIR...")
elif(hour>=12 and hour<17):
    print("GOOD AFTERNOON SIR...")  
elif(hour>=17 and hour<0):
    print("GOOD NIGHT SIR...")      


#Match Case in Python
x=int(input("Enter the value from 0 to 5 X: "))
match x:
    case 0:
        print("X is 0")
    case 1:
        print("X is 1")
    case 2:
        print("X is 2")
    case 3:
        print("X is 3")
    case 4:
        print("X is 4")
    case 5:
        print("X is 5")                    
    case _ if x>5:
        print("X is not in the list")    



#For Loops in python
# name="Dhruv"
# for i in name:
#     print(i,end=", ")
# colors=["Red","orange","black","yellow"] 
# for color in colors:
#     print(color)   
# for i in color:
#     print(i)    

for k in range(5):
    print(k+1)
# for k in range(1,20001):
#     print(k)
for k in range(1,20,3):
    print(k)    



#while-loops in Python
# i=int(input("enter the number:"))
# while(i<=38):
#     i=int(input("Enter the Number: "))
#     print(i)
#     i=i+1
# print("Done with the loop")
count=5
while(count>0):
    print(count)
    count=count-1
else:
    print("I am inside else")    



#Break and continue in Python
# for i in range(12):
#     print("5 X ",i+1,"=",5 *(i+1))
#     if(i==10):
#         break
# print("LOOP KO CHOD KAR NIKAL GAYA")    
# for i in range(12):
#     if(i==10):
#         print("Skip the iteration")
#         continue
#     print("5 X", i,"=", 5*i)
i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break




#Functions in Pyhton
def calculateGmean(a,b):
    mean=(a+b)/(a*b)
    print(mean)

def greaternumber(a,b):
    if(a>b):
        print("First number is Greater")
    else:
        print("Second number is greater")    
def islesser(a,b):
    if(a<b):
        print("First number is smaller")
    else:
        print("Second number is smaller")    
a=9
b=8
greaternumber(a,b)
islesser(a,b)
# if(a>b):
#     print("First number is greater")
# else:
#     print("Second number is greater")    
calculateGmean(a,b)
# gmean= (a*b)/(a+b)
# print(gmean)
c=8
d=9
greaternumber(c,d)
islesser(c,d)
# if(c>d):
#     print("C is greater than D")
# else:
#     print("D is Greater than C")    

calculateGmean(c,d)
# gmean1=(c*d)/(c+d)
# print(gmean1)