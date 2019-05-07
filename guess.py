import random
#
def user_choose(total, guess):
    """user choose to start game again or not"""
    user_ans = 'y'
    while user_ans == 'y':
        user_implication = "Do you want to start again?(y/n)\n"
        user_ans = input(user_implication)
        if user_ans == 'y':
            total = total + 1
            guess = guess + guess_num()
        else:
            break
    return total, guess

def guess_num():
    """choose a number and start to guess"""
    implication0 = 'What is your guess?\n'
    result = True
    real_ans = random.randint(1, 100)
    get_ans = input(implication0)
    guess_count = 1
    while result:
        if real_ans == int(get_ans):
            print("Congratulation!")
            result = False #end up
        elif real_ans < int(get_ans):
            implication1 = "Too high, try again\n"
            get_ans = input(implication1)
            guess_count = guess_count + 1
        else:
            implication2 = "Too low, try again\n"
            get_ans = input(implication2)
            guess_count = guess_count + 1
    return guess_count

if __name__ == '__main__':
    implication = 'Do you want to play the game?(y/n)\n'
    ans = input(implication)
    total_round = 0
    total_guess = 0
    if ans == 'y':
        total_guess = guess_num()
        total_round = 1
        total_round, total_guess = user_choose(total_round, total_guess)
    print(total_round, total_guess, 'avg:'+str(total_guess/float(total_round)))