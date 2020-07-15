from datetime import date
    
def main():
    name = 'Michael'
    height = 190
    birthdate = date(1976, 8, 14)
    Michael = Person(name, height, birthdate)
    print(Michael.get_description())
    
class Person:
    def __init__(self, name, height, birthdate):
        self.name = name
        self.height = height
        self.birthdate = birthdate
        
    def get_name(self):
        return self.name
    
    def get_height(self):
        return self.height
    
    def get_age(self):
        today_date = date.today()
        age = today_date.year - self.birthdate.year
        if self.birthdate.month > today_date.month:
            age -= 1
        elif self.birthdate.month == today_date.month:
            if self.birthdate.day > today_date.day:
                age -= 1
        return age        
    
    def get_description(self):
        return self.name + ' is ' + str(self.height) + ' cm high and is ' + str(self.get_age()) + ' years old.'    

main()
