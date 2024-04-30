#original code:
#def throw_me_an_error():
#  val1 = 14
#  val2 = 0
#  return val1 / val2

def throw_me_an_error():
    try: #original code to test:
        val1 = 14
        val2 = 0
        result = val1 / val2 #0 division
    except Exception as e: #error handling
        print(e)

throw_me_an_error()
##from documentation : exception ZeroDivisionError
    #Raised when the second argument of a division or modulo operation is zero. The associated value is a string indicating the type of the operands and the operation.