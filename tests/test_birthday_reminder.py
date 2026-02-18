
from datetime import *

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
    assert birthday_reminder.birthday_dict == {"Tony": datetime.strptime("1998-11-12", '%Y-%m-%d').date()}

'''
Given a name and date in the dictionary, we edit the date
'''

def test_editing_birthday_of_entry_in_dict():

    birthday_reminder = BirthdayReminder()
    birthday_reminder.update("Tony", "1998-11-12")
    birthday_reminder.update("Tony", "1996-11-12")
    assert birthday_reminder.birthday_dict == {"Tony": datetime.strptime("1996-11-12", '%Y-%m-%d').date()}


'''As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name
'''

def test_edit_name():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.update("Tony", "1998-11-12")
    birthday_reminder.edit_name("Tony", "Tone")



'''As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

Note: assuming "soon" to be within 2 weeks.
'''

def test_list_soon_birthdays():
    birthday_reminder = BirthdayReminder()
    birthday_reminder.update("Tony", "1998-02-21") #should pass
    birthday_reminder.update("James", "1998-02-22") #should pass
    birthday_reminder.update("Sally", "1998-11-12") #should fail
    birthday_reminder.update("Tim", "1998-02-15") #should fail
    result = birthday_reminder.list_soon_birthdays()
  
    assert result == ["Tony", "James"]

'''As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays (that are soon?)
'''
def test_age():
    birthday_reminder = BirthdayReminder()
    birthday_reminder = BirthdayReminder()
    birthday_reminder.update("Tony", "1991-02-21") #should pass
    birthday_reminder.update("Alex", "1992-02-22") #should pass
    birthday_reminder.update("Jonny", "1998-02-24") #should pass
    birthday_reminder.update("Sally", "1998-11-12") #fail
    birthday_reminder.update("Tim", "1998-02-15") #fail
    result = birthday_reminder.age()
    assert result == "The following people are going to turn the following ages soon:\nTony: 34\nAlex: 33\nJonny: 27"


'''
    age = today_date.year - dob_datetime.year
    if (today_date.month, today_date.day) < (dob_datetime.month, dob_datetime.day):
        age -= 1 

'''


