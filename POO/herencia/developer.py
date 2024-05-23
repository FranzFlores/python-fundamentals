from person import Person

class Developer(Person):
    def __init__(self):
        super().__init__()
        self.languages = ["Java","Python","C++","C#"]
        self.level = 3

    def get_languages(self):
        return self.languages
    
    def get_level(self):
        return self.level
    
    def learn(self,*languages):
        self.languages = languages
        return self.languages

    def program(self):
        return "Estoy programando"
    
    