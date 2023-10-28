import requests
import inspect
import sys

print(sys.executable)
print(sys.version)
print(sys.platform)

# print(inspect.ismodule(requests))
# print(inspect.isclass(requests.session))
# print(inspect.isfunction(requests.get))
#
#

# data = "string"
#
# dir()
#
# # def fun():
# #     pass
#
# # for method in dir(data):
# #     print(method)
#
# startLetter = input("Input start letter: ")
#
# for method in dir(data):
#     if method.startswith(startLetter.lower()):
#         print(method)

# print(getattr(data, "reverse", None))
# print(getattr(data, "index", None))
# print("callable data - ", callable(data))
# print("callable fun - ", callable(fun))
#
# class Parent:
#     pass
#
# class Child(Parent):
#     pass
#
# print(issubclass(Parent, Child))
# print(issubclass(Child, Parent))
#
# petr = Parent()
# petrPetrivich = Child()
#
# print(isinstance(petr, Parent))
# print(isinstance(petrPetrivich, Child))
