# Digital personal assistants help people to drive cars, plan their
# day, buy something online. In a sense, they are simplified
# versions of artificial intelligence with whom you can talk.

# In this project you will develop step by step a simple bot chat
# will help you study programming.

# Objective 
# For the first stage, you will write a bot who displays a greeting,
# its name, and the date of its creation. First impressions count!

# Your program should print the following lines:
# Hello! My name is {bot_name}.
# I was created in {birth_year}.

# Instead of {bot_name}, print any name you chooose and repleace
# {birth_year} with the current year (four digits).

# Example 
# Output:

# Hello! My name is Aid.
# I was created in 2020.

# You can change the text if you want but print exactly two lines.
# Next, we will use Aid and 2020 as your bot's name and its birth
# year, but you can change it if you need to.

# write your code here
class Bot:
    def __init__(self, bot_name, birth_year):
        self.bot_name = bot_name
        self.birth_year = birth_year
    
    def greet(self):
        print(f'Hello! My name is {self.bot_name}')
        print(f'I was created in {self.birth_year}')

def main():
    bot = Bot("Aid", 2021)
    bot.greet()

if __name__ == "__main__":
    main()