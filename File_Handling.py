## Basic Try-Except Block

try:
    f = open("file.txt")
    try:
        f.read("file.txt")
    except:
        print("Something went wrong when reading the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


def nameAge(name, age):
    if not isinstance(age, int):
        print('Age is not a whole number')
        return

    print('Your name is', name, 'and you are', age)

name = input('Enter name: ')
try:
    age = int(input('Enter age: '))
except ValueError:
    print('Invalid age')
finally:
    result = nameAge(name, age)
