x: int = 123
x = "jayesh"

'''
Type hinting - mypy 
providing hint if type is mismatched.
and always use data type something like 
value :str 
so developer life will be easy 

'''

def stringConvertIntoUpperCase(value: str):
    return value.upper()


print(stringConvertIntoUpperCase("jaysh"))


def sum(a:int, b:int) ->int:
    print(a+b)
    return a+b

sum(1,2)