# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

_Put or write the user story here. Add any clarifying notes you might have._

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays

#optional
As a user
So I can keep track of cards sent and to be sent
I want to be able to mark a birthday card for a year as "done"


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

from datetime import datetime, date

class BirthdayReminder:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:none
        # Side effects:
        #   Sets the name property of the self object
            #Side effect: creates a dictionary of names and birthdays
        pass # No code here yet

    '''
    As a user
    So I don't forget the details
    I want to keep a record of friends' names and birthdates
    '''
    def update(self, name, date):
        # Parameters: name (string), date (string)
        # Returns:
        #   Nothing
        # Side-effects
        #   date will become a 'datetime' format
        pass # No code here yet
    '''As a user
    So I can make edits when I've got dates wrong
    I want to be able to update a record by passing in a name and new date
    '''
    #use update(). Does same thing.


    '''As a user
    So I can make edits when people change their name
    I want to be able to update a record by passing in an old and a new name
    '''
    def edit_name(self, name, newname):
        # Parameters: name (string), newname (string)
        # Returns:
        #   Nothing
        # Side-effects
        #none
    pass # No code here yet

    '''As a user
    So I can remember to send birthday cards at the right time
    I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

    Note: assuming "soon" to be within 2 weeks.

    '''
    def list_soon_birthdays(self):
    # Parameters: name (string), newname (string)
    # Returns:
    # A string of the form "the following names have a birthday soon: "
    # Side-effects
    #none
    pass # No code here yet


    '''As a user
    So I can buy age-appropriate birthday cards
    I want to calculate the upcoming ages for friends with birthdays'''
        def calculate_birthday_ages(self):
    # Parameters: none
    # Returns:
    # A string of the form "the following people have a birthday soon, and here are there ages:  "
    # Side-effects
    #none
    pass # No code here yet


    '''So I can keep track of cards sent and to be sent
    I want to be able to mark a birthday card for a year as "done"
    '''
    def track_cards(self):
    # Parameters: none
    # Returns:
    # A string of the form "the following people have a birthday cards, and below lists whether they have been sent:  "
    # Side-effects
    #none
    pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

''' 
Given initialisation, creates an empty dictionary
'''

birthday_reminder = BirthdayReminder()
birthday_dict = {}

'''
Given a name and date, we add it to the dictionary

'''
birthday_reminder = BirthdayReminder()
birthday_reminder.add("Tony", "1998-11-12"):

'''
Given a name and date in the dictionary, we edit the date

'''
birthday_reminder = BirthdayReminder()
birthday_reminder.edit_date("Tony", "1997-11-12"):

'''
Given a name and date in the dictionary, we edit the name

'''
birthday_reminder = BirthdayReminder()
birthday_reminder.edit_name("Tony", "Tone"):






#...
"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
