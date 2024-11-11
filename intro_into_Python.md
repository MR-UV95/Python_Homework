Intro into Python Exercise

Exercise 1 : print() function  : Get your feet wet and have some fun with the universal first step of programming.
1-a 

# Replace "type here" on line 2 with "Hello World!"
print("Hello World!")

1-b
# You can assign "Hello World!" to the variable below on line 3.

my_text="Hello World!"
print(my_text)

Exercise 2 : Variables : Practice assigning data to variables with these Python exercises.
2-a

# Type here. Assign a number to the variable: glass_of_water

glass_of_water=3

print("I drank", glass_of_water, "glasses of water today.")

2-b

# Fill the print function so it prints glass_of_water

glass_of_water=3

glass_of_water=glass_of_water + 1


print(glass_of_water)

Exercise 3 : Data Types : Integer (int), string (str) and float are the most basic and fundamental building blocks of data in Python.
3-a

# Assign an integer to the variable, then print it.

men_stepped_on_the_moon=12
print(men_stepped_on_the_moon)

3-b
# Type a couple of words or a short sentence for your variable, then print it.

my_reason_for_coding="To learn python"
print(my_reason_for_coding)

3-c

# Assign a float with 2 decimals to the variable below. If you don't wan't to search the value you can check out Hint 1.

global_mean_sea_level_2018=21

# Type your code here.
global_mean_sea_level_2018=21.36


print(global_mean_sea_level_2018)

Exercise 9 : Strings : Basic string operations as well as many string methods can be practiced through 10+ Python String Exercises we have prepared for you.
9-a

# Assign the string below to the variable in the exercise.
"It's always darkest before dawn."

# Type your answer here.

str="It's always darkest before dawn."

print(str)

9-b
# By using first, second and last characters of the string, create a new string.

str="It's always darkest before dawn."

# Type your answer here.

ans_1="It."

print(ans_1)

9-c
# Replace the (.) with (!)
str="It's always darkest before dawn."

# Type your code here.

str = "It's always darkest before dawn!"

print(str)


Exercise 10 : len() function : Python’s len function tells the length of an object. It’s definitely a must know and very useful in endless scenarios. Whether it’s manipulating strings or counting elements in a list, len function is constantly used in computer programming.
10-a
# Using len() function find out how many items are in the list.

lst=[11, 10, 12, 101, 99, 1000, 999]

answer_1=len(lst)


print(answer_1)

10-b
# len() function can also tell the length of a string.
# Find out the length of the string given below.

msg="Be yourself, everyone else is taken."
# Type your code here.

msg_length=len(msg)


print(msg_length)


10-c
# How many keys are there in the dictionary?

dict={"Real Madrid": 13,"AC Milan": 7,"Bayern Munich":5 ,"Barcelona": 5, "Liverpool": 5}
#Type your answer here.

ans_1=len(dict)

print(ans_1)


Exercise 11 : .sort() method  : Practice sort method in Beginner Python Exercises and later on you’ll have the opportunity practice sorted function in Intermediate Python Exercises.
11-a
# Sort the list in ascending order with .sort() method.
lst=[11, 100, 99, 1000, 999]

#Type your answer here.

lst.sort()

print(lst)

11-b
# This time sort the countries in alphabetic order.

lst=["Ukraine", "Japan", "Canada", "Kazakhstan", "Taiwan", "India", "Belize"]

# Type your code here.

lst.sort()

print(lst)

11-c
# Now sort the list in descending order with .sort() method.

lst=[11, 100, 101, 999, 1001]

# Type your answer here.

lst.sort(reverse = True)

print(lst)

Exercise 12 : .pop() method  : A list method pop can be applied to Python list objects. It’s pretty straightforward but actually easy to confuse. These exercises will help you understand pop method better.
## 12-a
#Pop the last item of the list below.

lst=[11, 100, 99, 1000, 999]

# Type your answer here.

popped_item=lst.pop(4)
 
print(popped_item)
print(lst)

12-b
# Remove "broccoli" from the list using .pop and .index methods.

lst=["milk", "banana", "eggs", "bread", "broccoli", "lemons"]

# Type your code here.


item=lst.pop(4)


print(lst, item)

12-c
# Save Italy's GDP in a separate variable and remove it from the dictionary.

GDP_2018={"US": 21, "China": 16, "Japan": 5, "Germany": 4, "India": 3, "France": 3, "UK": 3, "Italy": 2}

# Type your answer here.

italy_gdp=GDP_2018.pop("Italy")


print(GDP_2018)
print(italy_gdp, "trillion USD")



