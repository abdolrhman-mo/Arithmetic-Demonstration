myInput = "2+ 1- 34*4 / 3 + 4"

problem = ""

# removing unuseful spaces
for item in myInput:
    if item != " ":
        problem = problem + item

operators = ['+', '-', '*', '/']

# giving the operators a spaces for split function to split everything
for operator in operators:
    if operator in problem:
        problem = problem.replace(operator, f" {operator} ")

# split function convert numbers and operators into a list
problem = problem.split()

operators_dic = {
    '*': 'multiplication',
    '/': 'division',
    '+': 'addition',
    '-': 'subtraction'
}


def operation(item, item_index):
    # Doing the operation
    if item == '*' or item == '/':
        print()
        print("we first do multiplication and division".upper())
        print()
        if item == "*":
            operation_ans = int(problem[item_index - 1]) * \
                int(problem[item_index + 1])
        elif item == "/":
            operation_ans = int(problem[item_index - 1]) / \
                int(problem[item_index + 1])
    elif item == '+' or item == '-':
        print()
        print("we then do addition and subtraction".upper())
        print()
        if item == "+":
            operation_ans = int(problem[item_index - 1]) + \
                int(problem[item_index + 1])
        elif item == "-":
            operation_ans = int(problem[item_index - 1]) - \
                int(problem[item_index + 1])

    # illustration
    print(f"{operators_dic[item]}: ", end="")
    print(
        f"{problem[item_index - 1]} {item} {problem[item_index + 1]} = ", end="")
    print(operation_ans)

    # updating the problem
    problem[item_index] = operation_ans

    del problem[item_index + 1]
    del problem[item_index - 1]

    # print problem updated
    print("=", " ".join(str(item) for item in problem))


print("Problem:", " ".join(str(item) for item in problem))

for count in range(100):
    for item, item_index in zip(problem, range(len(problem))):
        if item == '*' or item == '/':
            # print()
            # print(3 * "_", f"{item}", 3 * "_", end="")
            # print(f"\tindex: {item_index}")

            # print(f"item: {item} is '*' or '/'")
            operation(item, item_index)
            break
        else:
            # print(f"item: {item} is not a '*' or '/' ")
            pass

for count in range(100):
    for item, item_index in zip(problem, range(len(problem))):
        if item == '+' or item == '-':
            # print()
            # print(3 * "_", f"{item}", 3 * "_", end="")
            # print(f"\tindex: {item_index}")

            # print(f"item: {item} is '*' or '/'")
            operation(item, item_index)
            break
        else:
            # print(f"item: {item} is not a '*' or '/' ")
            pass
