
from lib.birthday_reminder import BirthdayReminder
''' 
Given initialisation, creates an empty dictionary
'''
def test_class_initialises_with_empty_dict():
    birthday_reminder = BirthdayReminder()
    assert birthday_reminder.birthday_dict == {}


'''
Given a name and date, we add it to the dictionary

'''
def test_adding_name_and_birthday_to_dict():

    birthday_reminder = BirthdayReminder()
    birthday_reminder.update("Tony", "1998-11-12")
    assert birthday_reminder.birthday_dict == {"Tony": "1998-11-12"}

'''
Given a name and date in the dictionary, we edit the date
'''

def test_editing_birthday_of_entry_in_dict():

    birthday_reminder = BirthdayReminder()
    birthday_reminder.update("Tony", "1998-11-12")
    birthday_reminder.update("Tony", "1996-11-12")
    assert birthday_reminder.birthday_dict == {"Tony": "1996-11-12"}


'''As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name
'''

def test_edit_name():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.update("Tony", "1998-11-12")
    birthday_reminder.edit_name("Tony", "Tone")




