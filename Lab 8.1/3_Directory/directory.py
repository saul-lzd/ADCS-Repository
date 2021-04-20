# author: Saul DLD
class Directory:
    persons = []

    def add(self, person):
        self.persons.append(person)

    def delete(self, position):
        self.persons.pop(position - 1)

    def find_by_email_age(self, email, age):
        p = None
        for person in self.persons:
            if person.email == email and person.age == age:
                p = person
                break;
                
        return p

    def list(self):
        for idx, person in enumerate(self.persons, start=1):
            print("[{index}] {person}".format(index=idx, person=person.to_string()))
