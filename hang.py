//hangman code logic


import random
import hangman_words
# from clear import clear
end_of_game= False
lives = 6
from hangman_art import logo
print(logo)
chosen_word = random.choice(hangman_words.word_list)
# print(f'Pssst, the solution is {chosen_word}.')
display = []
word_length = len(chosen_word)
for _ in range(word_length):
    display += "_"
while not end_of_game:

    guess = input("Guess a letter: ").lower()
    # clear()
    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives= lives-1
        if lives == 0:
            end_of_game = True
            print("you loose")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("you won")
    from hangman_art import stages
    print(stages[lives])