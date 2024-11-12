# Within the cohort class, add a constructor for cohort class
# Add a method to the class that prints the cohort name and total number of students
# Create a new instance/object of the cohort class

#Approach 1 Using inhertance:
# Parent class
class Cohort(object):
   # Adding a constructor for cohort class using: __init__ 
    def __init__(self, name, join_year):
        self.name = name
        self.join_year = join_year
# Method: display method
    def display(self):
        print(f"\nDisplay:\t")
        print(self.name)
        print(self.join_year)
 # Method: details method       
    def details(self):
        print(f"Cohort: {self.name}.")
        print(f"Start Year: {self.join_year}.")

# child class
class CohortName(Cohort):
    def __init__(self, name, join_year, total_students):
        self.total_students = total_students

        # invoking the __init__ of the parent class
        Cohort.__init__(self, name, join_year)
        
    def details(self):
        print(f"\nCohort Details:\t")
        print(f"Cohort: {self.name}")
        print(f"Start Year: {self.join_year}")
        print(f"Total Number of Students: {self.total_students}")


# creation of a new object variable or an instance of cohort class
a= CohortName('Cohort 3', 2022, 45)
b= CohortName('Cohort 4', 2024, 60)

# calling a function of the class Cohort using its instance 
a.display()
a.details()

b.display()
b.details() 

#Approach 2:
#using Encapsulation. It involves bundling the data(attributes) and methods (functions) that operate on the data into a single unit, called class.
class Cohort:
    def __init__(self, name, totalStudents):
        self.__name = name  # Private attribute
        self.__totalStudents = totalStudents    # Private attribute

    def display(self):
        print(f"\nCohort Summary:\t")
        print(f"Cohort Name: {self.__name}")
        print(f"Total Number of Students: {self.__totalStudents}")

    def details(self):
        print(f"\nCohort Details:\t")
        print(f"WITI in {self.__name} received {self.__totalStudents} as the total number of students admitted.")
        
        
a = Cohort('Cohort 3', 45)
b = Cohort('Cohort 4', 60)
a.display()       
a.details()
b.display()        
b.details()

