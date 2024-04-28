class Student:
   def __init__(self, name=" Muhammad Shahzaib", marks=50):
      self.name = name
      self.marks = marks

s1 = Student()
s2 = Student("Yaqoob", 25)

print ("Name: {} marks: {}".format(s1.name, s2.marks))
print ("Name: {} marks: {}".format(s2.name, s2.marks))