
#property meethod
class person():

    def __init__(self,employee,company,salary,position):
        self.employee=employee
        self.company=company
        self.salary=salary
        self.position=position
    @property
    def data(self):
        return self.employee+"\tiam working in \t" + self.company+ "\t and his salary is above\t" + self.salary + "\t and my position is\t" +self.position

v=person("veeraragavan","google","30 LPA","senoir software engineer")
print(v.data)

print(v.employee)
print(v.company)
print(v.salary)
print(v.position)