# import requests
# import inspect
#
# print(inspect.ismodule(requests))
# print(inspect.isclass(requests.session))
# print(inspect.isfunction(requests.get))
#
#

data = "string"

# def fun():
#     pass

# for method in dir(data):
#     print(method)

for method in dir(data):
    if method.startswith("s"):
        print(method)

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
