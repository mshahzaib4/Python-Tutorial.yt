class First:
    def __init__(self):
        self.num1 = 100

    def display1(self):
        print("Num1 =", self.num1)


class Second(First):
    def __init__(self):
        super().__init__()
        self.num2 = 200

    def display2(self):
        print("Num2 =", self.num2)


class Third(Second):
    def __init__(self):
        super().__init__()
        self.num3 = 300

    def display3(self):
        print("Num3 =", self.num3)


def main():
    obj1 = Third()
    obj1.display1()
    obj1.display2()
    obj1.display3()


if __name__ == "__main__":
    main()
