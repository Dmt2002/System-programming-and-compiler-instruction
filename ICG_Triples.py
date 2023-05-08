class Triple:
    def __init__(self, op, arg1=None, arg2=None, res=None):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.res = res

    def __repr__(self):
        if self.op in ['+', '-', '*', '/', '=']:
            return f"{self.res} = {self.arg1} {self.op} {self.arg2}"
        elif self.op == 'if':
            return f"if {self.arg1} goto {self.res}"
        elif self.op == 'goto':
            return f"goto {self.res}"
        elif self.op == 'label':
            return f"{self.res}:"
        elif self.op == 'print':
            return f"print {self.arg1}"

def gen_code():
    triples = []
    examples = []
    n = int(input("Enter number of statements: "))
    for i in range(n):
        op = input(f"Enter operator for statement {i+1}: ")
        if op in ['+', '-', '*', '/', '=']:
            arg1 = input("Enter argument 1: ")
            arg2 = input("Enter argument 2: ")
            res = input("Enter result: ")
            triple = Triple(op, arg1, arg2, res)
            triples.append(triple)
            examples.append(f"{res} = {arg1} {op} {arg2}")
        elif op == 'if':
            arg1 = input("Enter condition: ")
            res = input("Enter label: ")
            triple = Triple(op, arg1=arg1, res=res)
            triples.append(triple)
            examples.append(f"if {arg1} goto {res}")
        elif op == 'goto':
            res = input("Enter label: ")
            triple = Triple(op, res=res)
            triples.append(triple)
            examples.append(f"goto {res}")
        elif op == 'label':
            res = input("Enter label: ")
            triple = Triple(op, res=res)
            triples.append(triple)
            examples.append(f"{res}:")
        elif op == 'print':
            arg1 = input("Enter argument: ")
            triple = Triple(op, arg1=arg1)
            triples.append(triple)
            examples.append(f"print {arg1}")
    print("\nExample Triple Statements:")
    for i, ex in enumerate(examples):
        print(f"t{i+1} = {ex}")
    return triples


def main():
    triples = gen_code()
    print(f"\n Intermediate Code Generated: (Triple Table)")
    print("Operator\tOperand 1\tOperand 2")
    for t in triples:
        if t.op in ['+', '-', '*', '/', '=']:
            print(f"{t.op}\t\t{t.arg1}\t\t{t.arg2}")
        elif t.op == 'if':
            print(f"{t.op}\t{t.arg1}\t\t\t\t{t.res}")
        elif t.op == 'goto':
            print(f"{t.op}\t\t\t\t\t{t.res}")
        elif t.op == 'label':
            print(f"{t.res}:")
        elif t.op == 'print':
            print(f"{t.op}\t\t{t.arg1}")
    

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
