import string

def alphabet_position(letter):
    # return the 0-based position of the letter in the alphabet
    # case-INsensitive
    uppercase = string.ascii_uppercase

    up_str = letter.upper()
    #print(up_str)

    for char in range(len(uppercase)):
        if uppercase[char] == up_str:
            return char

#uppercase = string.ascii_uppercase
#print(type(uppercase))
#print(alphabet_position("Z"))

def rotate_character(char, rot):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    pos = alphabet_position(char)

    if char in uppercase:
        new_char = uppercase[(pos + rot) % 26]
    elif char in lowercase:
        new_char = lowercase[(pos + rot) % 26]
    else:
        new_char = char

    return new_char

#print(rotate_character("%", 13))
