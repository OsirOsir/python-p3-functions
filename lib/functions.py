#!/usr/bin/env python3


def greet_programmer():
    print("Hello, programmer!")  # Add the exclamation mark

def greet(name):
    print(f"Hello, {name}!")  # Add the exclamation mark

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")  # Add the exclamation mark

def add(num1, num2):
    return num1 + num2  # This function is correct as it is

def halve(number):
    if type(number) not in (int, float): 
        return None  # Return None if the input is not a number
    return number / 2  # Return half of the number
