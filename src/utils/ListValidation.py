class ListValidation(): 

     @classmethod 
     def is_list_valid(self, numList):
        for element in numList: 
            try: 
                float(element)
            except: 
                return False
        return True