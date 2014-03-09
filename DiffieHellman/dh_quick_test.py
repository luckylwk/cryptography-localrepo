#!/usr/bin/python

from random import getrandbits

def print_line():
    print 20 * "--"


## Setup variables.
g = 2
prime = 7919
bits = 256
print_line()
print "GENERATOR (Public):  ", g
print "PRIME (Public):      ", prime
print "BITS (Public):       ", bits
print_line()

## Calculations
a = getrandbits(bits)
A = pow(g, a, prime)
b = getrandbits(bits)
B = pow(g, b, prime)

print "a (Private):         ", a
print "Calculate A using GENERATOR^a (mod PRIME)"
print "A (Public, message): ", A
print_line()
print "b (Private):         ", b
print "Calculate B using GENERATOR^b (mod PRIME)"
print "B (Public, message): ", B
print_line()

s1 = pow(A, b, prime)
s2 = pow(B, a, prime)

if s1==s2:
    print "Shared secrets match: ", s1
