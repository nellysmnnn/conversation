import random

from conversation.realist_class import Realist
from positive_class import *
from fool_class import *


class main:
    def __init__(self):
        self.peoples = {}
        self.people_names = ["Anahit", "Irina", "Narine", "Armen", "Alexander", "Aram", "Hayk", "Silva", "Sanasar",
                             "Baghdasar"]
        self.people_types = ["Fool", "Positive", "Realist"]

    def distributing_people(self):
        with open("conversation_log.txt", "w") as file:
            file.write('')

        for i in range(5):
            random_name = random.choice(self.people_names)
            self.peoples[i] = {
                "name": random_name,
                "type": random.choice(self.people_types),
                "age": random.randint(20, 40)
            }
            self.people_names.remove(random_name)

    def init_conversation(self):
        for (fp_key, first_people) in self.peoples.items():
            for (sp_key, second_people) in self.peoples.items():
                if fp_key != sp_key:
                    self.say_hello(first_people, second_people)

    def say_hello(self, greeter, greeted):
        if (greeter['type'] == 'Positive'):
            Positive(greeter, greeted).talking()
        elif (greeter['type'] == 'Fool'):
            Fool(greeter, greeted).talking()
        elif (greeter['type'] == 'Realist'):
            Realist(greeter, greeted).talking()


main_class = main()
main_class.distributing_people()
main_class.init_conversation()
