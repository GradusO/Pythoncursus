try:
    filename = input("Enter a file to open? ")
    f = open(filename)
except FileNotFoundError:
    print("File does not exist")
except IsADirectoryError:
    print("That is a folder")