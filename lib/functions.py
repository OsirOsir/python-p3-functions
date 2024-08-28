#!/usr/bin/env python3


def greet_programmer():
    print("Hello, programmer!")  

def greet(name):
    print(f"Hello, {name}!")  

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")  

def add(num1, num2):
    return num1 + num2  

def halve(number):
    if type(number) not in (int, float): 
        return None  # Return None if the input is not a number
    return number / 2  # Return half of the number