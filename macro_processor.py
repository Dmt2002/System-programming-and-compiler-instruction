def macro_def(lines):

    # Extract macro definition
    macro_def = []
    j=0
    line = lines[j].strip()

    while line != 'endm':
        macro_def.append(line)
        j+=1
        line = lines[j].strip()
    macro_def.append(lines[j].strip())

    return macro_def

def parse_alp(alp_program):
    macro_def_table = {}
    macro_name_table = []
    arg_list_array = []

    with open(alp_program, 'r') as f:
        lines = f.readlines()

        for i in range(len(lines)):
            line = lines[i].strip()

            # If line is a macro definition
            if line.__contains__('macro'):
                # Extract macro name and argument list
                macro_name = line.split()[0]
                macro_name_table.append(macro_name)
                arg_list_array += line.split()[2:]

                # Add macro definition to macro definition table
                macro_def_table[macro_name] = macro_def(lines[i+1:])
                    

    return macro_def_table, macro_name_table, arg_list_array

# Second Pass
def expanded_code(alp_program,macro_def_table, macro_name_table,expanded_program):
     
     with open(alp_program, 'r') as f, open(expanded_program, 'w') as f_out:
        lines = f.readlines()

        for i in range(len(lines)):
            line = lines[i].strip()

            if line.split()[0] in macro_name_table and not line.__contains__('macro'):
                macro_name = line.split()[0]
                macro_args = line.split()[1]

                for macro_line in macro_def_table[macro_name]:
                    if macro_line.__contains__('xx'):
                        new_macro_line = macro_line.replace('xx',macro_args)
                        f_out.write(new_macro_line + '\n')
                        continue
                    elif macro_line.__contains__('endm'):
                        continue
                    f_out.write(macro_line + '\n')
            else:
                f_out.write(line + '\n')
                    

# Example usage
alp_program = "sample.asm"
expanded_program = "expanded.asm"

macro_def_table, macro_name_table, arg_list_array = parse_alp(alp_program)

# print(macro_def_table)    # Output: {'ADD': ['MOV A,X', 'ADD A,Y', 'MOV X,A']}
# print(macro_name_table)   # Output: ['ADD']

print()
print("Macro Name Table (MNT):")
for macro_name in macro_name_table:
    row0 = "Index\tMacro Name\t MDT Index"
    print(row0)
    row = f"{macro_name_table.index(macro_name)}\t{macro_name}\t\t{list(macro_def_table).index(macro_name)}"
    print(row)
print()
print("Macro Definition Table(MDT):")

MDT = []
for macro in macro_def_table:
    MDT.extend(macro_def_table[macro])
row1 = "Index\tCard"
print(row1)
for i in range(len(MDT)):
    
    row = f"{i}\t{MDT[i]}"
    print(row)


print("\nArgument List Array (ALA):")
row1 = "Index\tArgument"
print(row1)
for i in range(len(arg_list_array)):
    row = f"{i}\t{arg_list_array[i]}"
    print(row)

expanded_code(alp_program,macro_def_table, macro_name_table,expanded_program)
