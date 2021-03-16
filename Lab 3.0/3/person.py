# author: Saul DLD
class Person:

    def __init__(self, name, email, age, country):
        self.name = name
        self.email = email
        self.age = age
        self.country = country

    def to_string(self):
        return "(Person: {name}, age: {age}, email:{email}, from:{country})".format(
            name=self.name, age=self.age, email=self.email, country=self.country)
