from datetime import *
class BirthdayReminder():

    def __init__(self):
        self.birthday_dict = {}
        print(self.birthday_dict)

    def update(self, name, date):
        
        self.birthday_dict[name] = datetime.strptime(date, '%Y-%m-%d').date()

    def edit_name(self, name, newname):
        saved_birthday = self.birthday_dict[name]
        self.birthday_dict.pop(name)
        self.birthday_dict[newname] = saved_birthday

    def list_soon_birthdays(self):
        list = []
        today = date.today()
        two_weeks = date.today() + timedelta(days=14)
        for key in self.birthday_dict.keys():
            print(type(self.birthday_dict[key]))
            
            

            pass
            '''
            if dict[key] is in range today, intwoweeks:
                list.add(key)

            [key[value] for k,v in birthday_dict if ...]
            '''




        print(today)
        print(two_weeks)
        print(type(today))



        
birthday_reminder = BirthdayReminder()
birthday_reminder.update("Tony", "1998-02-21") #should pass
birthday_reminder.update("Toy", "1998-11-12") #should fail
birthday_reminder.update("ny", "1998-11-12") #should fail
birthday_reminder.list_soon_birthdays()








