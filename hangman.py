from random_word import RandomWords

r = RandomWords()
#wrd = r.get_random_word(minLength=5, maxLength=10)
wrd = "Alaska"
wrd_lwr = wrd.lower()
print (wrd) # helper

msg = "*"*len(wrd)
mod_mess = ""

choices_count = 6

while choices_count >0:
    choice = input("Guess the letter: ")
    if choice in wrd_lwr:
        print (f"Letter '{choice}' is contained in the word.")
    #    choice_pos = wrd_lwr.index(choice)
    else:
        print (f"Letter '{choice}' isn't contained in the word.")
    choices_count = choices_count-1
    for i in wrd_lwr:
        if i == choice:
            choice_pos = wrd_lwr.index(choice)
            out_mess = wrd_lwr.replace("*", choice)
            mod_mess = msg[:choice_pos] + choice + msg[choice_pos+1:]
            msg = mod_mess 
            print(msg)
            print("")
    
guess = input("Guess the word: ")
if guess == wrd_lwr:
    print("Right guess!")
else:
    print("Wrong guess! You loose!")