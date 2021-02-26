from art import logo

#The main function
def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {cipher_direction}d result: {end_text}")

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

should_continue = True
while should_continue:
        empty = True
        while empty:
                direction = input("Type encode to encrypt or decode to decrypt:\n")
                if not(direction in ['encode','decode']):
                    print("You need to type in either encode or decode only.")
                    continue
                else:
                    break
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 25
        caesar(start_text = text, cipher_direction = direction, shift_amount = shift)

        running = True
        while running:
            restart = input("Type yes to start again, no to exit. \n")
            if not(restart in ['yes', 'no']):
                print("You need to type either yes or no only.")
                continue
            elif restart == 'no':
                print("Goodbye")
                should_continue = False
                break
            elif restart == 'yes':
                should_continue = True
                break
                