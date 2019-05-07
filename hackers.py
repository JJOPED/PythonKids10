"""
if __name__ == '__main__':
    list1 = [2*x for x in range(3)]#0,1,2->0,2,4
    print(list1)
    list2 = [x for x in range(10) if x % 2 == 1]#odd number between 0  and 10
    print(list2)
    reverse_list2 = list2.reverse()#list2 has been changed while reverse_list2 is none
    print(reverse_list2,' ',list2)
"""
"""1337.py
Given a message, convert it into 1337 sp34k
Jia.Q, May 2019"""

test_message = 'Hello World!'
test_substitutions = [['e', '3']]
substitutions = [['a', '4'], ['e', '3'], ['l', '1'], ['o', '0'], ['t', '7']]
#functiion section
def encode_message(message = test_message, substitutions = test_substitutions):
    """Take a string message and apply each of the substitutions provided. 
    Substitutions should be a list, the elements of substitutions need to belistes of
     length 2 of the form(old_string, new_string)"""
    convert = message
    for c in substitutions:
        old = c[0]
        new = c[1]
        convert = convert.replace(old, new)#the replace function don't change the primary string
    return convert
#test section
message = input('Type the message to encode here:')
convert_message = encode_message(message, substitutions)
print(message)
print(convert_message)
"""
Learn how to use the tool of Debug>>Debugger in IDLE. You should open a .py file
and set a breakpoint."""