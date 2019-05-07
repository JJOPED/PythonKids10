"""
math_trainer.py
Train your times table.
Initial Features:
* Point out times table for a given number.
* Limit tables to a lower number (default is 1) and an upper number (default is 12)
* Pose test questions to the user.
* Check whether the user is right or wrong.
* Track the user's score.
Jia.Q
May 2019
"""
"""
def get_num():
    return [(x ,y) for x in range(3) for y in range(3)]
print(get_num())
"""
#import section
import random
import sys
import time

#constants
LOWER = 1
UPPER = 12
MAX_QUESTIONS = 7
QUESTION_TEMPLATE = "What is %sx%s?"
TABLES_TEMPLATE = "%2i x %2i = %3i"
INSTRUCTIONS ="""Welcome to Math Trainer
 This application will train you on your times tables.
 It can either print one or more of the tables for you so that you can revise (training) 
  or it can test your times tables.
"""

#function section
def make_question_list(lower=LOWER, upper=UPPER, random_order=True):
    """
    prepare a list of question in the form (x,y) 
    where x and y are in the range from LOWER to UPPER inclusive
    using random.shuffle() to shuffle the list of question and get a random list to traverse
    """
    spam = [(x+1, y+1) for x in range(lower-1, upper) for y in range(lower-1, upper)]
    if random_order is True:
        random.shuffle(spam)#Shuffle list x in place, and return None
    return spam

def do_training():
    """
    Start to train with the max number of question MAX_QUESTIONS and get the score
    """
    question_list = make_question_list()
    score = 0
    start_time = time.time()
    #for i in MAX_QUESTIONS:#'int' object is not iterable
    for i, question in enumerate(question_list):
        if i >= MAX_QUESTIONS: #index start from 0
            break
        user_ans = input(QUESTION_TEMPLATE % (question))
        right_ans = question[0] * question[1]
        if int(user_ans) == right_ans:
            print('Correct!')
            score = score + 1
        else:
            print('Incorrect, should have been %s' % (right_ans))
    end_time = time.time()
    time_token = end_time - start_time
    #time.time():time() -> floating point number;Return the current time in seconds since the Epoch
    #time.ctime():ctime(seconds) -> string;Convert a time in seconds since the Epoch to a string in local time
    #time.gmtime(): gmtime([seconds]) -> (tm_year, tm_mon, tm_mday, tm_hour, tm_min,tm_sec, tm_wday, tm_yday, tm_isdst)
    #Convert seconds since the Epoch to a time tuple expressing UTC (a.k.a.GMT).  When 'seconds' is not passed in, convert the current time instead
    print("score:%.2f by using %.2fs" % (score/float(MAX_QUESTIONS)*100, time_token))

def display_times_table(upper=UPPER):
    """
    Display the times table up to UPPER 
    """
    table_per_line = 5
    table_to_print = range(1, upper+1)
    # get a batch of table_per_line to print
    batch = table_to_print[:table_per_line]
    #remove them from table_to_ptint
    table_to_print = table_to_print[table_per_line:]
    while batch != []: #stop when there is no more to print
        for x in range(1, upper+1): #x from 1 to 12
            accumulator = []
            for y in batch:
                accumulator.append(TABLES_TEMPLATE % (x, y, x*y))
            #print one row
            print(' '.join(accumulator))
        print('\n')
        #another round 1-12 *6-10
        if len(table_to_print) < table_per_line:
            batch = table_to_print
            table_to_print = []
        else:
            batch = table_to_print[:table_per_line]
            table_to_print = table_to_print[table_per_line:]

def to_quit():
    """quit the application"""
    if confirm_quit():
        sys.exit()
    print("In quit (not quiting, returning")

def confirm_quit():
    """to confirm"""
    CONFIRM_INSTRUCTION = "Are you sure you want to quit (y/n)?"
    spam = input(CONFIRM_INSTRUCTION)
    if spam == 'y':
        return True
    else:
        return False

#main section
if __name__ == '__main__':
    #print(template % random.choice(make_question_list()))

    #display_times_table()
    #do_training()

    print(INSTRUCTIONS)
    prompt = 'Press 1 for training, 2 for testing, 3 for quit'
    user_chose = input(prompt)
    # Return a copy of the string S with leading and trailing whitespace removed.
    user_chose = user_chose.strip()
    while user_chose not in ['1', '2', '3']:
        user_chose = input("Please type either 1, 2 or 3")
        user_chose = user_chose.strip()
    if user_chose == '1':
        display_times_table()
    elif user_chose == '2':
        do_training()
    else:
        to_quit()
