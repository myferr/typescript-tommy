import sys

def GetArg(index, flag = False):
    try:
        if (flag == True):
            arg = f"--{sys.argv[index]}"
        else:
            arg = sys.argv[index]
        return arg
    except IndexError:
        return None

def GetArgList():
    return sys.argv
