#Question 1 - Functional Prompt

print("--Question 1--")

def flatten_and_sort(array):
    nums = []  # Initialize an empty list to store flattened elements

#Outer loop iterates through each sublist 'item' in the 'arr'
    for item in array:
        # Inner loop iterates through each element 'n' in the sublist 'item'
        for n in item:
            nums.append(n)  # Append the element 'n' to the 'nums' list

    return sorted(nums)  # Return the sorted 'nums' list


#1. The code lacks full data immutability enforcement.
#2. The code doesn't qualify as a pure function due to its modification of the 'flattened_nums' list, leading to side effects.
#3. This code doesn't demonstrate higher-order function characteristics as it doesn't incorporate other functions.
#4. A loop has been utilized within this function.
#5. Enhances code clarity while managing data.


#Question 2 Object Oriented Prompt

class Podracer:
    def __init__(self, max_speed, condition, price):
        self.max_speed = max_speed
        self.condition = condition
        self.price = price

    def repair(self):
        self.condition = "repaired"

class AnakinsPod(Podracer):
    def boost(self):
        self.max_speed *= 2

class SebulbasPod(Podracer):
    def flame_jet(self, other_podracer):
        other_podracer.condition = "trashed"


# Create instances of Podracers
podracer1 = Podracer(800, "perfect", 50000)
anakins_pod = AnakinsPod(1200, "trashed", 80000)
sebulbas_pod = SebulbasPod(1000, "repaired", 60000)

# Demonstrate the functionality
print("Original condition:", podracer1.condition)
podracer1.repair()
print("Repaired condition:", podracer1.condition)

print("Anakin's Pod max speed before boost:", anakins_pod.max_speed)
anakins_pod.boost()
print("Anakin's Pod max speed after boost:", anakins_pod.max_speed)

print("Sebulba's Pod condition before flame jet:", sebulbas_pod.condition)
sebulbas_pod.flame_jet(podracer1)
print("Sebulba's Pod condition after flame jet:", podracer1.condition)

#1:Encapsulation: Classes encapsulate data and methods, hiding internal details and providing data protection.
#2:Abstraction: Classes abstract implementation complexities, enabling interaction through exposed methods and attributes.
#3:Inheritance: Creates a hierarchy of classes, allowing derived classes to inherit attributes and methods from a base class, promoting code reuse and representing "is-a" relationships.
#4:Polymorphism: Polymorphism enables different classes to be treated as instances of a common superclass, facilitating flexibility and interchangeability in handling related objects.

#Coding Style Comparison: Using an Object-Oriented approach benefits by organizing code around entities, improving modularity and maintainability. Procedural programming might lead to code duplication and less clear representation of relationships and behaviors.

#Assistance of Object-Oriented Programming:Object-Oriented Programming aids by structuring code, modeling real-world relationships, and promoting modularity for easy maintenance.

