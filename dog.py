class Dog:
    def __init__(self, name):
        self.name = name
        self.trick_list = []

    def get_name(self):
        return self.name

    def sit(self):
        print(f"{self.name} sits.")
        self.trick_list.append("sit")

    def lay_down(self):
        print(f"{self.name} lays down.")
        self.trick_list.append("lay down")

    def write_python_program(self):
        print(f"{self.name} writes a Python program.")
        self.trick_list.append("write Python program")

    def print_trick_list(self):
        if not self.trick_list:
            print(f"{self.name} has not performed any tricks yet.")
        else:
            print(f"{self.name} has performed the following tricks:")
            for trick in self.trick_list:
                print(trick)

# Example usage:
dog1 = Dog("Spot")
dog1.sit()
dog1.lay_down()
dog1.write_python_program()
dog1.print_trick_list()

dog2 = Dog("Buddy")
dog2.sit()
dog2.write_python_program()
dog2.print_trick_list()
