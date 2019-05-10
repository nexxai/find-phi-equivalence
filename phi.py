#!/usr/local/bin/python3

import sys
import math
import datetime
import time
import random
from decimal import *

# The golden ratio
phi = (1 + math.sqrt(5)) / 2

counter = 0
base_number = 1
max_rounds = 0

def find_phi_equivalence(first, second):
    global counter
    global base_number
    global max_rounds
    
    counter = counter + 1

    next_num = int(first) + int(second)
    ratio = int(second) / int(first)
    difference = abs(Decimal(ratio) - Decimal(phi))
    
    if difference != 0:
        return [second, next_num]

    if counter > max_rounds:
        max_rounds = counter
        print_status(first, second, counter, Decimal(difference))

    if base_number % 250 == 0:
        print_status(first, second, counter, Decimal(difference))

    base_number = base_number + 1

def big_random_number():
    n = 10000
    number = ''.join(["%s" % random.randint(0, 9) for num in range(0, n)])
    return int(number)

def print_status(first, second, counter, difference):
    timestamp = datetime.datetime.fromtimestamp(
        time.time()).strftime('%Y-%m-%d %H:%M:%S')
    print("[COMPLETE] STARTING VALUES: {} & {}".format(str(first), str(second)))
    print("[{}] Ratio = Phi (to 49 decimal places) after {} steps".format(timestamp, str(counter)))
    print("[VAL] Difference: {}".format(Decimal(difference)))

first = big_random_number()
second = big_random_number()
last_fib = find_phi_equivalence(first, second)
while 0 < 1:
    if last_fib is not None:    
        last_fib = find_phi_equivalence(last_fib[0], last_fib[1])
    else:
        counter = 0
        first = big_random_number()
        second = big_random_number()
        last_fib = find_phi_equivalence(first, second)
