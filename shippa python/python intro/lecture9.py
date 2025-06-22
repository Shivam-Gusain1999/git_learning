class students :
    def __init__(self, name, marks, subjects):
        self.name = name
        self.marks = marks
        self.subjects = subjects
        print("adding new data in a database")


    def dataa(self):
        print("welcome students", self.name)
    def show_details(self):
     print(f"name : {self.name}, marks : {self.marks}, subjects : {self.subjects}")

    def averagee(self):
        print("welcome students", self.marks)   
        


student1 = students("shivam", 98, "maths")
student2 = students("karan", 87, "physics")
student3 = students("arjun", 75, "english")
student1.dataa()
student2.dataa()
student3.dataa()

student1.show_details()
student2.show_details()
student3.show_details()

student1.averagee()
student2.averagee()
student3.averagee()

