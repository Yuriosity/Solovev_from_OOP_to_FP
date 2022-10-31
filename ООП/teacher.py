from person import Person


class Teacher(Person):

    def __init__(self, person, subject):
        self.subject = subject
        self.person = person
	
    def get_person(self):
        return self.person
    
    def get_subject(self):
        return self.subject
