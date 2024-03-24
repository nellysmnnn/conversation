from human_class import *


class Fool(Human):
    def __init__(self, first_person, second_person):
        super().__init__(first_person, second_person)

    def talking(self):
        self.answer = f"{self.first_person['name']} greets {self.second_person['name']}"f": Hi, {self.second_person['name']}!\n"
        with open("conversation_log.txt", "a") as file:
            file.write(self.answer)
