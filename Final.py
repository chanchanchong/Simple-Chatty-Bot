# Description 
# At the final stage, you will improve your simple bot so that it can
# give you a test and check your answers. The test should be a 
# multiple-choice quiz about programming. Your bot has to repeat
# the test until you answer correctly and congratulate you upon
# completion.

# Objective 
# Your bot can ask anything you want, but there are two rules for
# your output:
# - the line with the test should end with the question mark
# - an option starts with a digit followed by the dot (1., 2.,
# 3., 4.)

# If a user enters an incorrect answer, the bot may print a
# message:
# Please, try again.

# The program should stop on the correct answer and print
# Congratulations, have a nice day! at the end.

# Example 
# The greater-than symbol followed by a space ( > ) represents
# the user input. Note that it's not part of the input.

# Example 1: a dialogue with the final version of your bot

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
# Let's test your programming knowledge.
# Why do we use methods?
# 1. To repeat a statement multiple times.
# 2. To decompose a program into sevral small subroutines.
# 3. To determine the execution time of a program.
# 4. To interrupt the execution of a program.
# > 4
# Please, try again.
# > 2
# Completed, have a nice day!
# Congratulations, have a nice day!

# The program must end with the Congratulations, have a nice
# day! message.

# Use the provided template to simplify your work. You can
# change the text if you want. Please note that we use functions
# to make it easy to understand the program and add new code tho
# it or edit later.

class Bot:
    def __init__(self, bot_name, birth_year):
        self.bot_name = bot_name
        self.birth_year = birth_year
        self.name = None
    
    def greet(self):
        print(f'Hello! My name is {self.bot_name}')
        print(f'I was created in {self.birth_year}')
    
    def ask_creator(self):
        self.name = input("Please, remind me your name.")
        print("What a great name you have ", self.name)
    
    def guess_age(self):
        print("Let me guess your age.")
        print("Enter remainders of dividing your age by 3, 5, and 7")
    
        def age(_):
            return (lambda a, b, c:
                    (a * 70 + b * 21 + c * 15)
                    % 105)(rem[0], rem[1], rem[2])
        
        rem = [int(input()) for _ in range(3)]
        print(f"Your age is {age(rem)}; that's a good time to start programming.")

    def count(self):
        print("Now I will prove to you that I can count to any number you want.")         
        print("\n".join(f'{i} !' for i in range(int(input() + 1))))

    def test(self):
        print("Let's test your programming knowledge.")
        print("Why do we use methods?")
        print("1. To repeat a statement multiple times.")
        print("2. To decompose a program into several small subroutines.")
        print("3. To determine the execution time of a program.")
        print("4. To interrupt the execution of a program.")
        i = int(input())
        while i != 2:
            print("Please, try again.")
            i = int(input())
def main():
    bot = Bot("Aid", 2021)
    bot.greet()
    bot.ask_creator()
    bot.guess_age()
    bot.count()
    bot.test()
if __name__ == "__main__":
    main()