# Description
# Now you will teach your bot to count. It's going to become an
# expert in numbers!

# Objective 
# At this stage, you will program the bot to count from 0 to any
# positive number users enter.

# Example
# The greater-than symbol followed by a space ( > )
# represents the user input. Note that it's not part of the input.

# Example 1: a dialogue with the new version of the bot

# Hello! My name is Aid.
# I was created in 2020.
# Please, remind me your name.
# > Max
# What a great name you have, Max!
# Let me guess your age.
# Enter remainders of dividing your age by 3, 5, and 7.
# > 1
# > 2
# > 1
# Yoir age is 22; that's a good time to start programming!
# Now I will prove to you that I can count to any number you want.
# > 5
# 0 !
# 1 !
# 2 !
# 3 !
# 4 !
# 5 !
# Completed, have a nice day!

class Bot:
    def __init__(self, bot_name, birth_year):
        self.bot_name = bot_name
        self.birth_year = birth_year
    
    def greet(self):
        print(f'Hello! My name is {self.bot_name}')
        print(f'I was created in {self.birth_year}')
    
    def ask_creator(self):
        print('Please, remind me your name.')
        print(f'What a great name you have {input()}')
    
    def guess_age(self):
        print('Let me guess your age.')
        print("Enter remainders of dividing your age by 3, 5, 7")

        def age(_):
            return (lambda a, b, c:
                    (a * 70 + b * 21 + c * 15)
                    % 105)(rem[0], rem[1], rem[2])
        rem = [int(input()) for _ in range(3)]
        print(f"Your age is {age(rem)}; that's a good time to start programming.")
    
    def count(self):
        print('Now I will prove to you that I can count to any number you want.')
        print('\n'.join(f'{i} !' for i in range(int(input()) + 1)))
        print('Completed, have a nice day!')
def main():
    bot = Bot("Aid", 2021)
    bot.greet()
    bot.ask_creator()
    bot.guess_age()
    bot.count()

if __name__ == "__main__":
    main()