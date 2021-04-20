# Implement a class that manages a Directory
# author: Saul DLD

from directory import Directory
from person import Person
import logging


logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.INFO, filename='app.log', filemode='w+', format='%(name)s - %(levelname)s - %(message)s')

def main():
    logging.info("Running Application...");

    directory = Directory()

    add_persons(directory)
    show_directory(directory)

    find_user(directory, "robin@bgs.com", 62)
    find_user(directory, "elvis@presley.com", 42)

    delete_user(directory, 2)
    show_directory(directory)

    save_directory(directory)


def add_persons(directory):
    logging.debug("Adding persons...");

    persons = [
        Person("Barry Gibb", "barry@bgs.com", 74, "Australia"),
        Person("Maurice Gibb", "maurice@bgs.com", 53, "Germany"),
        Person("Robin Gibb", "robin@bgs.com", 62, "Portugal"),
        Person("Andy Gibb", "andy@bgs.com", 30, "Mexico")
    ]
    for person in persons:
        directory.add(person)


def delete_user(directory, index):
    logging.info("Removing user...");
    print("> Delete user in position: ", index)
    directory.delete(index)


def find_user(directory, email, age):
    logging.info("Finding user...");
    p = directory.find_by_email_age(email, age)
    if p is None:
        logging.info("User not found: ")
        print("> Person not found: {user}".format(user=email))
    else:
        print("> ", p.to_string())
    
    return p


def show_directory(directory):
    logging.info("Showing Directory...");
    print("=" * 80)
    print("Directory")
    directory.list()
    print("=" * 80)


def save_directory(directory):
    logging.info("Saving Directory...");
    file = open("./Directory.txt", "w+")
    for idx, person in enumerate(directory.persons, start=1):
        file.write("[{index}] {person}\n".format(index=idx, person=person.to_string()))


if __name__ == "__main__":
    main()
