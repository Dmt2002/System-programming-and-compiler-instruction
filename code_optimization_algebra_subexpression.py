code = ''' 
x = a+1
y = b*1
c = j/1
u = d+e
v = d+e
'''

# Perform algebraic simplification
new_code = ""
for line in code.split("\n"):
    if "=" in line:
        var, exp = line.split("=")
        var = var.strip()
        exp = exp.strip()
        if "+1" in exp:
            exp = exp.replace("+1", "")
        if "*1" in exp:
            exp = exp.replace("*1", "")
        if "/1" in exp:
            exp = exp.replace("/1", "")
        new_code += var + " = " + exp + ";\n"
    else:
        new_code += line + "\n"

# Perform common subexpression elimination
new_code_lines = new_code.split("\n")
subexpressions = {}
for i in range(len(new_code_lines)):
    line = new_code_lines[i]
    if "=" in line:
        var, exp = line.split("=")
        exp = exp.strip()
        if exp in subexpressions:
            new_code_lines[i] = var.strip() + " = " + subexpressions[exp] + ";\n"
        else:
            subexpressions[exp] = var.strip()
new_code = "\n".join(new_code_lines)

print(new_code)
