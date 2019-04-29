from stack import * #Import everything regarding class Stack


def test_integers():
    print("int test")
    s = Stack(7) #Class Stack for integer inputs
    s.push(5) #Put 5 into the list stack
    t = s.pop() #Remove 5
    print(t) #Show result


def test_floats():
    print("float test")
    s = Stack(2.3) #Class Stack for float inputs
    s.push(5.0) #Put 5.0 into the list stack
    t = s.pop() #Remove 5.0
    print(t) #Show result




def test_strings():
    print("string test")
    s = Stack("") #Class Stack for string inputs
    s.push("Sharks suck") #Put string into the list stack
    t = s.pop() #Remove string
    print(t) #Show result



def test_exception():
    print("exception test")
    s = Stack(5) #Class Stack for integer inputs
    s.push("Sharks suck") #Not an integer so freak out!
    t = s.pop() #Remove string
    print(t) #Show result

def safe_test_int_exception(): #Only keep ints out
    print("safe int test")
    s = IntStack()
    s.push(1.0)


def safe_test_int(): #Only lets ints in
    print("safe non int test")
    s = IntStack()
    s.push(5)

if __name__ == '__main__':



     try:
         test_exception() #Run the test exception function

     except ValueError: #If the value doesn't match the stack value
         print("exception test value error") #Print this error


     try:
         test_strings() #Run the test strings function

     except ValueError: #If the value doesn't match the stack value
         print("string test value error") #Print this error



     try:
         test_integers() #Run the test integers function

     except ValueError: #If the value doesn't match the stack value
         print("integer test value error") #Print this error



     try:
         test_floats() #Run the test floats function

     except ValueError: #If the value doesn't match the stack value
         print("float test value error") #Print this error




     try:
         safe_test_nonint() #Run the safe test for non ints function

     except ValueError: #If the value doesn't match the stack value
         print("safe test non int value error") #Print this error


     try:
         safe_test_int() #Run the safe test for ints function

     except ValueError: #If the value doesn't match the stack value
         print("safe test int value error") #Print this error
         

