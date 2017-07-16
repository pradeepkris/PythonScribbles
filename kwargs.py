def Func(*args, **kwargs):
    for arg in args:
        print arg

    for item in kwargs.items():
        print item

Func(1, 2, 3, x='ham', *[1, 2, 3])


# def outside(x=5):
#     def inside():
#         print x
#
#     return inside
#
# d = outside()
# d()
