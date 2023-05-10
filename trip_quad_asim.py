tac = '''t1 = a + b
t2 = c + d
t3 = t1 + t2
t4 = - d
a = t3'''
lines = tac.split("\n")
print("Triples: ")
print("{: ^10}{: ^10}{: ^10}".format("Operator","Arg 1","Arg 2"))

for line in lines:
    assignment = line.split(" = ")
    right_side = assignment[1].split(" ")
    
    if len(right_side) == 3:
        print("{: ^10}{: ^10}{: ^10}".format(right_side[1],right_side[0],right_side[2]))
    elif len(right_side) == 2:
        print("{: ^10}{: ^10}{: ^10}".format("u"+right_side[0],right_side[1]," "))    
    elif len(right_side) == 1:
        print("{: ^10}{: ^10}{: ^10}".format("=",right_side[0]," "))
        
 tac = '''t1 = a + b
t2 = c + d
t3 = t1 + t2
t4 = - d
a = t3'''
lines = tac.split("\n")
print("Quadraples: ")
print("{: ^10}{: ^10}{: ^10}{: ^10}".format("Operator","Arg 1","Arg 2","Result"))

for line in lines:
    assignment = line.split(" = ")
    left_side = assignment[0]
    right_side = assignment[1].split(" ")
    
    if len(right_side) == 3:
        print("{: ^10}{: ^10}{: ^10}{: ^10}".format(right_side[1],right_side[0],right_side[2],left_side))
    elif len(right_side) == 2:
        print("{: ^10}{: ^10}{: ^10}{: ^10}".format("u"+right_side[0],right_side[1]," ",left_side))    
    elif len(right_side) == 1:
        print("{: ^10}{: ^10}{: ^10}{: ^10}".format("=",right_side[0]," ",left_side))
