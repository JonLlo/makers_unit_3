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
        reminder_list = []
        today = date.today()

        
        two_weeks = date.today() + timedelta(days=14)
        print(f'HELLO: {type(two_weeks)}')

        if today < two_weeks:
            print("yes")
            print(today.month)
            print(today.day)
            print(two_weeks.month)

        for key in self.birthday_dict.keys():
            if (today.month, today.day) < (self.birthday_dict[key].month, self.birthday_dict[key].day)  < (two_weeks.month, two_weeks.day):
                print(f'We are seeing that {key} has a birthday soon: {self.birthday_dict[key]}')
    
                reminder_list.append(key)
        print(reminder_list)
                
                

            #if dict[key] is in range today, intwoweeks:
            #    list.add(key)



        print(type(self.birthday_dict[key]))
            
            

         
        '''
        if dict[key] is in range today, intwoweeks:
            list.add(key)

        [key[value] for k,v in birthday_dict if ...]
            '''




        print(today)
        print(two_weeks)
        print(type(today))
        return reminder_list


    def age(self):
        self.final_dict = {}
        reminder_list_extracted = self.list_soon_birthdays()
        print(f'xyz {reminder_list_extracted}')
        for name in reminder_list_extracted:
            dob = self.birthday_dict[name]
            today = date.today()
            age = today.year - dob.year
            if (today.month, today.day) < (dob.month, dob.day):
                age = age - 1
                self.final_dict[name] = age
        final_str = 'The following people are going to turn the following ages soon:'
        for key, value in self.final_dict.items():
            final_str = final_str + (f'\n{key}: {value}')
        

        
        print(final_str)
        print(self.final_dict)
        return final_str
            


        





        
birthday_reminder = BirthdayReminder()
birthday_reminder.update("Tony", "1991-02-21") #should pass
birthday_reminder.update("Alex", "1992-02-22") #should pass
birthday_reminder.update("Jonny", "1998-02-24") #should pass
birthday_reminder.update("Toy", "1998-11-12") #should fail
birthday_reminder.update("ny", "1998-11-12") #should fail
birthday_reminder.list_soon_birthdays()
birthday_reminder.age()








