import csv
with open('word_guessing_game_suggestions.csv','a',newline='') as suggestions_file:
    writer = csv.writer(suggestions_file)
    suggestion = input("Enter your suggestion(If you have no suggestion then just write None): ")
    # data = [name,suggestion]
    writer.writerow(['Name','Suggestion'])