class Person:
  def __init__(self,name,age,gender):
    self.name=name
    self.age=age
    self.gender=gender
  def greet(self):
    print("Hello, I am {}.".format(self.name))
  def introduce(self):
    print("My name is {} and I am {} years old.".format(self.name, self.age))
class Student(Person):
  def __init__(self, name, age, gender, course):
    super().__init__(name, age, gender)
    self.course = course
  def study(self):
    print("I am studying {}.".format(self.course))
class Teacher(Person):
  def __init__(self, name, age, gender, subject):
    super().__init__(name, age, gender)
    self.subject = subject
  def teach(self):
    print("I am teaching {}.".format(self.subject))
if __name__ == "__main__":
  person = Person("John Doe", 30, "male")
  person.greet()
  person.introduce()
  student = Student("Jane Doe", 25, "female", "Computer Science")
  student.greet()
  student.introduce()
  student.study()
  teacher = Teacher("Mr. Smith", 40, "male", "Math")
  teacher.greet()
  teacher.introduce()
  teacher.teach()
