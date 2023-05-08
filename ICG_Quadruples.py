class Quadruple:
    def __init__(self, op, arg1=None, arg2=None, res=None):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.res = res

    def __repr__(self):
        if self.op in ['+', '-', '*', '/', '=']:
            return f"{self.op}\t\t{self.arg1}\t\t{self.arg2}\t\t{self.res}"
        elif self.op == 'if':
            return f"{self.op}\t{self.arg1}\t\t\t\t{self.res}"
        elif self.op == 'goto':
            return f"{self.op}\t\t\t\t\t{self.res}"
        elif self.op == 'label':
            return f"{self.res}:"
        elif self.op == 'print':
            return f"{self.op}\t\t{self.arg1}"


def gen_code():
    quadruples = []
    examples = []
    n = int(input("Enter number of statements: "))
    for i in range(n):
        op = input(f"Enter operator for statement {i+1}: ")
        if op in ['+', '-', '*', '/', '=']:
            arg1 = input("Enter argument 1: ")
            arg2 = input("Enter argument 2: ")
            res = input("Enter result: ")
            quadruple = Quadruple(op, arg1, arg2, res)
            quadruples.append(quadruple)
            examples.append(f"{res} = {arg1} {op} {arg2}")
        elif op == 'if':
            arg1 = input("Enter condition: ")
            res = input("Enter label: ")
            quadruple = Quadruple(op, arg1=arg1, res=res)
            quadruples.append(quadruple)
            examples.append(f"if {arg1} goto {res}")
        elif op == 'goto':
            res = input("Enter label: ")
            quadruple = Quadruple(op, res=res)
            quadruples.append(quadruple)
            examples.append(f"goto {res}")
        elif op == 'label':
            res = input("Enter label: ")
            quadruple = Quadruple(op, res=res)
            quadruples.append(quadruple)
            examples.append(f"{res}:")
        elif op == 'print':
            arg1 = input("Enter argument: ")
            quadruple = Quadruple(op, arg1=arg1)
            quadruples.append(quadruple)
            examples.append(f"print {arg1}")
    print("\nExample Quadruple Statements:")
    for i, ex in enumerate(examples):
        print(f"t{i+1} = {ex}")
    return quadruples


def main():
    quadruples = gen_code()
    print(f"\n Intermediate Code Generated: (Quadruple Table)")
    print("Operator\tOperand 1\tOperand 2\tResult")
    for q in quadruples:
        print(q)
    

if __name__ == '__main__':
    main()

# Enter number of statements: 2
# Enter operator for statement 1: =
# Enter argument 1: 2
# Enter result: x
# Enter operator for statement 2: *
# Enter argument 1: 3
# Enter argument 2: x
# Enter result: y
# Intermediate Code Generated:
# Operator        Operand 1       Operand 2
# =               2               x
# *               3               x
