from art import logo
from replit import clear
print("２０２０ ｜ ＠Ｃｍｌｏｈｒ")
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

ops = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
    print(logo)

    num1 = float(input("Number?:\n> "))
    for sym in ops:
        print(sym)

    cont = True
    while cont:
        opp_sym = input("Symbol:\n> ")
        num2 = float(input("Number?:\n> "))
        calc_func = ops[opp_sym]
        answer = calc_func(num1, num2)
        
        print(f"{num1} {opp_sym} {num2} = {answer}")
        print("---------------------")
        if input(f"'y' to continue\n'n' to start new.\n> ").lower() == "y":
            num1 = answer
            print("---------------------")
            print(f"{answer}")
        else:
            cont = False
            clear()
            calculator()
calculator()