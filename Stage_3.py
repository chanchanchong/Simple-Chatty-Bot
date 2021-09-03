# Description
# Keep improving your bot by developing new skills for it. We
# suggest a simple guessing game that will predict the age of a 
# user.

# It's based on a simple math trick. First, take a look at this
# formula:
# age = (remainder_3 * 70 + remainder_5 * 21 + remainder_7 * 15) % 105

# The numbers remainder_3, remainder_5, and remainder_7 are the
# remainders of division by 3, 5, 7 respectively.

# It turns out that for each number ranging from 0 to 104 the
# calculation will result in the number itself. This perfectly fits the
# ordinary age range, doesn't it? Ask a user for the remainders
# and use them to guess the age!

# Objective
# At this stage, you will introduct yourself to the bot. It will greet
# you by your name and then try to guess your age using
# arithmetic operations.

# Your program should print the following lines:
# Hello, My name is Aid.
# I was created in 2020.
# Please, remind me your name.
# What a great name you have, Max!
# Let me guess your age.
# Enter remainders of dividing your age by 3, 5, 7.
# Your age is {your_age}; that's a good time to start programming

# Read three numbers from the standard input. Assume that all
# the numbers will be given on separate lines.

# Instead of {your_age}, the bot will print the age determined
# according to the special formula discussed above.

# Example 
# The greater-than symbol followed by a space ( > ) represents
# the user input. Note that it's not part of the input.

# Example 1: a dialogue with the bot
# Hello! My name is Aid.
# I was created in 2020.
# Please, remind me your name.
# > Max
# What a great name you have, Max!
# Let me guess your age.
# Enter remainders of dividing your age by 3, 5, 7.
# > 1
# > 2
# > 1
# Your age is 22; that's a good time to start programmming!

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
        print("Please, remind me your name.")
        print(f'What a great name you have {input()}!')

    def guess_age(self):
        print("Let me guess your age.")
        print("Enter remainders of dividing your age by 3, 5, 7")

        def age(_):
            return (lambda a, b, c:
                    (a * 70 + b * 21 + c * 15)
                    % 105)(rem[0], rem[1], rem[2])
        rem = [int(input()) for _ in range(3)]
        print(f"Your age is {age(rem)}; that's a good time to start programming!")

def main():
    bot = Bot("Aid", 2021)
    bot.greet()
    bot.ask_creator()
    bot.guess_age()

if __name__ == "__main__":
    main()