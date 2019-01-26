

class Person:
    def __init__(self, first_name, last_name, phone_number, title):
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.title = title
        self.full_name = f'{title} {first_name} {last_name}'


def create_number_not_saved_person(phone_number=""):
    return Person("Number", "Not Saved", phone_number, "")

def get_person_by_phone_number(phone_number, people):
    for person in people:
        if person.phone_number == phone_number:
            return person
    return create_number_not_saved_person(phone_number)


def get_phone_numbers(people):

    phone_numbers = []

    for person in people:
        phone_numbers.append(person.phone_number)
    
    return phone_numbers