from aocd import get_data
import re

data = get_data(day=1, year=2023)

# num_dict = {"one" : '1', "two" : "2", "three" : '3', "four": '4', \
# "five": '5', "six": '6', "seven": '7', "eight": '8', "nine" : '9'}

num_dict = {"one" : 'o1e', "two" : "t2o", "three" : 't3e', "four": '4', \
"five": 'f5e', "six": '6', "seven": '7n', "eight": 'e8t', "nine" : 'n9e'}


def p1():
    total = 0
    for line in data.split('\n'):

        l = 0
        r = len(line) - 1

        while(not line[l].isnumeric()):
            l += 1

        while(not line[r].isnumeric()):
            r -= 1
        
        total += int(line[l] + line[r])

    return total

def p2():
    total = 0
    for line in data.split('\n'):
        for key, val in num_dict.items():
            line = line.replace(key, val)
        
        l = 0
        r = len(line) - 1

        while(not line[l].isnumeric()):
            l += 1

        while(not line[r].isnumeric()):
            r -= 1
        
        total += int(line[l] + line[r])
    
    return total

print(p1())
print(p2())
    
