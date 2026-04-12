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












