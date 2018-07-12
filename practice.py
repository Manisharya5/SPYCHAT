# class student :
    # name = 'Tommy'
# s1 = student()
# print(s1.name)
#=====================output = Tommy==============

#class student :
#     name = " "
#     roll = 0
#     collage = " "
#     year = 0

#s1 = student()

 #s1.name = input("enter name:")
 #s1.roll = int(input('enter the roll:'))
 #s1.year = int(input("enter the year:"))
 #s1.collage = input("enter collage:")
 #print(s1.name,s1.roll,s1.year,s1.collage)

#=====print (name,roll,year,collage) of class student====================

#====================================================================================

#class Student :
#    name = " "
#    roll = 0
#    year = 0
#    collage = " "
#    def dispall(self):          #defination of method inside class to print attribute
#         print(self.name)
#         print(self.roll)
#         print(self.year)
#         print(self.collage)

#s1 = student()                 #definating the object (instantiation of class)

#s1.name = input("enter name:")
#s1.roll = int(input('enter the roll:'))
#s1.year = int(input("enter the year:"))
#s1.collage = input("enter collage:")
#s1.dispall()                            #call s1 object

#======print (name,roll,year,collage) of class student by creating method in class============

#===============Class member and object member examples========================

#class Sample:
    #def __init__(self, a,b,c):
        #self.v1 = a
        #self.v2 = b
        #self.v3 = c

#s1 = Sample(10,"ram",3.20)         #======constructor decleration===============
#print(s1.v1)
#print(s1.v2)
#print(s1.v3)                      #output ( a=10,b=ram,c=3.20)

#==============class employe====================

#class employe:
#    total_emp = 0    #=============class member==========
#    def __init__(self,name,salary):
#        self.name = name
#        self.salary = salary
#        employe.total_emp = employe.total_emp + 1

#    def disp_employe(self):
#        print("employe name is %s and salary is %d" %(self.name,self.salary))

#    def count_total (self):
#        print("total employe are %d" %(employe.total_emp))

#e1 = employe("messi",24000)
#e1.disp_employe()
#e1.count_total()

#e2 = employe("ronaldo",30000)
#e2.disp_employe()
#e2.count_total()
#==============output=================#
#employe name messi and salary is 24000
#total employe are 1
#employe name ronaldo and salary is 30000
#total employe are 2

#e1.count_total()        #======output(2)===================

#===============================================================================

#============================[INHERITENCE]=====================================

#class Parent:
#    def __init__(self):
#        print("calling Parent constructor")
#    def ParentMethod(self):
#        print("calling Parent method")

#class Child(Parent):
#    def __init__(self):
#        print("calling Child constructor")
#    def ChildMethod(self):
#        print("calling Child method")

#p1 = Parent()
#p1.ParentMethod()

#c1 = Child()
#c1.ChildMethod()

#c1.ParentMethod()
#p1.ChildMethod()

#===============================================================================

#class Person:
#    def __init__(self,name,age):
#        self.name = name
#        self.age  = age
#        print("calling constructor")

#    def ShowName(self):
#        print(self.name)

#    def ShowAge(self):
#        print(self.age)

#class Student(Person):
#    def __init__(self,name,age,roll):
#        Person.__init__(self,name,age)          #super().__init__(self,name,age)
#        self.roll = roll
#        print("calling student constructor")

#    def getroll(self):
#        return self.roll

#p1 = Person("Roy",26)
#p1.ShowName()
#p1.ShowAge()

#S = Student("ram",22,1024)
#S.ShowName()
#S.ShowAge()
#print(S.getroll())

#    OUTPUT :
#            calling constructor
#            Roy
#            26
#            calling constructor
#            calling student constructor
#            ram
#            22
#            1024

#==================Stack immplementation in python==============================

#class Stack:
#    def __init__(self):
#        self.items = []

#    def isempty(self):
#        return self.items == []

#    def push (self,item):
#        self.items.append(item)

#    def pop(self):
#        return self.items.pop()

#    def size(self):
#        return len(self.items)

#s = Stack()
#s.push(10)               #pushing 10 in stack
#s.push(20)               #pushing 20 in stack
#print(s.items)           #print [10,20]
#print(s.pop())           #pop 20       stack =[10]
#s.push(30)
#s.push(40)               #[10,30,40]
#print(s.size())          #3

#============output============#
#[10, 20]
#20
#3

#===============================================================================

#def fact(n):
#    if n == 1:
#        return 1
#    else:
#        return n*fact(n-1)

#n= int(input("enter a number"))
#print("the factorial of %d is %d" %(n,fact(n)))

#===============================================================================

#def sum(list):
#    if len(list) == 1:
#        return list[0]
#    else:
#        return list[0] + sum[list[1:]]
#print(sum([10,20,30,40,50]))
