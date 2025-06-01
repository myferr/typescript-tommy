from ollama_generation import Generate
from args import *
import os
import random
import string

randomString = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))

def Create_Output(file = randomString + ".md"):
    if (GetArg(index=1) == "--output"):
        print("Output flag detected")
        if (GetArg(index=2) != None):
            print("Output file detected")
            file = GetArg(index=2)
        else:
            file = randomString + ".md"
    else:
        file = randomString + ".md"
        
    os.system(f'echo """{Generate(subject=GetArg(2))}""" > {file}')
    print("Course generated.")
