class CaesarCipher(): 

    def __init__(self, id, message = None, n = None):
        self.id = id
        self.message = message
        self.n = n

    def to_JSON(self):
        return {
            'id' : self.id,
            'message' : self.message,
            'n' : self.n
        }