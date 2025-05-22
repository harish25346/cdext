import re
file=input("Enter file name: ")
buffer=""
def divide(input):
    pattern=r"[\s]+|([+\-*/=(){};,])"
    tokens=re.split(pattern,input)
    return [token for token in tokens if token and not token.isspace()]
try:
    with open(file,"r") as f:
        buffer=f.read()
        op=divide(buffer)
        print(op)
except FileNotFoundError:
    print("File not found")