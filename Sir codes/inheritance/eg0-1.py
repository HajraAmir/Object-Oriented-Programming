class natnum(int):
    pass

def main():
    x = natnum(2231)
    print("type(x)", type(x))
    print("type(x+2)", type(x+2))
    print(x+2)

main()
