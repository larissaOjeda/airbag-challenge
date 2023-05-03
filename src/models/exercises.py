from database.db import get_connection
from typing import DefaultDict, List, Optional, Tuple
from pydantic import , ValidationError

from datetime import datetime
import pandas as pd
from pandas import DataFrame
import io
import random
from flask import Response


class Exercises: 

    @classmethod
    def printCombinations() -> list:
        """
        Generates all possible combinations of three distinct digits in ascending order

        Returns
            list of strings with all the possible combinations of the three different digits asc 
        """
        res = []
        for n in range(0, 10):
            for m in range(n+1, 10):
                for k in range(m+1, 10):
                    res.append(f"{n}{m}{k}")
        return res 

    @classmethod
    def clearDuplicates(numList: list[]) -> Optional[list[float]]:
        """
        Removes duplicate items from a list of numbers and returns the resulting list.
        numList is expected to be a list of integers or floats, and returns a list of floats or None if the input list is None.

        Args
            numList: list of integers or floats.

        Returns
            A list of unique float values or None if the input list is None.
        
        Exceptions
            If an exception occurs it is caught and raised.
        """
        if numList is None: 
            return None 
        if len(numList) == 0: 
            return numList
        try:
            return list((set(numList)))
        except Exception as ex: 
            raise Exception(ex)
    
    @classmethod
    def caesar_cipher(message: str, shift: int) -> str:
        """
        Encrypts a given message using a Caesar cipher
        It is assumed that the message does not contain numbers or special characters (e.g. ".,;:-%$#" or more)

        Args:
            message: string to be encrypted
            shift: integer indicating the number of positions to shift each letter by

        Returns:
            encrypted message: string containing the encrypted message
        """
        encrypted_message = ""
        for char in message:
            if char.isalpha():
                shifted_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
                if char.isupper():
                    shifted_char = shifted_char.upper()
                encrypted_message += shifted_char
            else:
                encrypted_message += char
        return encrypted_message


    @classmethod
    def evalExpression(expression: str) -> Optional[float]:
        """
        Calculates the value of a given arithmetic expression

        Args
            expression: The arithmetic expression to be evaluated.

        Returns
            float: The calculated value of the expression.
        """

        expression = expression.replace(" ", "") # removing spaces
        stack = []
        i = 0

        while i < len(expression):
            character = expression[i]

            if character.isdigit():
                j = i + 1
                while j < len(expression) and expression[j].isdigit():
                    j += 1
                number = float(expression[i:j])
                stack.append(number)
                i = j

            elif character in "+-*/":
                stack.append(character)
                i += 1

            elif character == "(":
                count = 1
                j = i + 1
                while j < len(expression) and count > 0:
                    if expression[j] == "(":
                        count += 1
                    elif expression[j] == ")":
                        count -= 1
                    j += 1
                number = Exercises.evalExpression(expression[i+1:j-1])
                stack.append(number)
                i = j

            elif character == ")":  # If its a right parenthesis return the result of the expression
                break

        # Operators priority: multiplication and division first
        i = 1
        while i < len(stack) - 1:
            if stack[i] == "*":
                stack[i-1:i+2] = [stack[i-1] * stack[i+1]]
            elif stack[i] == "/":
                if stack[i+1] == 0:
                    raise ZeroDivisionError("Division by zero")
                stack[i-1:i+2] = [stack[i-1] / stack[i+1]]
            else:
                i += 2

        # Operators priority: addition and subtraction  second
        result = stack[0]
        for i in range(1, len(stack), 2):
            if stack[i] == "+":
                result += stack[i+1]
            elif stack[i] == "-":
                result -= stack[i+1]

        return result

        

        








