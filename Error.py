def checkString(var):
    if type(var) != str:
        raise TypeError(f"Sorry, we can't work with {type(var)}, we need str")
    else:
        return var

# try:
#     print("start")
#     print(10/0)
#     print("no errors")
try:
    print(checkString(1))

except NameError as error:
    print(error)

except ZeroDivisionError as error:
    print(error)

print("code after")