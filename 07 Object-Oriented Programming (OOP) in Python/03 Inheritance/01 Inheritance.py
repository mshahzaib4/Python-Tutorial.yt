class Data_Entry:
    def __init__(self):
        self.id = None
        self.id2 = None
        self.marks = None
        self.marks2 = None
        self.phone_number = None
        self.phone_number2 = None

    def input1(self):
        self.id = int(input("Enter ID="))
        self.marks = int(input("Enter Marks="))
        self.phone_number = int(input("Enter Phone Number="))

    def show(self):
        print("\n ID IS =", self.id)
        print(" Marks IS =", self.marks)
        print(" Phone Number IS =", self.phone_number)


class UpdateData(Data_Entry):
    def input2(self):
        self.id2 = int(input("\nEnter ID2="))
        self.marks2 = int(input("Enter Marks2="))
        self.phone_number2 = int(input("Enter Phone Number2="))
        self.id = self.id2
        self.marks = self.marks2
        self.phone_number = self.phone_number2


obj1 = UpdateData()
obj1.input1()
print("\nUpdate Object\n")
obj1.input2()
obj1.show()
