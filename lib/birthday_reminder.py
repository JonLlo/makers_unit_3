class BirthdayReminder():

    def __init__(self):
        self.birthday_dict = {}
        print(self.birthday_dict)

    def update(self, name, date):
        self.birthday_dict[name] = date

    def edit_name(self, name, newname):
        saved_birthday = self.birthday_dict[name]
        self.birthday_dict.pop(name)
        self.birthday_dict[newname] = saved_birthday







