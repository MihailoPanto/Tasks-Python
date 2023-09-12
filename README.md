# Tasks-Python

First assignment

 Python tasks
1. Find all numbers that are divisible by 9 but are not a multiple of 5, between 1000 and 3000 (both included). The numbers should be printed in a comma-separated sequence on a single line.
2. Writeaprogramthatacceptsasequenceofwhitespaceseparatedwordsas input and prints the words after removing all duplicate words and sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice makes perfect and hello world again Then, the output should be: again and hello makes perfect practice world
3. Writeaprogramthatacceptsasentenceandcalculatethenumberofuppercase letters and lowercase letters. Suppose the following input is supplied to the program: Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9
4. Youaregivenalistofintegersasaninput.Returnalistwiththesameelements where all zeros are at the end of the array.
Analyze why:
     def solution(nums):
         for i in nums:
             if 0 in nums:
                 nums.remove(0)
                 nums.append(0)
         return nums
isn’t the best solution.
5. TherandomCandymanputscandysticksinhiscandybag.Theyhavevarious sizes and can be green or red. When someone asks for a candy stick, the Candyman randomly gets one from his bag. The Candyman would like to inform people about the average size of the following candy stick that will be chosen and the chance to have a red one. But he wants to keep his bag contents private and may be too lazy to inspect the bag by himself. Fortunately, the Candyman knows basic mathematics and can remember a few numbers. How can the Candyman inform people about his candies?
You have to implement a CandyMan class or structure containing a list of candy sticks. The class must have the methods:
add_candy

      get_a_random_candy
     get_average_size
     get_red_candy_chance.
You are forbidden to browse the candy list when calling the last two functions, and you can rely only on 3 numbers the Candyman can remember. The quantities will stay reasonable, and the Candyman will never have billions of candy sticks in his bag.
