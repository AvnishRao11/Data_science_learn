class Student:
    def __init__(self,name,age,number,blood_group):
        self.name=name
        self.age=age
        self.number=number
        self.blood_group=blood_group
    def show(self):
        print(f"hello your name is {self.name}\n your age is {self.age}\n your number is {self.number}\n your blood group is {self.blood_group}\n ")
obj=Student("avnish",21,8076555234,"A+")

obj.show()

