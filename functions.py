NUM_OF_GUESSES = 10
WORDS_LIST = ["apple", "banana","carrot","cucumber", "eggplant","Fig", "Grape", "Lettuse","Mango","Potato"]

from random import choice

def choose_random_word(wordes:list[str]) -> str:
    the_random_word = choice(wordes)
    return the_random_word.lower()

def create_mask_word(word:str) -> str:
    the_mask_word = "*" * len(word)
    return the_mask_word


def print_game_status(mask_word:str, guesses_left:int,guessed_letters:set) -> None:
    print("==========")
    print(f"The mask of wordes: {mask_word}.")
    print(f"You have {guesses_left} guesses left!") 
    if guessed_letters:
        print(f"You've already guessed the letters: {" ".join(guessed_letters)}.")

def get_user_input(guessed_letters:set) -> str:
    is_valid_input = None
    while not is_valid_input or already_guessed:
        user_input = input("Guess one letter:")
        is_valid_input = check_validate_of_input(user_input)
        already_guessed = check_if_letter_already_guessed(user_input,guessed_letters)
    return user_input
        
def check_validate_of_input(user_input:str) -> bool:
    if user_input.isalpha() and len(user_input) == 1:
        return True
    else:
        return False

def update_guessed_letters_set(guessed_letters:set, letter:str) -> set:
    guessed_letters.add(letter.lower())
    return guessed_letters

def check_if_letter_already_guessed(user_input:str, guessed_letters:set) -> bool:
    if not guessed_letters:
        return False
    if user_input.lower() in guessed_letters:
        print("The letter is already guessed.")
        return True 
    else: 
        return False

def check_guess(user_input:str, the_random_word:str) -> bool:
    return True if user_input in the_random_word else False

def update_mask_word(mask_word:str, user_input:str, the_random_word:str) -> str:
    for i in range(len(the_random_word)):
        if the_random_word[i] == user_input:
            mask_word = mask_word[:i] + user_input + mask_word[i+1:]
    return mask_word

def check_victory(mask_word:str, the_random_word:str):
    return True if mask_word == the_random_word else False

def print_victory_or_loos(gueeses_left:int) -> None:
    if gueeses_left ==0:
        print("You lost! Maybe next time..")
    else:
        print(" 😁 👌 👍 😍   Yow won!!! Good job.   😁 👌 👍 😍")

def manage_the_game(num_of_guesses:int, wordes_list:list) -> None:
    the_random_word = choose_random_word(wordes_list)
    the_mask_of_word = create_mask_word(the_random_word)
    guesses_left = num_of_guesses
    guessed_letters = set("")
    is_victory = False
    while guesses_left and not is_victory:
        print_game_status(the_mask_of_word, guesses_left, guessed_letters)
        user_guess = get_user_input(guessed_letters)
        is_guess_true = check_guess(user_guess, the_random_word)
        if is_guess_true:
            the_mask_of_word = update_mask_word(the_mask_of_word, user_guess, the_random_word)
            is_victory = check_victory(the_mask_of_word, the_random_word)
        else:
            guesses_left -= 1
            guessed_letters = update_guessed_letters_set(guessed_letters,user_guess)
    
    print_victory_or_loos(guesses_left)

def main(num_of_guesses:int, wordes_list:list) -> None:
    manage_the_game(num_of_guesses, wordes_list)


main(NUM_OF_GUESSES, WORDS_LIST)