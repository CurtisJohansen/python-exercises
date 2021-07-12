# 1 - Conditional Basics
#   a. prompt the user for a day of the week, print out whether the day is Monday or not

day_of_week = input ("Please enter a day of the week: ")

if day_of_week ==("Monday") or day_of_week ==("monday"):
    print("You have chosen Monday.")
else:
    print("You did not choose Monday.")

#   b. prompt the user for a day of the week, print out whether the day is a weekday or a weekend

day_of_week = input ("Please enter a day of the week: ")

if day_of_week ==("Saturday") or day_of_week ==("saturday") or day_of_week ==("sunday") or day_of_week ==("Sunday"):
    print("You have chosen a day in the weekend.")
else:
    print("You choosen a weekday.")

#   c. create variables and make up values for
#       the number of hours worked in one week
#       the hourly rate
#       how much the week's paycheck will be
# write the python code that calculates the weekly paycheck. You get paid time and a half if you work more than 40 hours

hours_worked = 45
hourly_rate = 75
overtime_hours = hours_worked - 40
overtime_pay = overtime_hours * hourly_rate * 0.5
weekly_paycheck = hours_worked * hourly_rate + overtime_pay

if hours_worked > 40:
    overtime_hours
else:
    overtime_pay = 0
    
print (weekly_paycheck)

# 2 - Loop Basics
#   a. While
#       Create an integer variable i with a value of 5.
#       Create a while loop that runs so long as i is less than or equal to 15
#       Each loop iteration, output the current value of i, then increment i by one.

i = 5
while i <= 15:
    print(i)
    i += 1

# Create a while loop that will count by 2's starting with 0 and ending at 100. Follow each number with a new line.

i = 0
while i <= 100:
    print(i)
    i += 2

# Alter your loop to count backwards by 5's from 100 to -10.

i = 100
while i >= -10:
    print(i)
    i -= 5

# Create a while loop that starts at 2, and displays the number squared on each line while the number is less than 1,000,000. Output should equal:

i = 2
while i <= 1000000:
    print(i)
    i = i ** 2

# b. For Loops
#       i. Write some code that prompts the user for a number, 
#           then shows a multiplication table up through 10 for that number.

user_number = int(input ("Please enter a number. "))
for i in range(1, 11):
    print (user_number, "x", i, "=", i*user_number)

#       ii. Create a for loop that uses print to create the output shown below.

for i in range(10):
    print(str(i) * i)

# c. break and continue
#   i. Prompt the user for an odd number between 1 and 50. 
#      Use a loop and a break statement to continue prompting the user if they enter invalid input. 
# Hint: use the isdigit method on strings to determine this). 
# Use a loop and the continue statement to output all the odd numbers between 1 and 50, 
# except for the number the user entered.

while True:
    
    odd_number = input("Please enter an odd number between 1 and 50 ")
    if odd_number.isdigit():
        odd_number = int(odd_number)
        if odd_number % 2 == 0 and odd_number <= 50:
            continue
        break
i = 1
while i <= 50:
    if i == odd_number:
        print("Yikes! Skipping number: ", i)
        i += 2
    else:
        print("Here is an odd number: ", i)
        i += 2

# d. The input function can be used to prompt for input and use that input in your python code. 
#    Prompt the user to enter a positive number 
#    and write a loop that counts from 0 to that number. 
#    (Hints: first make sure that the value the user entered is a valid number, also note that the input function returns a string, so you'll need to convert this to a numeric type.)

while True:
    
    positive_number = input("Please enter a positive number ")
    if positive_number.isdigit():
        positive_number = int(positive_number)
        if positive_number > 0:
            break
for number in range(0, positive_number + 1):
    print(number)

# e. Write a program that prompts the user for a positive integer. Next write a loop that prints out the numbers from the number the user entered down to 1.

while True:
    
    positive_integer = input("Please enter a positive integer ")
    if positive_integer.isdigit():
        positive_integer = int(positive_integer)
        if positive_integer <= 0:
            continue
        break
for number in range(positive_integer, 0, -1):
    print(number) 

# 3. Fizzbuzz
# One of the most common interview questions for entry-level programmers is the FizzBuzz test. 
# Developed by Imran Ghory, the test is designed to test basic looping and conditional logic skills.

#       Write a program that prints the numbers from 1 to 100.
#       For multiples of three print "Fizz" instead of the number
#       For the multiples of five print "Buzz".
#       For numbers which are multiples of both three and five print "FizzBuzz".

for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")
        continue
    elif number % 3 == 0:
        print("fizz")
        continue
    elif number % 5 == 0:
        print("buzz")
    else:
        print(number)

# 4. Display a table of powers.

#       Prompt the user to enter an integer.
#       Display a table of squares and cubes from 1 to the value entered.
#       Ask if the user wants to continue.
#       Assume that the user will enter valid data.
#       Only continue if the user agrees to.

while True:
    pos_int = input("Please enter a positive integer ")
    if pos_int.isdigit():
        if int(pos_int) > 0:
            break
will_continue = input("Would you like to continue and print a table of powers? Enter y or Yes to continue ")
if will_continue.lower().startswith('y'):
    pos_int = int(pos_int)        
    print()
    print("number | squared | cubed")
    print("------ | ------- | -----")
    for number in range(1, pos_int + 1):
        number_squared = number ** 2
        number_cubed = number ** 3
        print(f"{number:<6} | {number_squared:<7} | {number_cubed:<5}")

# Bonus: Research python's format string specifiers to align the table
# 5. Convert given number grades into letter grades.

# Prompt the user for a numerical grade from 0 to 100.
# Display the corresponding letter grade.
# Prompt the user to continue.
# Assume that the user will enter valid integers for the grades.
# The application should only continue if the user agrees to.

# Grade Ranges:

#   A : 100 - 88
#   B : 87 - 80
#   C : 79 - 67
#   D : 66 - 60
#   F : 59 - 0

while True:

    numbered_grade = int(input("Please enter a numbered grade "))

    if numbered_grade >= 88:
        print("A")
    elif numbered_grade >= 80:
        print("B")
    elif numbered_grade >= 67:
        print("C")
    elif numbered_grade >= 60:
        print("D")
    else:
        print("F")
    
    wants_continue = input("Would you like to continue? Enter y or Yes ")
    if wants_continue.lower() not in ["y", "yes"]:
        break

# Bonus
# Edit your grade ranges to include pluses and minuses (ex: 99-100 = A+).

while True:

    numbered_grade = int(input("Please enter a numbered grade "))

    if numbered_grade >= 97:
        print("A+")
    elif numbered_grade >= 91:
        print("A")
    elif numbered_grade >= 88:
        print("A-")
    elif numbered_grade >= 86:
        print("B+")
    elif numbered_grade >= 83:
        print("B")       
    elif numbered_grade >= 80:
        print("B-")
    elif numbered_grade >= 76:
        print("C+")
    elif numbered_grade >= 70:
        print("C") 
    elif numbered_grade >= 67:
        print("C-")
    elif numbered_grade >= 65:
        print("D+")
    elif numbered_grade >= 63:
        print("D")
    elif numbered_grade >= 60:
        print("D-")
    else:
        print("F")
    
    wants_continue = input("Would you like to continue? Enter y or Yes ")
    if wants_continue.lower() not in ["y", "yes"]:
        break

# 6. Create a list of dictionaries where each dictionary represents a book that you have read. Each dictionary in the list should have the keys title, author, and genre. Loop through the list and print out information about each book.

# Prompt the user to enter a genre, then loop through your books list and print out the titles of all the books in that genre.