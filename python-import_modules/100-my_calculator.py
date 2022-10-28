#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    if(len(sys.argv) != 4):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    arg1 = sys.argv[2]
    arg = sys.argv[1]
    arg2 = sys.argv[3]
    if arg1 == "+":
        print('{} {} {} = {}'.format(arg,
              arg1,
              arg2, add(int(arg), int(arg2))))
    elif arg1 == "-":
        print('{} {} {} = {}'.format(arg,
              arg1,
              arg2, sub(int(arg), int(arg2))))
    elif arg1 == "*":
        print('{} {} {} = {}'.format(arg,
              arg1,
              arg2, mul(int(arg), int(arg2))))
    elif arg1 == "/":
        print('{} {} {} = {}'.format(arg,
              arg1,
              arg2, div(int(arg), int(arg2))))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)