def get_indices(word, letter):
    '''
    Function returns list of guessed letters indices
    '''
    ind_lst = []
    for i in word:
        if i == letter:
            ind = word.index(i)
            ind_lst.append(ind)
    return ind_lst

def star_replacement(word, letter):
    mod_msg = "*" * len(word)
    for i in word:
        if i == letter:
            let_ind = word.index(i)
            mod_msg[let_ind] = letter
    return mod_msg
            
#print(get_indices("alaska","a"))
print(star_replacement("alaska","s"))