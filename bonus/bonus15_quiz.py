import random


def find_random_number(low_number, up_number):
    result = random.randint(low_number, up_number)
    return result


user_low_no = int(input("Enter the lower bound: "))
user_up_no = int(input("Enter the upper bound: "))

print(find_random_number(user_low_no,user_up_no))
