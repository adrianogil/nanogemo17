from eventposition import EventPosition
from random import randint
from utils import get_random

class Island:
    def __init__(self, sizex = -1, sizey = -1):
        self.all_adjetives = ['Ancient', 'Boring', 'Charming', 'Exciting', 'Fantastic', 'Fascinating', 'Vibrant', 'Death', 'Happy', 'Strange']
        self.all_main_names = ['Land', 'Country', 'Island', 'Village']

        self.all_resources = ['Wood', 'Water', 'Gold']

        if sizex != -1:
            self.sizex = sizex
        else:
            self.sizex = randint(4,30)

        if sizey != -1:
            self.sizey = sizey
        else:
            self.sizey = randint(4,30)

        self.island_matrix = [[EventPosition((x,y),'nothing') for x in xrange(0,self.sizex)] for y in xrange(0, self.sizey)];
        self.island_name = self.generate_island_name()

        self.resources = self.generate_resources()

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

    def generate_resources(self):
        new_resources_attempts = randint(1, self.sizey*self.sizex)
        for i in xrange(0, new_resources_attempts):
            randposx = randint(0, self.sizex-1)
            randposy = randint(0, self.sizey-1)

            if self.island_matrix[randposy][randposx].event_type == 'nothing':
                self.island_matrix[randposy][randposx].event_type = get_random(self.all_resources)

    def describe(self):
        island_description = 'God created the region named as ' + self.island_name + \
            ' with a size ' + str(self.sizey) + ' x ' + str(self.sizex)

        resources_position = 0

        for y in xrange(0, self.sizey):
            for x in xrange(0, self.sizex):
                if self.island_matrix[y][x].event_type != 'nothing':
                    island_description = island_description + '\nThere is ' + self.island_matrix[y][x].event_type + \
                        ' position (' + str(y) + ',' + str(x) + ')'
                    resources_position = resources_position + 1

        island_description = island_description + "\nTotal resources position is " + str(resources_position)

        return island_description
