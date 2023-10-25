class student:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display(self):
        print("name=",self.name)
        print("age=",self.age)
        print("grade=",self.grade)
print("Student1 Details:\n")
s1=student("Neymar","18","12")
s2=student("Messi","19","12")
print(s1.display(),"\n\n")
print("Student2 Details:\n")
print(s2.display())
