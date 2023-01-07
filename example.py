class Eatery:
# make Restaurant should store two attributes: a restaurant_name and a cuisine_type.
# Make a method     Make a class called Restaurant. The __init__() method for 
# called describe_restaurant() that prints these two pieces of 
# information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.
# Three Restaurants: Start with your class from Exercise 9-1. Create three 
# different instances from the class, and call describe_restaurant() for each 
# instance
    def __init__(self,type,foods):
        self.type=type
        self.food=foods
        self.number_served=0
    def about_eatery(self):
        print(self.type + "is the best eatery and ave good location")
        print("i love to eat "+self.food+" in "+self.type)
    def time_eatery(self):
        print(self.type + " opens everyday but open by 9am on sunday's")
    def served_number (self):
        print(self.type+"served about "+str(self.number_served)+" costomer's a day.")
    def set_number (self,num):
        if num >= self.number_served:
            self.number_served=num
        else:
            print("you are a liar!!!")
    def increment_served (self,x):
        self.number_served+=x
        
        
        
        
my_eatery = Eatery("mega chicken","fried rice")
print("my best eatery is "+my_eatery.type)
print("i always buy "+my_eatery.food)
my_eatery.about_eatery()
my_eatery.time_eatery()
my_eatery.set_number(27)
my_eatery.increment_served(20)
my_eatery.served_number()


# Write a python class that accepts two arguments(name and age)
# respectively and a method that returns e.g "Yaqub is an adult" 
# or "Yaqub is not an adult" depending if the age is greater
# than 18 and viceversa
class Information:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def age_count(self):
        if self.age >= "18":
            return self.name+" you are an aldult"
        else:
            return self.name+" you are not an aldult"
        

no_1 = Information("ayub","21")
no_2 = Information("olu","10")
person=no_1.age_count()
persin=no_2.age_count()
print(person)
print(persin)

