user_input = input("Enter the message you would like to encrypt: ").upper() ## Asks the user to enter words they want to encrypt.

while not all(char.isalpha() or char in (' ', '.') for char in user_input): ## Disables anything that is not a letter, except for full-stop and spaces
    print("Only alphabetic characters are allowed.") # Starts over if anything besides alphabetic characters are entered (symbols, numbers)
    user_input = input("Enter the words you would like to encrypt: ").upper() ## Asks user to enter message they want to encrypt.

shift = int(input("Please enter how much you would like to shift by: ")) ## Asks the user how much they would like to shift each letter by.
cipher_text = ""

for char in user_input: ## Iterates over each character inputted in the user_input 
    if char == ".":
        newchar = (ord("X") - 65 + shift) % 26 ## Changes full-stops to X and shifts by number chosen
        cipher_text += chr(newchar + 65)
    elif char.isalpha():
        newchar = (ord(char) - 65 + shift) % 26 ## Shifts all alphabetic letters by shift number inputted.
        cipher_text += chr(newchar + 65)

print(f"Message Encrypted!: {cipher_text}")

