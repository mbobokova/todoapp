"""
#ex1
    rate = 2
    dollars = float(input('dolar '))
    euro = dollars * 2
   print(euro)
"""

"""
#ex2 
    ranking = ['John', 'Sen', 'Lisa']
    
    rank_number = int(input("Enter rank number: "))
    rank_number -= 1
    print(ranking[rank_number])
"""

"""
#ex3 INDEX
    ranking = ['John', 'Sen', 'Lisa']
    
    rank_person = (input("Enter person's name: "))
    rank_number = ranking.index(rank_person)
    rank_number += 1
    
    print(rank_number)
"""

"""
filenames = ['document', 'report', 'presentation']

for index, file in enumerate(filenames):
    row = f"{index}-{file.capitalize()}.txt"
    print(row)
 """

"""
ips = ['100.122.133.105', '100.122.133.111']

user_action = int(input("Enter the index of the IP you want: "))
print("You chose", ips[user_action])
"""

""" ADD NEW STRING TO NEW LINE TO TXT FILE
file = open(f"../files_bonus/members.txt", 'r')
members = file.readlines()
file.close()

add_member = input("Add a new member: ") + "\n"
members.append(add_member)

file = open(f"../files_bonus/members.txt", 'w')
file.writelines(members)
file.close()
"""

""" CREATE FILE AND ADD STRING TO EACH
filenames = ['doc2.txt', 'report2.txt', 'presentation2.txt']

for filename in filenames:
    file = open(f"../files_bonus/{filename}", 'w')
    file.write("Hello")
"""

""" READING FILES
filenames = ['a.txt', 'b.txt', 'c.txt']
for filename in filenames:
    file = open(f"../files_bonus/{filename}", 'r')
    files = file.read()
    file.close()
    print(files)
"""

"""
usernames = ["john 1990", "alberta1970", "magnola2000"]
usernames = [len(username) for username in usernames]
print(usernames)
"""

"""
with open("files/docs.txt", "r") as file:
    file.read()
"""

""" TRY EXCEPT
try:
    total_value = float(input("Enter total value: "))
    if total_value == 0:
        exit("Your total value cannot be zero.")
    value = float(input("Enter value: "))
    percentage = value/total_value * 100
    print(f"That is {percentage}%")
except ValueError:
    print("You need to enter a number. Run the program again.")
"""
"""
colors = [11, 34, 98, 43, 45, 54, 54]

for color in colors:
    if color > 50:
        print(color)


def get_max():
    grades = [9.6, 9.2, 9.7]
    grades_max = max(grades)
    grades_min = min(grades)
    grades_max_min = f"Max: {grades_max}, Min: {grades_min}"
    return grades_max_min


max_grades = get_max()
print(max_grades)

-------------------------------------------------------------
def prepare(text):
    text = text.title()
    text = text.strip()
    return text


print(prepare("hello    "))

----------------------------------------------

def liters_to_m3(liter):
    m3 = liter / 1000
    return m3

******************//////////////////////////******************

def strength(password):
    result = {}

    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    uppercase = False

    for i in password:
        if i.isdigit():
            digit = True

        if i.isupper():
            uppercase = True

    result["digits"] = digit
    result["upper-case"] = uppercase

    if all(result.values()):
        # Return "Strong Password" if all attributes are True
        return "Strong Password"
    else:
        # Return "Weak Password" if any attribute is False
        return "Weak Password"
    
    
    
-----------------*******************--------------------------

def foo(list):
    list_sum = sum(list)
    list_count = len(list)
    avarage = list_sum / list_count
    return avarage

numbers = [10, 20, 30, 40]


print(foo(numbers)

-----------------*******--------------------------

def foo(name):
    name = name.title()
    text = f"Hi {name}"
    return text


print(foo("zuyka"))

--------------------------



def concatenates(first, second):
    for i in first:
        text = second.append(i)
        return text


print(concatenates("Zuzka", "hovno"))

user_temperature = input("Temperature: ")


--------------------------

user_temperature = int(input("Temperature: "))

def check_temperature(input_temp):
    if input_temp > 7:
        return "Warm"
    elif input_temp <= 7:
        return "Cold"


print(check_temperature(user_temperature))

***************--------------------------******************


def foo(text):
    if len(text) < 8:
        return False
    elif len(text) >= 8:
        return True

print(foo("akoyeneviemco"))


***************--------------------------******************
"""


def weather(temperature):
    cold_temperature = 15
    hot_temperature = 25

    if temperature > hot_temperature:
        return "Hot"
    elif hot_temperature > temperature > cold_temperature:
        return "Warm"
    elif temperature < cold_temperature:
        return "Cold"

print(weather(10))
