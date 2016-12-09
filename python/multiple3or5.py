#!/usr/bin/env python3

def multiple3or5(num):
    output = 0
    index = 1
    while index < num:
        if index % 3 == 0 or index % 5 ==0:
            output += index
        index += 1

    return output


print(multiple3or5(1000))
