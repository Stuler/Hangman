from random_word import RandomWords

def get_wrd():
    r = RandomWords()
    wrd = r.get_random_word(minLength=5, maxLength=10)
    wrd_lwr = wrd.lower().strip()
    return wrd_lwr

wrd_lwr = get_wrd()
print (wrd_lwr)

choices_count = 6
choices_list = []
unhid_word = []
guessed_list = []
init_word = ""

while choices_count > 0:
    choice = input("Guess the letter: ")
    if choice in wrd_lwr:
        print (f"Letter '{choice}' is contained in the word.\n")
        choices_list.append(choice)
    else:
        print (f"Letter '{choice}' isn't contained in the word.\n")
        choices_count = choices_count-1
    for i in wrd_lwr:
        if i in choices_list:
            unhid_word.append(i)
        else:
            unhid_word.append('*')
    
    guessed = init_word.join(unhid_word)
    guessed_list.append(guessed)
    wrd_to_shw = guessed_list[-1][-len(wrd_lwr):]
    print(wrd_to_shw, "\n")
    print(f"{choices_count} guesses left!\n")
    
    if choices_count > 0:
        guess_prompt = input("Do you want to guess the word? y/n: \n")
        if guess_prompt == "y":
            guess = input("Guess the word: ")
            if guess == wrd_lwr:
                print("Right guess!")
            else:
                print("Wrong guess!")
        else:
            continue      
    else:
        answer = input ("Guess the word: \n")
        if answer == wrd_lwr:
            print("Right guess!")
        else:
            print("Wrong guess! \n"
            f"Correct word: {wrd_lwr} \n")
    
    repeat_prompt = input("Do you want to play again? y/n: \n")
    if repeat_prompt == "y":
        wrd_lwr = get_wrd()
        choices_count = 6
        choices_list = []
        guessed_list = []
        unhid_word = []
    else:
        print("Quitting the game!")
        choices_count = 0

# add dificulties
# clean the code