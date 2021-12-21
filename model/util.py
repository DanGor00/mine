import random
import string


def generate_id(number_of_small_letters=4,
                number_of_capital_letters=2,
                number_of_digits=2,
                number_of_special_chars=2,
                allowed_special_chars=r"_+-!"):
    userid = ""
    ascii_lower = string.ascii_lowercase
    ascii_upper = string.ascii_uppercase
    digits = string.digits
    special_chars = ' '.join(allowed_special_chars)
    special_chars = special_chars.split()                                                       
    ascii_lower = ' '.join(ascii_lower)
    ascii_lower= ascii_lower.split()
    ascii_upper = ' '.join(ascii_upper)
    ascii_upper= ascii_upper.split()
    digits = ' '.join(digits)
    digits= digits.split()
    char_list = []
    for i in range(number_of_small_letters):
        char = random.choice(ascii_lower)
        char_list.append(char)

    for i in range(number_of_capital_letters):
        char = random.choice(ascii_upper)
        char_list.append(char)
        
    for i in range(number_of_digits):
        char = str(random.choice(digits))
        char_list.append(char)

    for i in range(number_of_special_chars):
        char = str(random.choice(special_chars))
        char_list.append(char)

    random.shuffle(char_list)
    
    for ele in char_list:
        userid += ele
    #print(userid)

    return userid