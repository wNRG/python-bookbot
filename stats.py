def get_word_count(string):    
    return len(string.split())

def get_character_count(string): 
    x = {}    
    for char in string.lower():
        if char in x:
            x[char]+=1
        else:
            x[char] = 1

    return x

def sort_dictionary(dictionary):
    x = [] 
    for char, num in dictionary.items():
        x.append({'char': char, 'num': num})

    x.sort(key=sort_by_num, reverse = True)

    return x

def sort_by_num(dictionary):
    return dictionary['num']
