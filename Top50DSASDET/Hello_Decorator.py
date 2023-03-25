def Hello_Decorator(func):

    def inner1():
        print("Hello , this is before function execution")

        func()

        print("this is after function execution")
    return inner1

def function_to_be_used():
    print("This is inside a function")

function_to_be_used = Hello_Decorator(function_to_be_used)
function_to_be_used()

