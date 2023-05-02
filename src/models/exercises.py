from database.db import get_connection
from .entities.ChargingDetails import ChargingDetails
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
            return f"Provided list is empty"
        try:
            return list((set(numList)))
        except Exception as ex: 
            raise Exception(ex)
        








