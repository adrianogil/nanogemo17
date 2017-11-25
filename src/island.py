from eventposition import EventPosition
from random import randint

class Island:
    def __init__(self, sizex = 10, sizey = 10):
        self.all_adjetives = ['Ancient', 'Boring', 'Charming', 'Exciting', 'Fantastic', 'Fascinating', 'Vibrant', 'Death', 'Happy', 'Strange']
        self.all_main_names = ['Land', 'Country', 'Island', 'Village']

        self.sizex = sizex
        self.sizey = sizey
        self.island_matrix = [[EventPosition((x,y),'nothing') for x in xrange(0,sizex)] for y in xrange(0, sizey)];
        self.island_name = self.generate_island_name()

        self.people = []

    def generate_island_name(self):
        return self.all_adjetives[randint(0,len(self.all_adjetives)-1)] + ' ' + \
            self.all_main_names[randint(0, len(self.all_main_names)-1)]

    def get_population_size(self):
        return len(self.people)

    def add_person(self, p):
        self.people.append(p)

    def remove_person(self, p):
        self.people = [x for x in self.people if x != p]
