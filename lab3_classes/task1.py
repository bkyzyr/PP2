class StringManipulator:
    def inputing(self):
        return input("Enter a string: ")
    
    def printing(self, string):
        print(string.upper())

sm = StringManipulator()
user_string = sm.inputing()
sm.printing(user_string)
