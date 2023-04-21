#In this kata, your job is to create a class Dictionary which you can add words to and their entries.
class Dictionary():
    def __init__(self):
        self.new_dictionary = {}
         
    def newentry(self, word, definition):
        self.new_dictionary[str(word)] = definition
        
    def look(self, key):
        if key in self.new_dictionary:
            return self.new_dictionary[str(key)]
        else:
            return f"Can't find entry for {key}"