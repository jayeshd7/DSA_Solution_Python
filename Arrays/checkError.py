
def checkError():
    try:
        letters = ["a", "b"]
        print(letters[2])
    except ValueError as valueError:
        print("value error has occured")
    except IndexError as indexError:
        print("index error has occured")
    except SyntaxError as error:
        print("error has occured")

checkError()

