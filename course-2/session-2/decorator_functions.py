#!/usr/bin/env python3

def decorate(func):
    print('in decorate function, decorating', func.__name__)
    def wrapper_func(*args):
        print("Executing', func.__name__)
        return func(*args)
    return wrapper_func

def myfunc(parameter):
    print(parameter)


if __name__=='__main__':
    myfunc=decorate(myfunc)
    print(myfunc)


    myfunc("hello")

    exit(0)
