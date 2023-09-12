'''
The random Candyman puts candy sticks in his candy bag.
Theyhavevarious sizes and can be green or red. 
When someone asks for a candy stick, the Candyman 
randomly gets one from his bag.
The Candyman would like to inform people about the average size 
of the following candy stick that will be chosen and the
chance to have a red one. But he wants to keep his bag contents private 
and may be too lazy to inspect the bag by himself. Fortunately, 
the Candyman knows basic mathematics and can remember a few numbers. 
How can the Candyman inform people about his candies?
You have to implement a CandyMan class or structure containing a 
list of candy sticks. The class must have the methods:
add_candy
get_a_random_candy
get_average_size
get_red_candy_chance.
You are forbidden to browse the candy list when calling the last two 
functions, and you can rely only on 3 numbers the Candyman can remember. 
The quantities will stay reasonable, and the Candyman will never have 
billions of candy sticks in his bag.
'''

import random

min_size = 1
max_size = 5

class Candyman:

    def __init__(self):
        self.size_candies = 0
        self.num_candies = 0
        self.num_red = 0

    def add_candy(self, color, size):
        self.size_candies += size
        self.num_candies += 1
        if color == "red":
            self.num_red += 1

    def get_average_size(self):
        if self.num_candies != 0:
            return self.size_candies / self.num_candies
        else:
            return 0
    
    def get_red_candy_chance(self):
        if self.num_candies != 0:
            return self.num_red / self.num_candies
        else:
            return 0
        
    def get_a_random_candy(self):
        rand_num = random.random()
        candy_size = random.randint(min_size, max_size)

        while (candy_size > self.size_candies) or ((self.size_candies - candy_size) <= (self.num_candies - 1) * min_size and self.num_candies > 1):
            candy_size = random.randint(min_size, max_size)
        
        self.size_candies -= candy_size
        self.num_candies -= 1

        if rand_num < self.get_red_candy_chance():
            color = "Red"
            self.num_red -= 1
        else:
            color = "Green"
        
        return(f"{color} candy, size {candy_size}")
    
candy_man = Candyman()
candy_man.add_candy("red", 3)
candy_man.add_candy("green", 5)
candy_man.add_candy("red", 2)
candy_man.add_candy("green", 5)
candy_man.add_candy("green", 5)
candy_man.add_candy("green", 5)
# candy_man.add_candy("red", 2)

print("Average size: ", candy_man.get_average_size())
print("Red chance: ", candy_man.get_red_candy_chance())
print("----------------------")
print("Random candy: ", candy_man.get_a_random_candy())
print("----------------------")
print("Average size: ", candy_man.get_average_size())
print("Red chance: ", candy_man.get_red_candy_chance())
print("----------------------")
print("Random candy: ", candy_man.get_a_random_candy())
print("----------------------")
print("Average size: ", candy_man.get_average_size())
print("Red chance: ", candy_man.get_red_candy_chance())