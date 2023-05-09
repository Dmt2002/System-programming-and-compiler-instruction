code = '''
x = a + b - b + 1;
y = b + 3 - 3 * 1;
w = 3
u = 2
z = a * 1 / 1 + b * 1 / u;
if z < 0:
    x = 0;
else:
    x = x + 1;
'''

# Perform constant propagation
constants = {}
for line in code.split("\n"):
    if "=" in line:
        var, exp = line.split("=")
        var = var.strip()
        exp = exp.strip()
        for const_var, const_val in constants.items():
            exp = exp.replace(const_var, str(const_val))
        if all([c.isdigit() for c in exp]):
            constants[var] = eval(exp)
        else:
            constants.pop(var, None)

new_code = ""
for line in code.split("\n"):
    if "=" in line:
        var, exp = line.split("=")
        var = var.strip()
        exp = exp.strip()
        for const_var, const_val in constants.items():
            exp = exp.replace(const_var, str(const_val))
        new_code += var + " = " + exp + ";\n"
    else:
        new_code += line + "\n"

# Perform dead code elimination
new_code_lines = new_code.split("\n")
new_code_lines = [line for line in new_code_lines if "w =" not in line]
new_code = "\n".join(new_code_lines)

print(new_code)
