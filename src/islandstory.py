from random import randint
from person import Person

class IslandStory:
    def __init__(self, island):
        self.island = island
        self.day = -1
        self.new_people_comes_probability = 20
        self.min_new_people = 1
        self.max_new_people = 15

    def update_day(self):
        self.day = self.day + 1

        if self.day <= 0:
            return self.island.describe()

        day_events = ''

        person_comes_p = randint(0, 100)

        if person_comes_p > self.new_people_comes_probability:
            total_new_people = randint(self.min_new_people, self.max_new_people)
            for p in xrange(0, total_new_people):
                new_p = Person()
                self.island.add_person(new_p)
            day_events = '\t\t' + str(total_new_people) + ' new people came to here.\n'
            day_events = day_events + '\t\tTotal population: ' + str(self.island.get_population_size())


        if len(day_events) == 0:
            return '\tDay ' + str(self.day) + ': Nothing happened at all'
        return '\tDay ' + str(self.day) + ':\n' + day_events