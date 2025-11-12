# cast from str to int
str_numbers = "456"
str_numbers_to_int = int(str_numbers)
print("Before casting :", str_numbers, ", the data type is", type(str_numbers))
print("After casting :", str_numbers_to_int, ", the data type is", type(str_numbers_to_int))

# casting from int to str
integer = 12345
integer_to_str = str(integer)
print("Before casting :", integer, ", the data type is", type(integer))
print("After casting :", integer_to_str, ", the data type is", type(integer_to_str))

# casting from int to bool
num_int = 1
num_bool = bool(num_int)
print(num_bool, type(num_bool))
num_int = 0
num_bool = bool(num_int)
print(num_bool, type(num_bool))

# Koding comparison operators
# Equal to
print(8 == 8)
# Not equal to
print(8 != 9)
# Greater than
print(8 > 9)
# Less than
print(8 < 9)
# Less than or equal to
print(8 <= 9)
# Greater than or equal to
print(9 >= 9)

# Koding logical operators
a = True
b = True
print(a and b)
print(a or b)
print(not b)
#logic
print(5 > 6 and 6 < 7)

#Koding arithmetic operators
e = 8
f = 2
# Summation
sum = e + f
print(f"The sum of e with f is : {sum}")
# Reduction
red = e - f
print(f"The reduction of e with f is : {red}")
# Multiplication
multi = e * f
print(f"The multipication of e with f is : {multi}")
# Division
divi = e / f
print(f"The quotient of e with f is : {divi}")
# Modulo
mod = e % f
print(f"The remainder of e with f is : {mod}")
# Power
pow = e ** f
print(f"The power of e of f is : {pow}")

#Koding Input Output
#Input
name = str(input("What is your name : "))
age = int(input("What's your age : "))
print("Name: ", name)
print("Age: ", age)

# normal print
print('Hi all! I am', name, 'age', age, 'years old')
# format print
print(f'Hi all! I am {name} age {age} years old')
# format print dengan format lama
print('Hi all! I am %s age %d years old' % (name, age))
# format output
print(30*"=")
print("Temperature Calculator Program")
print(30*"=")

#Koding Conditionals Dan Exception Handling
#Using If-Else
try:
    your_GPA = float(input("Enter your GPA: "))
    if 4.0 >= your_GPA >= 0.0:
        if 4.0 >= your_GPA >= 3.80:
            print(f"Damn you've got a magna cumlaude with your {your_GPA} GPA")
        elif 3.50 <= your_GPA < 3.80:
            print(f"Cool!! You've got a cumlaude with your {your_GPA} GPA")
        elif 3.00 <= your_GPA < 3.50:
            print(f"You've got a stable GPA tho")
        elif your_GPA < 3.0:
            print(f"You need a stable GPA")
    else:
        print(f"Sorry, your GPA {your_GPA} is out of range and invalid")
except:
    print("Please enter a valid GPA")

#Using match case
try:
    status_code = int(input("Enter your status code: "))
    print("Your code means")
    match status_code:
        case 200:
            print("Success!")
        case 400:
            print("Bad Request")
        case 401:
            print("Unauthorized")
        case 402:
            print("Payment Required")
        case 403:
            print("Forbidden")
        case 404:
            print("Not Found")
        case 500:
            print("Internal Server Error")
        case _:
            print("Unknown code")
except:
    print("Please enter a valid status code")

#Ternary
a = 3
b = "Even Numbers" if a % 2 == 0 else "Odd Numbers"
print(b)

#Using Loops
for i in range(5):
    print(i)

# For loop with range
for i in range(5):
    print("Data science is easy!")
print(50*"=")
for i in range(1, 5, 2):
    print("Data science is easy!")

word = "I want to master data science"
for letter in word:
    print(letter)

# You can use it with enumerate function
for m, n in enumerate(word):
    print(f"Index {m}. {n}")

# It can go backwards
for i in range(5, 1, -1):
    print("I want big data's")

#Keyword control
for i in range(5):
    if i == 2:
        continue # skip this loop when i is equal to 2
    if i == 4:
        break # stops the loop when i is equal to 4
    print(i)

#Using while loop
count = 0
while count < 4:
    print("Keep the spirits up interns!")
    count += 1