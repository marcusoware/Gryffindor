import sys

def main():
    my_sys_func():

def my_sys_func():

    for arg in argument[1:]:
        if arg == "-m" or arg == "module":
            print("module")
        elif arg == "-p" or arg == "path":
            print("path")
        else:
            print("too few argument ")


if __name__ ==   cd