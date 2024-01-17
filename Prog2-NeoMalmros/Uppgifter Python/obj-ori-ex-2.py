# Write a Python program to create a person class. 
# Include attributes like name, country and date of birth. 
# Implement a method to determine the person's age.
months = ["january", "februry", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
class Person:
    def __init__(self, name, country, birthday, age):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.age = age
        date = self.birthday.split(" ")
        if int(date[0]) == 1:
            date[0].replace("1st")
        elif int(date[0]) == 2:
            date[0].replace("2nd")
        elif int(date[0]) == 3:
            date[0].replace("3rd")
        else:
            date[0].replace(f"{date[0]}th")
        print(f"{name} will turn {int(age) + 1} on the {date[0]} of {months[int(date[1])]}, 2024")

person1 = Person("Markus Petterson", "Afghanistan", "22 2 1945", "78")
person1.__init__()