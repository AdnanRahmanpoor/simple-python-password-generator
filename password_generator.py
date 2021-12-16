import random

alpha = 'abcdefghijklmnopqrstuvwxyz'
cap_alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '1234567890'
symbols = '!@#$%^&*()'

def pass_gen():
    length = int(input("How long do you want your password to be? "))
    chars = alpha + cap_alpha + num + symbols
    for i in range(length):
        password = random.choice(chars)
        print(password, end='')


pass_gen()