import time as Time

myString = "Machine Learning"


def count_string(string):
    print('Tedad horof reshte:', len(myString))


def count_e(string):
    count = 0
    for letter in myString:
        if letter == 'e':
            count += 1
    print('tedad horof "e" :', count)


def print_string(string):
    for i in range(15, -1, -1):
        Time.sleep(0.1)
        print(myString[i])


count_string(myString)
count_e(myString)
print_string(myString)
