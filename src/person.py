from random import randint

class Person:
    def __init__(self):
        self.all_first_name = ['Jorbes', 'Mil', 'Jos']
        self.all_last_name = ['Galapos', 'Galateia', 'Morango']
        self.name = self.generate_person_name()

    def generate_person_name(self):
        return self.all_first_name[randint(0, len(self.all_first_name)-1)] + \
            ' ' + self.all_last_name[randint(0, len(self.all_last_name)-1)]

