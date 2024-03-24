class Human:
    def __init__(self, first_person, second_person):
        self.first_person = first_person
        self.second_person = second_person
        self.answer = ''


    def talking(self):
        self.answer = f"{self.first_person['name']} greets {self.second_person['name']}:"f" Hello, {self.second_person['name']}\n"
        with open("conversation_log.txt", "a") as file:
            file.write(self.answer)

