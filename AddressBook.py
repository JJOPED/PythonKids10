"""
AddressBook.py
An address book program to store details of people I know.
Stuff I'm storing is:
first name
family name
email address
date of birth
[other stuff]
Jia.Q
May 2019
"""

#a = AddressBook()
#a.instance_contribute = 0
#print(a.instance_contribute) #0

#import section
#import _compat_pickle as pickle
import pickle
import  os.path

#Constant
SAVE_FILE_NAME = 'address_book.pickle'
INSTRUCTIONS = """Address Book Application
Press:
a to add a person
d to display a list of all entry in summary form
i to print these instruction again
q to quit
"""
CONFIRM_QUIT = 'Are you sure that you want to quit? (y/n)'

##class section
class AddressBook(object):
    """
    AddressBook instance hold and manage a list of people
    """
    def __init__(self):
        """
        Set people attribute to an empty list
        """
        self.people = []

    def add_people(self, new_people):
        """
        Add a new people to the list
        """
        self.people.append(new_people)

    def save_people(self):
        """
        save a copy of self into  a pickle file
        """
        with open(SAVE_FILE_NAME, 'w') as file_object:
            pickle.dump(self, file_object)


class People(object):
    """
    the class of People which save some information
    """
    def __init__(self, first_name=None, family_name=None, email_address=None, date_of_birth=None):
        """
        People instances hold and manage details of a person
        """
        self.first_name = first_name
        self.family_name = family_name
        self.email_address = email_address
        self.date_of_birth = date_of_birth
    def __repr__(self):
        """
        Given a People object self return a readable string representation
        """
        template = "first name: %s\n"+"family name: %s\n"+"email address:%s\n"+"date of birth: %s\n"
        return template%(self.first_name, self.family_name, self.email_address, self.date_of_birth)

class Controller(object):
    """
    Controller acts as a way of managing the data stored in an instance of People and
     the user, as well as managing loading the stored data
    """
    def __init__(self):
        """
        initial Controller.
        Look for a saved address book.
        If one is found, load it, otherwise create an empty address book.
        """
        """self.address_book = AddressBook()
        temp_people = People('Eric', 'Idle', None, 'March 22,1997')
        self.address_book.add_people(temp_people)"""
        self.address_book = self.load()
        if self.address_book is None: # if you use "==", there will be woring
            self.address_book = AddressBook()
        self.run_instance()


    def load(self):
        """
        Load a pickled address book from the standard save file
        """
        if os.path.exists(SAVE_FILE_NAME) :
            with open(SAVE_FILE_NAME, 'r') as file_object:
                return (pickle.loads(file_object))

        else:
            return None

    def run_instance(self):
        """
        Appliction's main loop: get users inputs and respond accordingly 
        """
        print(INSTRUCTIONS)
        while True:
            command = input("What would you like to do?")
            if command == 'a' :
                self.add_in_controller()
            elif command == 'd':
                self.display_summaries()
            elif command == 'i':
                print(INSTRUCTIONS)
            elif command == 'q':
                if confirm_quit():
                    self.address_book.save_people()
            else:
                print("I don't recognize that instruction (%s)" %command)



    def add_in_controller(self):
        """
        get the input from usres and add a new person into the list and pickled file
        """
        print("Adding a new person to the address book ")
        print("What is the person's:")
        first_name = input('first name:')
        if first_name == 'q':
            print('Not adding.')
            return
        family_name = input('family name:')
        if family_name == 'q':
            print('Not adding')
            return
        email_address = input('email address:')
        if email_address == 'q':
            print('Not adding')
            return
        date_of_birth = input('date of birth (Month day, year):')
        if date_of_birth == 'q':
            print('Not adding')
            return
        temp_people = People(first_name, family_name, email_address, date_of_birth)
        self.address_book.add_people(temp_people)
        print('Added address entry for %s %s\n'%(first_name, family_name))

    def display_summaries(self):
        """
        display summary information for each entry in  address book
        """
        print("Display Summaries:")
        for index, e in enumerate(self.address_book.people):
            values = (e.first_name, e.family_name, e.email_address, e.date_of_birth)
            print("%s:%s:"%(index+1, values))

#function section
def confirm_quit():
    spam = input(CONFIRM_QUIT)
    if spam == 'y':
        return True
    else:
        return False

#main section
if __name__ == '__main__':
    """
    address_book = AddressBook()
    temp_people = People('Eric', 'Idle', None, 'March 22,1997')
    address_book.add_people(temp_people)
    print(address_book.people[0])
    """
    controller = Controller()
    print(controller.address_book.people)