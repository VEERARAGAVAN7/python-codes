"""
#basic Oops method/class method

class student():
    name    = "Veeraragavan"
    age     = 20
    gender  = 'M'
    college = "Svct"
    dept    = "ECE"
    CGPA    = 8.0

print(student.name) # dot.notation method

print(getattr(student,'age')) # getattr method

setattr(student,'character','good') # setattr method
print(student.character)

student.knowledge='top calss' # creating data using dot notaion
print(student.knowledge)

delattr(student,"age") # delete data using (delattr) method
print(student.age)  #just refrence ku print pannen
"""
print("----------------------------------------------------------------------------")
#instance mehtod

class student():
    name="veeraragavan"
    dept="ECE"
    clg="Svct"

    def detail(self,age):
        print("NAME          :",student.name)
        print("DEPARTMENT    :", student.dept)
        print("COLLEGE       :", student.clg)
        print("AGE           :", age)

v=student()
v.detail(22)

print("\n")
student.detail(v,19)

print("\n")

#getting output using getattr method
print(getattr(student,'name'))

print("\n")

#set value using setattr method
setattr(student,'knowledge','top class')
print(student.knowledge)

print("----------------------------------------------------------------------------")


