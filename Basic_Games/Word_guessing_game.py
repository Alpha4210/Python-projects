# This is a word guessing game where the user will try to guess the word.
import emoji as emj
import termcolor as tc
import time
import random as rdm
import threading
import csv

# This is a timer made for the game.
# def countdown(timer):
#     while timer:
#         mins, secs = divmod(timer, 60)
#         timeformat = '{:02d}:{:02d}'.format(mins, secs)
#         print(timeformat, end='\r')
#         time.sleep(1)
#         timer -= 1
#     print("\nTime's up! You didn't guess the word in time.")

# This is a background timer
# def background_timer(duration, interval=1):
#     """Runs a background timer for the given duration (in seconds) with the specified interval (in seconds)."""
#     start_time = time.time()
#     while time.time() - start_time < duration:
#         elapsed_time = int(time.time() - start_time)
#         print(f"Timer: {elapsed_time} seconds", end='\r')
#         time.sleep(interval)
#     print(f"Timer finished! Duration: {duration} seconds")

#Defining the functions for different difficulties

def easy_diff():
    '''This function is used if the user choses easy difficulty
    
    Length of word to guess = 5 letters
    Chances for guessing the word = 8
    Time limit for guessing the word = 2 minutes or 120 seconds
    
    '''
    length_of_word = 5
    chances = 8
    # time_for_guessing = 120 # time here  is in seconds
    
    words = "apple, bread, cloud, dance, earth, flame, grace, heart, ivory, joker, khaki, lemon, movie, night, ocean, peach, quiet, radio, sugar, tiger, uncle, vault, water, yeast, zebra"
    word_list = words.split(',')
    selected_word = rdm.choice(word_list)
    print("You have 120 seconds or 2 minutes to answer")

    for i in range(chances):
        a = input("Guess the word: \n")
        if a==selected_word:
            print("Congrats you guessed the correct word!")
            print(f"Name:{name}\nScore:{(i+1)}")
            break
        elif a!=selected_word:
            print("Try again")
            if i == chances - 1:
                print(f"Better luck next time, the correct word was {selected_word}")
                break
            continue
        

def med_diff():
    '''This function is used if the user choses medium difficulty
    
    Length of word to guess = 5 letters
    Chances for guessing the word = 8
    Time limit for guessing the word = 1:30 minutes or 90 seconds
    
    '''
    length_of_word = 7
    chances = 8
    # time_for_guessing = 120 # time here  is in seconds
    
    # words = "already", "picture", "journey", "believe", "success", "tension", 
    # "example", "cabinet", "freedom", "thought", "chapter", "chances",
    # "courage", "capture", "control", "fortune", "grammar", "holiday",
    # "justice", "respect", "fashion", "teacher", "victory", "seventh",
    # "sunrise", "history", "library", "natural", "trouble", "remains",
    # "variety", "wonders", "whisper", "weather", "universe", "balance",
    # "fashion"
    word_list = [
    "already", "picture", "journey", "believe", "success", "tension", 
    "example", "cabinet", "freedom", "thought", "chapter", "chances",
    "courage", "capture", "control", "fortune", "grammar", "holiday",
    "justice", "respect", "fashion", "teacher", "victory", "seventh",
    "sunrise", "history", "library", "natural", "trouble", "remains",
    "variety", "wonders", "whisper", "weather", "universe", "balance",
    "fashion"
]
    selected_word = rdm.choice(word_list)
    print("You have 90 seconds or 1:30 minutes to answer")

    for i in range(chances):
        a = input("Guess the word: \n")
        if a==selected_word:
            print("Congrats you guessed the correct word!")
            print(f"Name:{name}\nScore:{(i+1)}")
            break
        elif a!=selected_word:
            print("Try again")
            if i == chances - 1:
                print(f"Better luck next time, the correct word was {selected_word}")
                break
            continue
        
        
def hard_diff():
    '''This function is used if the user choses hard difficulty
    
    Length of word to guess = 9 letters
    Chances for guessing the word = 8
    Time limit for guessing the word = 1 minute or 60 seconds
    
    '''
    length_of_word = 5
    chances = 8
    # time_for_guessing = 120 # time here  is in seconds
    
    word_list = [
    "adventure", "beautiful", "celebrate", "chocolate", "happiness", 
    "important", "wonderful", "fantastic", "excellent", "harmonize", 
    "knowledge", "literature", "discovery", "president", "incredible", 
    "lifetime", "strategies", "brilliant", "fascinate", "container", 
    "confident", "relevance", "superhero", "condition", "permanent", 
    "numerical", "generally", "assistant", "automatic", "objective"
]
    selected_word = rdm.choice(word_list)
    print("You have 60 seconds or 1 minute to answer")

    for i in range(chances):
        a = input("Guess the word: \n")
        if a==selected_word:
            print("Congrats you guessed the correct word!")
            print(f"Name:{name}\nScore:{(i+1)}")
            break
        elif a!=selected_word:
            print("Try again")
            if i == chances - 1:
                print(f"Better luck next time, the correct word was {selected_word}")
                break
            continue
        
