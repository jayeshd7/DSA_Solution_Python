def checkError():
    try:
        letters = ["a", "b"]
        print(letters[2])
    except (ValueError, IndexError):
        print("error has occured")


checkError()
