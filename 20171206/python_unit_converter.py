#!/usr/bin/env python
# coding=utf-8

factor = 0.6214

# Program greets user and describes what's the purpose of the program
greeting = "hello, welcome to my unit converter. This tool helps you to convert kilometers to miles."
print greeting
print "*" * 20

# Program asks user to enter number of kilometers
while True:
    kilometers = int(raw_input("Please enter the number of kilometres: "))
    print "You entered " + str(kilometers)

# User enters the amount of kilometers

# Program converts these kilometers into miles and prints them.
    print kilometers, "Kilometers are", kilometers * factor, "miles."

# Program asks user if they'd want to do another conversion
    exit = raw_input("Would you like to do another conversion? Type n to exit.")
    if exit == "n":
        print "Ok, thanks and goodbye. See you soon."
        break
