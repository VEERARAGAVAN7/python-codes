#__init__ Method

class Users:

    def __init__(self,name):
        print("\n What's your name?")
        self.name=name
    def printall(self):
        print("My name is : ",self.name)

o= Users("Veeraragavan")
o.printall()
print(o.__dict__)

v=Users("Gnanambal")
v.printall()
print(v.__dict__)

print("--------------------------------------------------------------------------")
print("\n")

class family():

    def __init__(self,name,age,gender,DOB,qualify):
        print("sumbit your details On govt portal!")
        self.name=name
        self.age=age
        self.gender=gender
        self.DOB=DOB
        self.quality=qualify


    def get_data(self):
        print("Name             :",self.name)
        print("Age              :" ,self.age)
        print("Gender           :", self.gender)
        print("Date Of Birth    :", self.DOB)
        print("Qualification    :",self.quality)

v=family("veeraragavan Gnanambal",19,'m',"May 9th 2003","Engineer")
v.get_data()
print("\n")
v1=family("karthika",21,"F","dec 10th 2001","bsc.nutrition")
v1.get_data()