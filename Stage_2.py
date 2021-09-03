# Description 
# The greeting part is great, but chatbots are also supposed to
# interact with a user. It's time to implement this functionality.

# Objective
# At this stage, you will introduce yourself to the bot so that it can
# greet you by your name.

# Your program should print the following lines:
# Hello! My name is Aid.
# I was created in 2020.
# Please, remind me your name.
# What a great name you have, {your_name}!

# You may change the name and the creation year of your bot if
# you want. 

# Instead of {your_name}, the bot must print your name entered
# from the standard input.

# Example 
# The greater-than symbol followed by a space ( > ) represents
# the user input. Not that it's not part of the input.

# Example 1: a dialogue with the bot
# Hello! My name is Aid.
# I was created in 2020.
# Please, remind me your name.
# > Max
# What a great name you have, Max!

# Use the provided template to simplify your work. You can
# change the text, but not the number of printed lines.

class Bot:
    def __init__(self, bot_name, birth_year):
        self.bot_name = bot_name
        self.birth_year = birth_year
    
    def greet(self):
        print(f'Hello! My name is {self.bot_name}')
        print(f'I was created in {self.birth_year}')

    def ask_creator(self):
        print("Please, remind me your name. ")
        print(f'What a great name you have {input()}!')

def main():
    bot = Bot("Aid", 2021)
    bot.greet()
    bot.ask_creator()

if __name__ == "__main__":
    main()



