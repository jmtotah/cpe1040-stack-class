

class Stack():
    def __init__(self, sample): #Paramiters for Stack
        self.stack = [] #List that gets added to
        self.sample = sample #Self needed so that the def's can comunnicate
        print("New Stack object")


    def pop(self): #For removing items from the list
        print("Popping...")
        return self.stack.pop()

    def push(self, value): #For adding items to the list
        if not isinstance(value, type(self.sample)): #If the value inputted is not the same type as sample
            raise ValueError('Expected integer but got {}'.format(type(value))) #Show this error
        else:
            self.stack.append(value) #Otherwise add it to the list
            print("Pushing...") #And print pushing



class IntStack(Stack): #To allow for int only check
    def __init__(self):
        Stack.__init__(self,0)









