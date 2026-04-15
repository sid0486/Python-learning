# PARENT CLASS :

class Car :
    def __init__(self,brand,model):
        self.brand = brand 
        self.model = model 

    def full_name(self):
        return f"{self.brand} {self.model}"

    def show(self):
        print("Car")

# SINGLE INHERITANCE:

class ElectricCar(Car):
    def __init__(self,brand,model,battery):
        Car.__init__(self,brand,model)
         # ❌ Avoid super() here because later multiple inheritance (HybridCar)
        # super() may follow MRO and go to wrong class (PetrolCar)
        
        # ✅ Direct call to parent (safe for multiple inheritance cases)
        self.battery = battery

    def full_name(self):
        # Method overriding (polymorphism)
        # Extending parent behavior
        return f"{self.brand} {self.model} {self.battery}"

    def is_expensive(self):
        return "Expensive Electric car "

# MULTILEVEL INHERITANCE:

class LuxuryElectricCar(ElectricCar):
    def __init__(self,brand,model,battery,features):
          # ✅ Safe to use super() (linear inheritance chain)
        super().__init__(brand,model,battery)

        self.features=features


# HIERARCHICAL INHERITANCE:
class PetrolCar(Car):
    def __init__(self,brand,model,fuel):
        # ❌ Avoid super() (same reason as ElectricCar)
        # Prevent MRO issues in HybridCar
        Car.__init__(self,brand,model)
        self.fuel = fuel
    
    def fuel_type(self):
        return "Petrol"


class DieselCar(Car):
    def __init__(self,brand,model,fuel):
    # ✅ Safe (no multiple inheritance involvement here)
        Car.__init__(self,brand,model)
        self.fuel = fuel

    def fuel_type(self):
        return "Diesel"


# DIMOND PROBLEM (MULTIPLE INHERITANCE)
class HybridCar(ElectricCar,PetrolCar):
    def __init__(self,brand,model,battery,fuel):
         # ❌ super() not used because:
        # it follows MRO → Hybrid → Electric → Petrol → car
        # and may skip or mis-handle required arguments

        # ✅ Manually calling both constructors
        # because each parent has different responsibility
        ElectricCar.__init__(self,brand,model,battery)
        PetrolCar.__init__(self,brand,model,fuel)


# MULTIPLE INHERITANCE :
class Battery :
    def battery_info(self):
        print("Battery : lithium_ion")


class Engine:
    def engine_info(self):
        print("Engine: petrol engine")

# class HybridCar(Car,Battery,Engine):
#     def __init__(self,brand,model):
#         super().__init__(brand,model)

#     def car_type(self):
#         print("Hybrid Car")
class AdvanceHybrid(HybridCar,Battery,Engine):
    # No __init__ needed
    # It will use HybridCar constructor automatically
    pass 


my_car = Car("Toyota","Corolla")
print(my_car.model)
print(my_car.brand)
print(my_car.full_name())

my_new_car = Car("Tata","Safari")
print(my_new_car.model)
print(my_new_car.brand)
print(my_new_car.full_name())

e1 = ElectricCar("Tesla", "Model S", "100kWh")
print(e1.full_name())
print(e1.battery)

e2 = ElectricCar("Tata", "Punch", "40kWh")
print(e2.full_name())
print(e2.battery)
print(e2.is_expensive())

l1 = LuxuryElectricCar("BMW", "i7", "120kWh", "Auto Drive, Premium Interior")
print(l1.features)
print(l1.battery)
print(l1.full_name())

p1 = PetrolCar("Tata","Safari","Petrol")
d1 = DieselCar("Mahindra", "Thar", "Diesel")
print(p1.full_name(),"-",p1.fuel_type())
print(d1.full_name(),"-",d1.fuel_type())


h1 = HybridCar("Toyota", "Prius", "50kWh", "Petrol")
h1.show()
print(h1.full_name())
print(h1.fuel_type())

ah1 = AdvanceHybrid("Lexus", "RX", "80kWh", "Petrol")
ah1.battery_info()
ah1.engine_info()
print(ah1.full_name())
print(ah1.fuel_type())




# STUDENT MANAGEMENT :

class Student:
    def __init__(self,Rollno,Name,Marks):
        self.Rollno = Rollno
        self.Name = Name
        self.Marks = Marks

    def show_details(self):
        print(f"Rollno: {self.Rollno} , Name: {self.Name} , Marks:{self.Marks}")

    def get_grades(self):
        if self.Marks >= 90:
            return "A"
        elif self.Marks >= 75:
            return "B"
        else:
            return "C"
            
            
class StudentManager:
    def __init__(self):
        self.students = []

    def add_student(self,student):
        self.students.append(student)

    def show_all(self):
        if not self.students:
            print("No students available")
            return

        for s in self.students:
            s.show_details()
            print("Grade:",s.get_grades())
            print("-" * 30)

    def find_student(self,roll):
        for s in self.students:
            if s.Rollno == roll:
                return s 
        return None


    def update_marks(self,roll,new_marks):
        student = self.find_student(roll)
        if student:
            student.Marks = new_marks
            print("MARKS UPDATED SUCESSFULLY !!!!")
        else :
            print("STUDENT NOT FOUND")


    def delete_student(self,roll):
        self.students = [s for s in self.students if s.Rollno != roll]
        print("STUDENT DELETED SUCESSFULLY")



manager = StudentManager()

manager.add_student(Student(1, "Sam", 85))
manager.add_student(Student(2, "John", 92))
manager.add_student(Student(3, "Amit", 70))

manager.show_all()

student = manager.find_student(2)
if student:
    student.show_details()
else:
    print("Student Not Found")

manager.update_marks(1,84)

manager.delete_student(3)

manager.show_all()


# menu system:

while True:
    print("1.Add student:")
    print("2.find student:")
    print("3.update marks:")
    print("4.delete student:")
    print("5.Show all:")
    print("6.Exit:")

    choice = input("Enter choice:")

    if choice == "1":
        roll = int(input("Enter Rollno:"))
        name = input("Enter Name:")
        marks = int(input("Enter Marks:"))
        manager.add_student(Student(roll,name,marks))

    elif choice == "2":
        roll = int(input("Enter Rollno:"))
        student = manager.find_student(roll)
        if student:
            student.show_details()
        else:
            print("Student not found")

    elif choice == "3":
        roll = int(input("Enter Rollno:"))
        marks = int(input("Enter new marks:"))
        manager.update_marks(Student(roll,marks))

    elif choice == "4":
        roll = int(input("Enter Rollno:"))
        manager.delete_student(Student(roll))

    elif choice == "5":
        manager.show_all()

    elif choice == "6":
        print("goodbye !!!!")
        break

    else:
        print("invalid data")





class student :
    school_name = "ABC school"    # ✅ Class variable

    def __init__(self,name):
        self.name = name         # Instance variable


s1 = student("sid")
print(s1.name)
print(s1.school_name)















