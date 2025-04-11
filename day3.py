#function in Python
# def average(a=9,b=1):
#     print("the average is ", (a+b)/2)

# average(4,6)
# average()    
# average(1,5)
# average(5)
# average(b=9)
# def average1(c,d=8):#giving input of C is compulsory
#     print("The average is ",c+d+d)
# average1(c=9,d=21)


# def average2(*numbers):
#     # print(type(numbers))
#     sum=0
#     for i in numbers:
#         sum=sum + i
#     print("Average is: "sum/len(numbers))    


# average2(5,6)


def name(**name):
    print(type(name))
    print("Hello,",name["fname"],
          name["mname"],name["lname"])

name(mname="Buchan",lname="Barnese",fname="james")



#List In Python
# l=[3,4,10,"String",True]
# print(l)
# print(type(l))
# print(l[0])
# print(l[1])
# print(l[2])
# print(l[3])
# print(l[4])
# #print(l[5])
# print(l[-3])
# if 10 in l:
#     print("True")
# else:
#     print("False")    
# if "10" in l:
#     print("True")
# else:
#     print("False")    
# if "arry" in "string":
#     print("True")
# else:
#     print("False")    
# print(l)
# print(l[1:])
# print(l[1:-1])
# print(l[1:4])
# print(l[1: :2])
list=[i*i for i in range(10)]
print(list)
lst=[i*i for i in range(10) if i%2==0]
print(lst)


#List Meathods
l=[11,4,2,8,1]
print(l)
# l.append(6)
# print(l)
# l.sort(reverse=False)
# print(l)
# l.reverse()
# print(l)
# print((l.index(1)))
# print((l.count(1)))
# m=l
# m[0]=0
# l.insert(1,899)
# print(l)
m=[900,1000,1100]
l.extend(m)
print(l)
k=[l+m]
print("Concatination if L and M is:",k)



#Tuples in Python
tp=(1,3,5,7,8,"green",True)
print(type(tp))
#tp[0]=90
#this will show error because tuples are immutable
print(tp[0])
print(tp[1])
print(tp[2])
print(tp[3])
if 342 in tp:
    print("Yess this number is present in the numbers")
else:
    print("NO, this number is not present")    
tp = tp[2:4]    
print(tp)



#Meathod in Tuples
Countries=("Spain","russia","India","England")
print(Countries)
temp=list(Countries)
temp.append("germany")#add item
temp.pop(2)           #remove item
temp[2]="USA"         #update item
Countries=tuple(temp)
print(Countries)
cout2=("pak","ind","aus")
cout3=Countries+cout2
print(cout3)
t=(1,2,3,4,6,7,8,6,7,6,6,6)
res=t.count(6)
res1=t.index(6)
print("Count of 6 i tuple is:",res)



#Kaun Banega Crorepati
question=[
    "Who is the Prime Minister of India",
    "Which City is called as a Pink city",
    "Who is the tallest animal in the Jungle",
    "Who is the Richest man in India"
]
option_q1=["(1) Swami Vivekanand",
           "(2) Nathuram Godse",
           "(3) narendra Modi",
           "(4) Sardar Vallabhai Patel"
           ]
print("----------------------------------")
print("Welcome to Kaun Banega Crorepati")
print("----------------------------------")
print("You are given a easy questions by answering them you will get price according to questions")
print("----------------------------------------")
print("Question 1")
print("Question 1 "+question[0])
print(option_q1[0])
print(option_q1[1])
print(option_q1[2])
print(option_q1[3])
x=int(input("Choose Your Answer:"))
match x:
    case 1:
        print("Your Answer is wrong,Sorry You cant play further")
        exit()
    case 2:
        print("Your Answer is wrong,Sorry You cant play further")
        exit()
    case 3:
        print("Your answer is correct, congratulation you are moving to next Question")
    case 4:
        print("Your Answer is wrong,Sorry You cant play further")
        exit()
print("----------------------------------------")
print("Currenty You are winning $1000000")
print("----------------------------------------")
print("Question 2")
print("Question 2  "+question[1])  
option_q2=["(1) Jaipur","(2) Ahmedabad","(3) delhi","(4) Utter pradesh"]      
print(option_q2[0])
print(option_q2[1])
print(option_q2[2])
print(option_q2[3])
x=int(input("Choose Your Answer:"))
match x:
    case 1:
        print("Your answer is correct, congratulation you are moving to next Question")

    case 2:
        print("Your Answer is wrong,Sorry You cant play further")
        exit()
    case 3:
        print("Your Answer is wrong,Sorry You cant play further")
        exit()
    case 4:
        print("Your Answer is wrong,Sorry You cant play further")
        exit()
print("----------------------------------------")
print("Currenty You are winning $2000000")
print("----------------------------------------")
print("Question 3")
print("Question 3  "+question[2])
option_q3=["(1) Lion","(2) Monkey","(3) Elephant","(4) Giraffe"]
print(option_q3[0])
print(option_q3[1])
print(option_q3[2])
print(option_q3[3])
x=int(input("Choose Your Answer:"))
match x:
    case 1:
        print("Your Answer is wrong,Sorry You cant play further")
        exit()
    case 2:
        print("Your Answer is wrong,Sorry You cant play further")
        exit()
    case 3:
        print("Your Answer is wrong,Sorry You cant play further")
        exit()
    case 4:
        print("Your answer is correct, congratulation you are moving to next Question")
print("----------------------------------------")
print("Currenty You are winning $3000000")
print("----------------------------------------")  
print("Question 4")
print("Question 4  "+question[3])
option_q4=["(1) Gautam Adani","(2) Mukesh Ambani","(3) Shahrukh Khan","(4) Nirav Modi"]
print(option_q4[0])
print(option_q4[1])
print(option_q4[2])
print(option_q4[3])
x=int(input("Choose Your Answer:"))
match x:
    case 1:
        print("Your Answer is wrong,Sorry You cant play further")
        exit()
    case 2:
        print("Your answer is correct, congratulation you are moving to next Question")
        
    case 3:
        print("Your Answer is wrong,Sorry You cant play further")
        exit()
    case 4:
        print("Your Answer is wrong,Sorry You cant play further")
        exit()
print("----------------------------------------")
print("Currenty You are winning $4000000")
print("----------------------------------------") 
print("Congratulation, You have attempt all answer correctly now you are winning $10000000 in CASH")    



# Fstring in Python
letter="Hey my name is {} and i am from {}"
country="India"
name="Dhruv"
print(letter.format(name, country))
print(f"Hey my name is {name} and i am from {country}")



# DocString in Python
def square(n):
    '''Takes in a number n, returns the square of N'''
    print(n**2)
square(5)
print(square.__doc__)



# Recursion in Python
# factorial(7) = 7*6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(3) = 3*2*1
# factorial(0) = 1

# factorial(n) = n*factorial(n-1)
def factorial(n):
    if(n==0 or n==1):
       
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))
print(factorial(7))
print(factorial(5))
f0=0
f1=1
f2=f1+f0
# f(n)=f(n-1)+f(n_2)