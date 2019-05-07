"""
silly_sentencer.py
formatted output:%s（string） %i（int） %f（float） %g(general) %(percentage)
This program prints silly sentences by mapping random words into a fromatting template.
sb. v. the adj. n..
 Jia.Q May 2019
"""
#print('hello %s, my name is Jia' %'Jane')
import random
template = '%s %s the %s %s.'
someone = ['My python teacher', 'Tim', 'Bob', 'Nancy', 'Jack',
           'Jane', 'Daisy', 'Timmy', 'The man', 'The kid', 'He', 'She']
adv = ['badly', 'difficultly', 'hardly', 'never', 'almost', 'just', 'only']
verb = ['is', 'reads', 'goes', 'returns', 'reaches', 'gets', 'learns', 'teaches',
        'studies', 'eats', 'has', 'writes', 'drives']
adj = ['beautiful', 'nice', 'good', 'big', 'small', 'heavy',
       'different', 'special', 'splendid', 'tall', 'ugly', 'frail', 'general']
noun = ['book', 'room', 'apple', 'fruits', 'bottle', 'pen', 'pencil', 'ruler',
        'computer', 'notebook', 'phone', 'bike', 'watch', 'car', 'instrument', 'feather']
if __name__ == '__main__':
    sb = random.choice(someone)
    av = random.choice(adv)
    v = random.choice(verb)
    aj = random.choice(adj)
    n = random.choice(noun)
    format_value = (sb, v, aj, n)
    #print(template % (sb, v, aj, n))
    print(template % format_value)