def custom_diff():
    '''This function is used if the user choses custom difficulty
    
    Length of word to guess = 5/7/9 letters
    Chances for guessing the word = n
    Time limit for guessing the word = n
    
    '''
    length_of_word = int(input("Enter the length of word you want to guess(5/7/9): "))
    chances = int(input("Enter the number of chances you want to guess the word within: "))
    time_req = int(input("Enter the time in which you want to guess the word within(in seconds): "))
    
    # time_for_guessing = 120 # time here  is in seconds
    
    five_letters_word_list = [
    "apple", "brave", "crane", "drift", "eagle", "flame", "globe", 
    "honey", "ivory", "jelly", "karma", "lemon", "mango", "noble", 
    "ocean", "pearl", "queen", "raven", "solar", "tiger", "ultra", 
    "vivid", "whale", "xenon", "young", "zebra"
]
    seven_leters_word_list = [
    "already", "picture", "journey", "believe", "success", "tension", 
    "example", "cabinet", "freedom", "thought", "chapter", "chances",
    "courage", "capture", "control", "fortune", "grammar", "holiday",
    "justice", "respect", "fashion", "teacher", "victory", "seventh",
    "sunrise", "history", "library", "natural", "trouble", "remains",
    "variety", "wonders", "whisper", "weather", "universe", "balance",
    "fashion"
]
    nine_letters_word_list = [
    "adventure", "beautiful", "celebrate", "chocolate", "happiness", 
    "important", "wonderful", "fantastic", "excellent", "harmonize", 
    "knowledge", "literature", "discovery", "president", "incredible", 
    "lifetime", "strategies", "brilliant", "fascinate", "container", 
    "confident", "relevance", "superhero", "condition", "permanent", 
    "numerical", "generally", "assistant", "automatic", "objective"
]
    if length_of_word==5:
        selected_word = rdm.choice(five_letters_word_list)
        print(f"You have {time_req} seconds to answer")
        for i in range(chances):
            a = input("Guess the word: \n")
            if a==selected_word:
                print("Congrats you guessed the correct word!")
                print(f"Name:{name}\nScore:{(i+1)}")
                break
            elif a!=selected_word:
                print("Try again")
                if i == chances - 1:
                    print(f"Better luck next time, the correct word was {selected_word}")
                    break
                continue
    elif length_of_word==7:
        selected_word = rdm.choice(seven_letters_word_list)
        print(f"You have {time_req} seconds to answer")
        for i in range(chances):
            a = input("Guess the word: \n")
            if a==selected_word:
                print("Congrats you guessed the correct word!")
                print(f"Name:{name}\nScore:{(i+1)}")
                break
            elif a!=selected_word:
                print("Try again")
                if i == chances - 1:
                    print(f"Better luck next time, the correct word was {selected_word}")
                    break
                continue
    elif length_of_word==9:
        selected_word = rdm.choice(nine_letters_word_list)
        print(f"You have {time_req} seconds to answer")
        for i in range(chances):
            a = input("Guess the word: \n")
            if a==selected_word:
                print("Congrats you guessed the correct word!")
                print(f"Name:{name}\nScore:{(i+1)}")
                break
            elif a!=selected_word:
                print("Try again")
                if i == chances - 1:
                    print(f"Better luck next time, the correct word was {selected_word}")
                    break
                continue
        
    else:
        print("Invalid input!")    
    
            
# The game will run unless the user quits it.
if __name__=='__main__':
    while True:
        # Starting the game by asking the user his/her name and welcoming them
        tc.cprint("To begin the game please follow the below instructions:","blue", attrs=["bold"])
        name = input("Please enter your name: ")
        print(emj.emojize(f"Hello {name}, welcome to our word guessing game :wave:",language='alias'))

        print("\n") #giving a line gap

        # Asking the difficulty from the user
        print("Please select the difficulty for the game,", tc.colored("please chose it carefully as it cannot be changed after.", attrs=["bold"]))
        print('''You can select from the following difficulties:''',
            tc.colored('''
            1. Easy
            ''', "green"),
            tc.colored(''' 
            2. Medium
            ''', "yellow"),
            tc.colored('''
            3. Hard
            ''', "red"),
            '''
            4. Custom
            ''')

        diff = input("Choose a difficulty from one of the above: ")
        if diff.lower() == 'easy':
            easy_diff()
            break
        elif diff.lower() == 'medium':
            med_diff()
            break
        elif diff.lower() == 'hard':
            hard_diff()
            break
        elif diff.lower() == 'custom':
            custom_diff()
            break
        else:
            print("Please give a valid input")
    
print("Thanks for playing! We were provide further updates according to the suggestions given by you")


with open('word_guessing_game_suggestions.csv','a',newline='') as suggestions_file:
    writer = csv.writer(suggestions_file)
    suggestion = input("Enter your suggestion(If you have no suggestion then just write None): ")
    data = [name,suggestion]
    writer.writerow(data)

    