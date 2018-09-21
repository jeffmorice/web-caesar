from helpers import alphabet_position, rotate_character

def encrypt(text, rot):
    new_str = ""

    for char in text:
        new_str += rotate_character(char, rot)

    return new_str

#print(encrypt("Hello, World!", 5))

def main():
    message = input("Type a message:\n")
    rotate = int(input("Rotate by:\n"))
    print(encrypt(message, rotate))

if __name__ == "__main__":
    main()
