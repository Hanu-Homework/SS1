import tabulate


def gcd(num1, num2):
    return num1 if num2 == 0 else gcd(num2, num1 % num2)


def gcd_with_table(num1, num2):
    steps = []
    ret = 1

    while num2 != 0:
        steps.append((num1, num2, num1 // num2, num1 % num2))

        if num1 % num2 == 0:
            ret = num2

        temp = num1 % num2
        num1 = num2
        num2 = temp

    return steps, ret


def walk_and_change_if_equals(args, target, num1, num2) -> None:
    for index, arg in enumerate(args):
        if isinstance(arg, list):
            walk_and_change_if_equals(arg, target, num1, num2)
        else:
            if arg == target:
                args[index] = [num1, num2]  # num1 - num2


def walk_and_print(args, result=""):
    assert len(args) == 2

    so_bi_tru, so_tru = args

    if isinstance(so_bi_tru, list):
        print("(", end="")
        walk_and_print(so_bi_tru)
        print(")", end="")
    else:  # is number
        print(so_bi_tru, end="")

    print(" - ", end="")

    if isinstance(so_tru, list):
        print("(", end="")
        walk_and_print(so_tru)
        print(")", end="")
    else:  # is number
        print(so_tru, end="")


def walk_and_group():
    pass


# a = int(input("a: "))
# b = int(input("b: "))
# n = int(input("n: "))
a = 28
b = 8
n = 48

steps, d = gcd_with_table(a, n)

print("Step 1: ")
print(tabulate.tabulate(steps, headers=["Dividend", "Divisor", "Quotient", "Remainder"]))
print(f"gcd({a}, {n}) = {d}\n")

print("Step 2: ")
if b % d != 0:
    print("No root since b % d != 0")
    exit(0)
print("b % d == 0: True. Continue to Step 3\n")

print("Step 3: ")
print("d = n * s + a * r")
print(f"{d} = {n} * s + {a} * r")

print("Finding s and r:")

steps.reverse()

args = [steps[1][0], steps[1][1]]
to_separate = steps[1][1]
for step in steps[1:-2]:
    dd, dr, q, r = step
    # print(f"{r} = {dd} - ({dd + dr} - {dd}) * {q}")

    walk_and_change_if_equals(args, to_separate, dd + dr, dd)
    walk_and_print(args)
    print()

    to_separate = dd
